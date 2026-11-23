# Financial Analysis — Ukraine Grid-Scale Battery Storage

**Document 04** · **Stage:** Phase 1 (BESS) · **Fixed:** 2026-11-21 · **Revised:** 2026-11-22 (itemized market case; break-even on the market cost structure; decision read strictly from matrix D)
**Currency:** nominal USD · **Model:** `models/financial-model.xlsx` (selectors for scenario, financing and CAPEX case) · `scripts/financial_model.py`

## Summary
| CAPEX case | All-in CAPEX | Best combination | Equity IRR | Equity NPV at 15% |
|---|---|---|---|---|
| NREL (base, conservative) | USD 19.73 million · 493 USD/kWh | C, commercial debt | 1.3% | −USD 10.3 million |
| Market DC block + NREL installation costs (≈ DTEK benchmark) | USD 14.69 million · 367 USD/kWh | C, IFI-supported debt | 9.4% | −USD 2.2 million |
| Market, itemized (installation at large-tender prices) | USD 11.57 million · 289 USD/kWh | C, IFI-supported debt | **22.8%** | **+USD 1.8 million** |

- **NREL case:** none of the six combinations reaches the 15% equity IRR (range −2.7% to 1.3%).
  Three of them do not even return the money invested within 15 years.
- **Market case, itemized:** four combinations pass: C with IFI-supported debt (22.8%), B with
  IFI-supported debt (21.2%), C with commercial debt (15.6%) and B with commercial debt (15.1%).
- **Cheap equipment alone is not enough:** with the market battery price but NREL's US
  installation costs, the best equity IRR is 9.4%.
- **Break-even:** all-in CAPEX of at most **USD 324/kWh** (scenario C, IFI-supported), i.e. an
  installed system price (EPC bid, without connection fee and protection) of at most
  **USD 237/kWh**. The itemized market case is 11% below it; the DTEK benchmark is 13% above it.
- **Additionality:** in the market case IFI-supported debt (longer tenor) lifts the equity IRR of
  scenario C from 15.6% to 22.8%. In the NREL case debt destroys value (negative leverage):
  the project earns about 1.5% a year, less than the loan costs.
- **Decision (Concept Note, matrix D), by the all-in CAPEX that EPC bids confirm (scenario C):**
  up to USD 294/kWh — Go, commercial debt is enough (the itemized market case, 289, is just
  inside); 294–324 — Go with IFI support; above 324 — No-go. NREL case — No-go. The economic
  test is in document 05.

## 1. Method
- Nominal USD. Year 0 = 2027: construction, 100% of CAPEX. Years 1–15 = 2028–2042: operation.
- Revenue from document 03 (worse price period). Arbitrage revenue escalates with inflation;
  aFRR revenue stays flat because its price is fixed in EUR.
- OPEX from document 02, escalating with inflation except insurance (a share of CAPEX).
- Tax: 18% of profit after straight-line depreciation over 15 years; losses carried forward.
- Debt is sized by the lender: the largest loan whose equal annual payment keeps the DSCR at the
  target in the weakest year, capped at 70% of CAPEX:

$$D = \min\left(0.70 \times CAPEX,\ \ PV\left(r,\ T,\ \frac{\min_t CFADS_t}{DSCR^{*}}\right)\right), \qquad DSCR^{*} = 1.20\,(1-m) + 2.0\,m$$

  where *m* is the merchant share of revenue, *r* the loan rate and *T* the tenor.
- Equity IRR is the rate that makes the equity cash flows sum to zero; equity NPV discounts them
  at the 15% hurdle:

$$NPV = \sum_{t=0}^{15} \frac{CF_t}{(1+0.15)^{t}}$$

