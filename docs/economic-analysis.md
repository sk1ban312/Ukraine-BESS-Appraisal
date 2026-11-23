# Economic Analysis — Ukraine Grid-Scale Battery Storage

**Document 05** · **Stage:** Phase 1 (BESS) · **Fixed:** 2026-11-22
**Currency:** constant (real) USD · **Model:** `models/economic-analysis.xlsx` (selectors for CAPEX case and scenario) · `scripts/economic_model.py`

## Summary
| CAPEX case (scenario C) | All-in CAPEX | ENPV at 6% | EIRR | Criterion C: ENPV ≥ 0 |
|---|---|---|---|---|
| NREL (base, conservative) | 493 USD/kWh | −USD 5.7 million | 1.0% | Fails |
| Market DC block + NREL installation (≈ DTEK benchmark) | 367 USD/kWh | +USD 2.5 million | 8.6% | Passes at 3% and 6%, fails at 10% |
| Market, itemized | 289 USD/kWh | +USD 7.3 million | 15.1% | Passes at all three rates |

- **Switching value:** ENPV at 6% is zero at an all-in CAPEX of **USD 407/kWh** (scenario C).
- **Main finding:** at a realistic cost (≈ DTEK) the battery is worth it for Ukraine, but not for a
  private investor: equity IRR 9.4% against the 15% hurdle (document 04). Matrix D gives No-go.
  The gap between the economic and the financial result is the main point for the memo (06).
- **Fragile:** at realistic cost ENPV turns negative if aFRR is valued for 12 hours a day
  (−USD 4.1 million) or at a 10% discount rate (−USD 1.1 million), and it is close to zero if
  arbitrage value falls by 20% (+USD 0.1 million).
- **CO₂:** the avoided emissions are small (770 t a year in scenario C); no conclusion depends on them.

## 1. Method
- Perspective: Ukraine as a whole against a no-project counterfactual, in which the same evening
  peak is met by the marginal supplier (thermal plants or imports) and the same reserve by the
  next-best provider. The battery is small against the system, so it does not change prices.
- Constant USD of year 1; years 0–15 (2027–2042); no end-of-life value (as in 04).
- Discount rate 6%, the World Bank benchmark; 3% and 10% as sensitivities (Concept Note,
  criterion C) [1]. EIRR is the rate at which ENPV = 0.

$$ENPV = \sum_{t=0}^{15} \frac{B_t - C_t}{(1+0.06)^{t}}$$

where *B* are the benefits and *C* the costs for Ukraine in year *t*.

## 2. From financial to economic flows
| Item | Financial analysis (04) | Economic analysis (05) | Reason |
|---|---|---|---|
| Arbitrage | Market revenue, rises with inflation | Same value, constant in real terms | DAM prices measure the value of energy in each hour; the battery moves energy from cheap to expensive hours |
| aFRR | Auction payment, flat in EUR | Same, falls 2.5% a year in real terms | Auction price taken as the cost of the next-best reserve provider ⚠️ assumption |
| Avoided CO₂ | — | Added at the World Bank shadow price of carbon | Section 3 |
| CAPEX | Document 04 | Same; it contains no taxes (US sales tax removed; import VAT and duty exempt) | Connection fee and protection are real costs |
| O&M, other OPEX | Document 04 | Same, constant in real terms | Real resources |
| Insurance | 2% of CAPEX | Same, as a proxy for expected war damage | Conservative |
| Network charges | Paid on net losses | Excluded | Transfer to network operators; the energy lost is already inside the arbitrage value |
| Corporate tax, loans, interest | Included | Excluded | Transfers and financing, not uses of resources |

## 3. Avoided CO₂
The battery cuts emissions only when it charges with energy that would otherwise be wasted and
discharges when thermal plants run. On all other days its losses add emissions.

$$CO_2 = EF \times A \times \left( N_{surplus} \times E \;-\; N_{other} \times E \times \left(\frac{1}{\eta} - 1\right) \right)$$

| Input | Value | Source |
|---|---|---|
| EF: emission factor of displaced thermal output | 0.525 tCO₂/MWh (Ukraine, combined margin, firm energy) | IFI Harmonized Grid Emission Factor data set v2.0, Jul 2019 [2] |
| N_surplus: zero-carbon charging days | 119 a year: both charge hours between 09:00 and 17:00 and average charging price below UAH 1,000/MWh ⚠️ threshold is an assumption | Period 1 prices (document 03) |
| N_other: days when only losses count | 246 a year | Same |
| E: energy discharged for arbitrage | A 40 · B 0 · C 20 MWh per day | Technical basis, C |
| A, η | 97% availability, 85% round-trip efficiency | Technical basis, B |
| Shadow price of carbon | Low: USD 40/t in 2020, 50 in 2030, +2.25% a year (≈ 48–65 over 2028–2042); high: twice the low value; 2017 USD | World Bank / High-Level Commission on Carbon Prices [3][4] |

