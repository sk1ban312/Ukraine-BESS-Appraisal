"""Financial model of the 20 MW / 40 MWh BESS (document 04). Nominal USD, years 0..15."""
import numpy as np
import numpy_financial as npf

FX = 45.05
BASE = dict(
    capex=241*40000 + 372*20000 - 17/334*(241*40000 + 372*20000) + 3.053e3*20000/FX + 24.32e9/250/FX,
    nrel=241*40000 + 372*20000, fom_rate=0.04, ins_rate=0.02, network=2499*1643.69/FX, other=150000,
    arb=2430967.09, afrr_b=2825082.66, afrr_c=1569490.37, arb_c=1215483.54,
    mkt_dc=80, mkt_freight=0.05, mkt_pcs=30, mkt_epc_4h=50, mkt_owner_rate=0.10,   # market case, technical basis D.5
    g=0.025, tax=0.18, life=15, hurdle=0.15, dscr_contract=1.20, dscr_merchant=2.0, max_gear=0.70,
)
FIN = {'commercial': dict(rate=0.0611, tenor=5), 'ifi': dict(rate=0.070, tenor=10)}

def market_system(p):
    """Installed battery system cost of the market case, USD (technical basis D.5).
    'tender' (default): DC block free-on-board China + freight + PCS/EMS + EPC, plus owner's costs. EPC is
        Ember's 4-hour tender price converted to 2 hours with NREL's split of all costs other than battery
        cabinets and inverter: 31 USD/kWh + 268 USD/kW (= 98 USD/kWh at 4 hours).
    'nrel_bos': the market DC block (with freight) replaces NREL's battery cabinets (210 USD/kWh);
        all other NREL items are kept, less US sales tax."""
    E, P = 40000, 20000
    dc = p['mkt_dc'] * E * (1 + p['mkt_freight'])
    if p.get('mkt_variant', 'tender') == 'nrel_bos':
        return p['nrel'] * (1 - 17/334) - 210 * E + dc
    epc = p['mkt_epc_4h'] * (31 * E + 268 * P) / 98
    return (dc + p['mkt_pcs'] * P + epc) * (1 + p['mkt_owner_rate'])

def run(scen, fin, **over):
    p = {**BASE, **over}; f = {**FIN[fin], **{k: v for k, v in over.items() if k in ('rate', 'tenor')}}
    n = p['life']; t = np.arange(1, n + 1); esc = (1 + p['g']) ** (t - 1)
    if p.get('capex_case', 'nrel') == 'market':
        sys_cost = market_system(p) * p.get('sys_mult', 1.0)   # sys_mult: break-even search on the installed system price
        capex = (sys_cost + 3.053e3*20000/FX + 24.32e9/250/FX) * p.get('capex_mult', 1.0)
        p.setdefault('fom_abs', p['fom_rate'] * sys_cost * p.get('capex_mult', 1.0))
    else:
        capex = p['capex'] * p.get('capex_mult', 1.0)
    arb_mult = p.get('arb_mult', 1.0); afrr_mult = p.get('afrr_mult', 1.0); av = p.get('avail_mult', 1.0)
    if scen == 'A': arb, afrr = p['arb'] * arb_mult * av, 0.0
    elif scen == 'B': arb, afrr = 0.0, p['afrr_b'] * afrr_mult * av
    else: arb, afrr = p['arb_c'] * arb_mult * av, p['afrr_c'] * afrr_mult * av
    rev = arb * esc + afrr
    merchant = arb / (arb + afrr) if arb + afrr else 1.0
    fom = p.get('fom_abs', p['fom_rate'] * p['nrel'])
    opex = (fom + p['network'] + p['other'] * p.get('other_mult', 1.0)) * esc + p['ins_rate'] * capex
    ebitda = rev - opex
    capex = capex - p.get("grant", 0.0)   # capital grant: cuts the amount financed and depreciated; insurance stays on the gross cost
    dep = capex / n
    unlev_tax = np.maximum(0, ebitda - dep) * p['tax']           # simple: no loss carry-forward for sizing
    cfads_sizing = ebitda - unlev_tax
    K = p.get('contract_years', p['life'])   # years in which lenders count aFRR as contracted (base: whole life)
    m_t = np.where(t <= K, merchant, 1.0)
    dscr_v = p['dscr_contract'] * (1 - m_t) + p['dscr_merchant'] * m_t; dscr_t = dscr_v[0]
    r, T = f['rate'], f['tenor']
    debt_dscr = max(0.0, -npf.pv(r, T, (cfads_sizing[:T] / dscr_v[:T]).min()))
    debt = min(p['max_gear'] * capex, debt_dscr)
    pmt = -npf.pmt(r, T, debt) if debt > 0 else 0.0
    bal = debt; interest = np.zeros(n); principal = np.zeros(n)
    for i in range(T):
        interest[i] = bal * r; principal[i] = pmt - interest[i]; bal -= principal[i]
    # tax with loss carry-forward
    ebt = ebitda - dep - interest; tax = np.zeros(n); lcf = 0.0
    for i in range(n):
        base = ebt[i] - lcf
        if base > 0: tax[i] = base * p['tax']; lcf = 0.0
        else: lcf = -base
    cfads = ebitda - tax; ds = interest + principal
    with np.errstate(divide='ignore', invalid='ignore'):
        dscr = np.where(ds > 0, cfads / ds, np.nan)
    eq = np.concatenate([[-(capex - debt)], cfads - ds])
    proj = np.concatenate([[-capex], ebitda - np.maximum(0, ebitda - dep) * p['tax']])
    irr = lambda x: npf.irr(x) if (x[1:] > 0).any() else np.nan
    return dict(scen=scen, fin=fin, capex=capex, rev1=rev[0], opex1=opex[0], ebitda1=ebitda[0], merchant=merchant,
                dscr_target=dscr_t, debt=debt, gear=debt / capex, proj_irr=irr(proj), eq_irr=irr(eq),
                eq_npv=npf.npv(p['hurdle'], eq), min_dscr=np.nanmin(dscr) if debt > 0 else np.nan, pmt=pmt)

if __name__ == '__main__':
    for s in 'ABC':
        for fin in ('commercial', 'ifi'):
            o = run(s, fin)
            print(f"{s} {fin:10s} rev1 {o['rev1']/1e6:5.2f} ebitda1 {o['ebitda1']/1e6:5.2f} merch {o['merchant']:.0%} "
                  f"dscrT {o['dscr_target']:.2f} debt {o['debt']/1e6:5.2f} gear {o['gear']:.0%} projIRR {o['proj_irr']:.1%} "
                  f"eqIRR {o['eq_irr']:.1%} eqNPV15 {o['eq_npv']/1e6:6.2f} minDSCR {o['min_dscr']:.2f}")