## 2. Assumptions
| Input | Value | Source |
|---|---|---|
| CAPEX, NREL case | USD 19.73 million | Technical basis, D.1 |
| CAPEX, market case | USD 11.57 million, itemized | Technical basis, D.5 |
| OPEX, year 1 | USD 1.32 million (NREL) · USD 0.80 million (market) | Technical basis, E and D.5 |
| Revenue, year 1 | A 2.43 · B 2.83 · C 2.78 (USD million) | Revenue analysis, 6 |
| Inflation | 2.5% per year | NREL ATB 2024, financial cases [1] |
| Corporate income tax | 18% | PwC Worldwide Tax Summaries, Ukraine [2] |
| Tax depreciation | 15 years, straight line (book life above the 5-year minimum for machinery) | Tax Code 138.3.3 via Buhplatforma [3] |
| Equity hurdle | 15% after tax, USD | Concept Note, criterion A |
| DSCR target | 1.20 contracted · 2.0 merchant, weighted by revenue share | Fitch via ESMAP/IFC [4]; NREL ATB 2024 [1] |
| Maximum debt share | 70% | IFI deals: OKKO wind 70% [5], Notus wind 70% [6], Kernel solar + storage 52% [7] |
| Commercial debt | 6.11% · 5 years | NBU: new USD loans to companies, Jan 2026; loans over 5 years ≈ 13% of the portfolio [8] |
| IFI-supported debt | 7.0% · 10 years ⚠️ tenor is an assumption | NREL ATB 2024: term debt for battery storage [1] |
| End-of-life value | 0 | Technical basis, H |

## 3. Results, NREL case (base)
| Scenario · financing | Debt / CAPEX | Project IRR | Equity IRR | Equity NPV at 15% | Min DSCR |
|---|---|---|---|---|---|
| A · commercial | 12% | 0.6% | 0.5% | −USD 11.7 million | 2.00 |
| A · IFI | 20% | 0.6% | −0.2% | −USD 11.0 million | 2.00 |
| B · commercial | 25% | 0.0% | −0.6% | −USD 10.6 million | 1.21 |
| B · IFI | 38% | 0.0% | −2.7% | −USD 9.5 million | 1.20 |
| C · commercial | 20% | 1.5% | 1.3% | −USD 10.3 million | 1.58 |
| C · IFI | 33% | 1.5% | 0.2% | −USD 9.1 million | 1.58 |

How large the loss is over 15 years (cash to equity, not discounted):

| Scenario · financing | Equity invested | Cash returned | Net | Payback |
|---|---|---|---|---|
| A · commercial | 17.4 | 18.2 | +0.8 | 14.5 years |
| A · IFI | 15.8 | 15.5 | −0.3 | never |
| B · commercial | 14.9 | 14.1 | −0.8 | never |
| B · IFI | 12.3 | 9.3 | −3.0 | never |
| C · commercial | 15.8 | 17.8 | +2.0 | 13.7 years |
| C · IFI | 13.2 | 13.5 | +0.3 | 14.8 years |

(USD million.) IFI-supported debt makes the net result worse here: the project earns about 1.5% a
year, while the loan costs 7%.

## 4. Results, market case (itemized)
| Scenario · financing | Debt / CAPEX | Project IRR | Equity IRR | Equity NPV at 15% | Min DSCR |
|---|---|---|---|---|---|
| A · commercial | 27% | 11.9% | 12.8% | −USD 1.1 million | 2.05 |
| A · IFI | 45% | 11.9% | 14.8% | −USD 0.1 million | 2.09 |
| B · commercial | 53% | 12.5% | **15.1%** | +USD 0.0 million | 1.21 |
| B · IFI | 70% | 12.5% | **21.2%** | **+USD 1.3 million** | 1.48 |
| C · commercial | 41% | 13.5% | **15.6%** | +USD 0.3 million | 1.60 |
| C · IFI | 69% | 13.5% | **22.8%** | **+USD 1.8 million** | 1.64 |

Variant with the market DC block but all other items at NREL's US cost (CAPEX USD 14.69 million,
367 USD/kWh, close to DTEK's 365): C · IFI 9.4%, C · commercial 8.5%, B · IFI 7.8%. It fails.

## 5. Stress tests (scenario C, IFI-supported debt)
| Test | Equity IRR, NREL case | Equity IRR, market case |
|---|---|---|
| Base | 0.2% | 22.8% |
| CAPEX × 2 (Concept Note) | −21.7% | −2.2% |
| Arbitrage revenue −20% (spread compression) | −2.9% | 16.1% |
| aFRR paid 12 hours a day instead of 24 | −8.0% | 6.5% |
| Availability 90% | −2.0% | 17.1% |
| Other OPEX × 2 | −1.6% | 18.2% |
| No inflation | −0.4% | 21.4% |
| O&M at 4% of a 4-hour battery cost | −4.7% | — |
| DC block at 71 / 89 USD/kWh (CAPEX 279 / 300 USD/kWh) | — | 25.3% / 20.0% |
| Equipment +30% (rebound, export rebate removed; CAPEX 322 USD/kWh) | — | 15.4% |
| Installation and other items at NREL's US cost (CAPEX 367 USD/kWh) | — | 9.4% |