Result: A 1,540 · B 0 · C 770 tCO₂ a year. Of 237 days with daytime charging, only 119 had
charging prices below UAH 1,000/MWh. Counting all 237 as zero-carbon would give 2,184 t a year in
scenario C (upper bound, section 5). Scenario B is set to zero: aFRR activation energy is assumed
net zero.

## 4. Results (USD million)
| Case · scenario | ENPV at 3% | ENPV at 6% | ENPV at 10% | EIRR |
|---|---|---|---|---|
| NREL · A | −3.7 | −6.7 | −9.6 | 0.3% |
| NREL · B | −4.8 | −7.3 | −9.8 | −1.0% |
| NREL · C | −2.6 | −5.7 | −8.6 | 1.0% |
| Market DC block + NREL installation · A | +5.2 | +1.5 | −2.1 | 7.5% |
| Market DC block + NREL installation · B | +4.1 | +0.9 | −2.2 | 7.0% |
| Market DC block + NREL installation · C | +6.3 | **+2.5** | −1.1 | 8.6% |
| Market, itemized · A | +10.5 | +6.3 | +2.4 | 13.5% |
| Market, itemized · B | +9.3 | +5.7 | +2.2 | 13.6% |
| Market, itemized · C | +11.5 | **+7.3** | +3.4 | 15.1% |

## 5. Sensitivity (scenario C, ENPV at 6%, USD million)
| Test | NREL | Market DC block + NREL installation | Market, itemized |
|---|---|---|---|
| Base | −5.7 | +2.5 | +7.3 |
| No CO₂ value | −6.1 | +2.1 | +6.9 |
| High carbon price | −5.3 | +2.9 | +7.7 |
| CO₂: every daytime-charging day zero-carbon | −4.9 | +3.2 | +8.1 |
| Arbitrage value −20% (more storage narrows spreads) | −8.1 | +0.1 | +5.0 |
| aFRR value for 12 hours a day | −12.3 | −4.1 | +0.7 |
| CAPEX × 2 (Concept Note) | −36.8 | −20.4 | −10.7 |

Switching values (all-in CAPEX at which ENPV at 6% = 0, market cost structure):
A 391 · B 381 · C **407** USD/kWh.

## 6. Decision by CAPEX (Concept Note, matrix D)
The financial break-even (04) and the economic switching value (05) split the CAPEX range into
four zones (scenario C, all-in USD/kWh):

| All-in CAPEX | Financial (04) | Economic (05) | Matrix D |
|---|---|---|---|
| ≤ 294 | Equity IRR ≥ 15% with commercial debt | ENPV > 0 | **Go**; the itemized market case (289) is just inside |
| 294–324 | ≥ 15% only with IFI support | ENPV > 0 | **Go with IFI support** |
| 324–407 | < 15% even with IFI support | ENPV > 0 | **No-go**, although worth it for Ukraine: the DTEK benchmark (≈ 365) falls here |
| > 407 | < 15% | ENPV < 0 | **No-go**; NREL case (493) |

## 7. Limitations
- aFRR value equals the auction price; the positive result at realistic cost depends on aFRR paid
  24 hours a day.
- Emission factor from a 2019 (pre-war) data set; the surplus-day threshold is an assumption;
  Ukraine's CO₂ tax inside thermal costs is not netted out (possible small double counting).
- Not counted (upside): avoided blackouts (value of lost load), capacity value, and the DAM price
  caps that understate the value of energy in scarcity hours.
- No conversion factors (shadow wage, shadow exchange rate); carbon price kept in 2017 USD
  (conservative).

## Sources
1. World Bank (2016) — Discounting Costs and Benefits in Economic Analysis of World Bank Projects: https://documents1.worldbank.org/curated/en/099610503022315638/pdf/IDU02e978a2a023f704c140bb1b082595e67e593.pdf
2. UNFCCC — IFI Harmonized Grid Emission Factor data set (v2.0, Jul 2019): https://unfccc.int/sites/default/files/resource/Harmonized_Grid_Emission_factor_data_set.pdf
3. World Bank — press release on the High-Level Commission on Carbon Prices, May 29, 2017: https://www.worldbank.org/en/news/press-release/2017/05/29/new-global-pathway-on-carbon-pricing-can-shift-finance-to-sustainable-investments-world-bank
4. E3G — Bank metrics: shadow carbon pricing (World Bank escalation of 2.25% a year): https://www.e3g.org/bank-metrics/shadow-carbon-pricing/
5. Financial analysis (04): `docs/financial-analysis.md` · Revenue analysis (03): `docs/revenue-analysis.md` · Technical basis (02): `docs/technical-basis.md` · Concept note (01): `docs/concept-note.md`
