"""Economic analysis of the 20 MW / 40 MWh BESS (document 05): ENPV and EIRR for Ukraine.

Constant (real) USD, years 0..15, same conventions as the financial model (04):
  benefits  = arbitrage (DAM price spread as the value of shifting energy, constant real)
            + aFRR availability payment (auction price as the value of reserve; fixed in EUR, so it
              falls 2.5% a year in real terms, as in 04)
            + avoided CO2, valued at the World Bank shadow price of carbon
  costs     = CAPEX + O&M + insurance (proxy for expected war damage) + other OPEX
  excluded  = corporate tax, loans and interest, network charges (transfers inside Ukraine)

CO2: on "surplus days" (both charge hours in daytime AND average charging price below
UAH 1,000/MWh, i.e. far below the fuel cost of thermal plants) the charging energy is taken as
zero-carbon and the evening discharge displaces thermal output. On all other days both ends are
thermal and only the losses count (negative). Upper-bound variant: every daytime-charging day.

Usage:  python economic_model.py daily_arbitrage.csv hourly_prices.csv
        daily_arbitrage.csv = output of scripts/arb_strategies.py;
        hourly_prices.csv   = data/processed/dam_idm_hourly_2025_2026.csv
"""
import sys
import numpy as np
import numpy_financial as npf
import pandas as pd
from scipy.optimize import brentq
from financial_model import BASE, FX, market_system

CONN, PROT = 3.053e3 * 20000 / FX, 24.32e9 / 250 / FX
EF = 0.525          # tCO2/MWh: IFI harmonised grid factor, Ukraine, combined margin, firm energy (v2.0, 2019)
RTE, AV, G = 0.85, 0.97, 0.025
SOLAR_HOURS = range(10, 18)   # charge-hour labels 10..17 (09:00-17:00)
SURPLUS_PRICE = 1000          # UAH/MWh, average price of the two charge hours (assumption)
P1 = ('2025-01-01', '2025-12-31')   # Period 1, the worse price period


def day_counts(daily_csv, hourly_csv, strict=True):
    """(zero-carbon charging days, other days) in Period 1."""
    d = pd.read_csv(daily_csv, parse_dates=['date']).set_index('date').loc[P1[0]:P1[1]]
    h = pd.read_csv(hourly_csv, parse_dates=['date'])
    prices = {k: g.sort_values('hour')['dam_uah_mwh'].to_numpy() for k, g in h.groupby('date')}
    hrs = d['charge_hours'].astype(str).str.split(',').apply(lambda x: [int(i) for i in x])
    day = hrs.apply(lambda x: all(i in SOLAR_HOURS for i in x))
    cheap = pd.Series([prices[k][[i - 1 for i in x]].mean() < SURPLUS_PRICE for k, x in hrs.items()], index=d.index)
    zero = day & cheap if strict else day
    return int(zero.sum()), int((~zero).sum())


def spc(year, level):
    """World Bank / HLCCP shadow price of carbon: 40-80 USD/t in 2020, 50-100 in 2030, +2.25% a year."""
    return (40 if level == 'low' else 80) * 1.0225 ** (year - 2020)


def capex_fom(case):
    if case == 'nrel':
        return BASE['capex'], 0.04 * BASE['nrel']
    s = market_system({**BASE, 'mkt_variant': 'nrel_bos' if case == 'hybrid' else 'tender'})
    return s + CONN + PROT, 0.04 * s


def flows(scen, case, days, co2='low', mult=1.0, arb_mult=1.0, afrr_mult=1.0):
    capex, fom = capex_fom(case)
    capex, fom = (capex - CONN - PROT) * mult + CONN + PROT, fom * mult
    t = np.arange(1, 16); defl = (1 + G) ** (t - 1)
    arb = {'A': BASE['arb'], 'B': 0.0, 'C': BASE['arb_c']}[scen] * arb_mult
    afrr = {'A': 0.0, 'B': BASE['afrr_b'], 'C': BASE['afrr_c']}[scen] * afrr_mult / defl
    e = {'A': 40, 'B': 0, 'C': 20}[scen]                       # MWh discharged per day for arbitrage
    tco2 = EF * AV * (days[0] * e - days[1] * e * (1 / RTE - 1))
    co2v = 0.0 if co2 is None else tco2 * np.array([spc(2027 + k, co2) for k in t])
    opex = fom + BASE['other'] + 0.02 * capex / defl
    return np.concatenate([[-capex], arb + afrr + co2v - opex]), tco2


def summary(f):
    return {r: npf.npv(r, f) / 1e6 for r in (0.03, 0.06, 0.10)}, npf.irr(f)


if __name__ == '__main__':
    days = day_counts(sys.argv[1], sys.argv[2])
    days_up = day_counts(sys.argv[1], sys.argv[2], strict=False)
    print(f'Period 1: {days[0]} surplus days, {days[1]} other days (upper bound: {days_up[0]} daytime-charging days)')
    for case in ('nrel', 'hybrid', 'market'):
        for s in 'ABC':
            f, tco2 = flows(s, case, days)
            npv, irr = summary(f)
            print(f"{case:6s} {s}: CAPEX {capex_fom(case)[0]/4e4:.0f}/kWh | tCO2/yr {tco2:,.0f} | ENPV 3% {npv[0.03]:+.1f} "
                  f"6% {npv[0.06]:+.1f} 10% {npv[0.10]:+.1f} | EIRR {irr:.1%}")
    print('Sensitivity, scenario C, ENPV at 6% (USD million) / EIRR:')
    tests = [('Base', {}), ('No CO2 value', dict(co2=None)), ('High carbon price', dict(co2='high')),
             ('CO2: every daytime-charging day', dict(days=days_up)),
             ('Arbitrage benefit -20%', dict(arb_mult=0.8)), ('aFRR value for 12 hours a day', dict(afrr_mult=0.5)),
             ('CAPEX x 2 (Concept Note)', dict(mult=None))]
    for lab, kw in tests:
        row = []
        for case in ('nrel', 'hybrid', 'market'):
            if kw.get('mult', 1.0) is None:
                cx = capex_fom(case)[0]; m = (2 * cx - CONN - PROT) / (cx - CONN - PROT)
                f, _ = flows('C', case, days, mult=m)
            else:
                kw2 = dict(kw); dd = kw2.pop('days', days)
                f, _ = flows('C', case, dd, **kw2)
            npv, irr = summary(f); row.append(f'{npv[0.06]:+5.1f} / {irr:5.1%}')
        print(f'  {lab:32s} NREL {row[0]} | hybrid {row[1]} | market {row[2]}')
    for s in 'ABC':
        m = brentq(lambda m: npf.npv(0.06, flows(s, 'market', days, mult=m)[0]), 0.2, 5)
        f, _ = flows(s, 'market', days, mult=m)
        print(f'Switching value {s}: ENPV(6%) = 0 at all-in CAPEX {-f[0]/4e4:.0f} USD/kWh')