The market case survives weaker spreads, lower availability, higher OPEX and a 30% rise in
equipment prices. It fails if aFRR is paid only half the day, if installation costs reach NREL's
level or if CAPEX doubles.

## 6. Break-even price
Price at which the equity IRR is exactly 15%, on the market cost structure (O&M at 4% of the
system price; connection fee and protection fixed at USD 88/kWh). USD per kWh, all-in CAPEX /
EPC bid (installed system price without connection fee and protection):

| Scenario | Commercial debt | IFI-supported debt |
|---|---|---|
| A | 268 / 180 | 288 / 200 |
| B | 290 / 202 | 322 / 234 |
| C | 294 / 207 | **324 / 237** |

For comparison, all-in (EPC part): itemized market case 289 (202); market DC block with NREL
installation 367 (279); DTEK–Fluence 2025 ≈ 365; NREL case 493.

## 7. Check against the Concept Note criteria
| Criterion | NREL case | Market case |
|---|---|---|
| A. Equity IRR ≥ 15% | Fails in all combinations | Itemized: C · IFI 22.8%, B · IFI 21.2%, C · commercial 15.6%, B · commercial 15.1%. With NREL installation costs: fails (best 9.4%) |
| B. Merchant share ≤ 60% | A fails (100%); B (0%) and C (44%) pass | Same |
| B. DSCR | Debt sized to the target (1.20–2.0) | Same |
| D. Decision matrix | No-go | By all-in CAPEX: ≤ 294 Go (commercial debt); 294–324 Go with IFI support; > 324 No-go. Itemized case (289): Go, with a margin of 0.6 points. ENPV in document 05 |
| E. Robustness | Worse price period used; red flag not triggered (document 03) | Fragile: fails with aFRR at 12 hours, installation at NREL cost or CAPEX × 2 |

## 8. Limitations
- No interest during construction, no debt service reserve account, no dividend withholding tax,
  no VAT timing.
- aFRR revenue assumes a new long-term auction and 24 paid hours a day (upper bound).
- Assumptions: the IFI-supported loan tenor (10 years); in the market case, freight (5%), owner's
  costs (10%) and the conversion of 4-hour tender EPC prices to 2 hours with NREL's cost split.
- Revenue from intraday trading, balancing and FCR is not included (upside).

## Sources
1. NREL ATB 2024 — Financial Cases and Methods: https://atb.nrel.gov/electricity/2024/financial_cases_&_methods
2. PwC Worldwide Tax Summaries — Ukraine, taxes on corporate income (reviewed 30 Jun 2026): https://taxsummaries.pwc.com/ukraine/corporate/taxes-on-corporate-income
3. Buhplatforma — minimum useful lives for tax depreciation, May 30, 2024: https://buhplatforma.com.ua/news/891-yakimi-e-stroki-amortizatsii-osnovnikh-zasobiv-u-podatkovomu-obliku
4. ESMAP / IFC — Renewable Energy Project Finance, Fitch Ratings (2012), slide 13: https://esmap.org/sites/esmap.org/files/ESMAP_IFC_RE_Training_World_Bank_Fitch.pdf
5. EBRD — EUR 157 million finance package for private Ukraine wind farms (2025): https://www.ebrd.com/home/news-and-events/news/2025/-157-million-finance-package-for-private-ukraine-wind-farms--.html
6. Forbes Ukraine — Notus Energy: EUR 65 million EBRD loan, Apr 3, 2026: https://forbes.ua/news/nimetska-notus-energy-zaluchae-65-mln-kreditu-vid-ebrr-na-budivnitstvo-ves-na-odeshchini-03042026-37708
7. Kyiv Post — Kernel: USD 45 million EBRD loan, Apr 24, 2026: https://www.kyivpost.com/post/74686
8. NBU — Monetary and Financial Statistics, January 2026, Tables 9 and 12: https://bank.gov.ua/admin_uploads/article/MFS_2026-01.pdf
9. Technical basis (02): `docs/technical-basis.md` (market-case sources: D.5, [36]–[39]) · Revenue analysis (03): `docs/revenue-analysis.md` · Concept note (01): `docs/concept-note.md`
