# Revenue Analysis — Ukraine Grid-Scale Battery Storage

**Document 03** · **Stage:** Phase 1 (BESS) · **Fixed:** 2026-11-21
**Currency:** USD. UAH converted at 45.05 UAH/USD and EUR at 49.53 UAH/EUR (NBU, 20 Nov 2026).
**Model:** `models/revenue-analysis.xlsx` · daily values: `scripts/arb_strategies.py`

## Summary
| Scenario | What the battery does | Revenue, worse period (USD million per year) | Merchant share |
|---|---|---|---|
| A | Arbitrage only: 20 MW × 2 h | **2.43** | 100% |
| B | aFRR only: 18 MW symmetric | **2.83** | 0% if contracted |
| C | 10 MW aFRR + 10 MW × 2 h arbitrage | **2.78** | 44% |

- A realistic strategy, using only past prices, earns 92–93% of perfect foresight: the daily price
  shape in Ukraine is very regular (cheap at night and midday, expensive in the evening).
- Arbitrage revenue is 21% higher in Period 2 than in Period 1. The day-ahead price cap rose from
  9,000 to 15,000 UAH/MWh in August 2025, so Period 1 is the worse period and counts.
- The best 30 days give 12–14% of annual revenue, far below the 50% red flag of the Concept Note.
- Scenarios B and C need a new long-term aFRR auction. If Ukrenergo pays 12 hours a day instead
  of 24, B falls to USD 1.41 million and C to USD 2.00 million.
- Only scenario C combines both revenue streams within the lenders' 60% merchant limit
  (Concept Note, criterion B). Scenario A fails that criterion.

## 1. Data
- Hourly day-ahead (DAM) prices, Market Operator, 1 Jan 2025 – 31 Oct 2026: 669 days, 16,056 hours,
  validated against the monthly BASE indices (`data/raw/SOURCE.md`) [1].
- Two test periods, as fixed in the Concept Note: Period 1 = Jan–Dec 2025; Period 2 = Nov 2025 – Oct 2026.
- Highest hourly price observed: 9,000 UAH/MWh until July 2025, 15,000 UAH/MWh from August 2025.
  Lowest: 10 UAH/MWh from September 2025.

## 2. Method

### 2.1 Arbitrage (scenario A)
Each day the battery charges in two hours and discharges in two hours. Because of losses, selling
1 MWh needs 1 / 0.85 ≈ 1.18 MWh bought:

$$R_{day} = E \times \left(P_{discharge} - \frac{P_{charge}}{\eta}\right), \qquad E = 40\ \text{MWh},\ \eta = 0.85$$

| Strategy | Rule | Role |
|---|---|---|
| Ceiling (perfect foresight) | 2 cheapest and 2 most expensive hours of the day; no trade if the margin is negative | Upper bound |
| Realistic (base case) | Hours chosen from the average price profile of the previous 28 days, charge before discharge, then applied to the day's actual prices; trades even when the margin turns out negative | Used in the financial model |

The realistic strategy most often charges at 13:00–14:00 (solar surplus) and discharges at
21:00–22:00; in winter it charges at 04:00–05:00 and discharges at 18:00–19:00.

### 2.2 aFRR availability payment (scenarios B and C)

$$R_{aFRR} = P_{aFRR} \times p \times \frac{\text{USD}}{\text{EUR}} \times h \times 365 \times A$$

| Input | Value | Basis |
|---|---|---|
| Price p | 16.8 EUR per MW per hour (symmetric aFRR) | Average price of the 4th long-term auction (27 May 2025) after financial security: UAH 786.95 [2][3] |
| Indexation | Price fixed in EUR, paid in UAH at the monthly average NBU rate | [2][4] |
| Paid hours h | 24 per day (base, upper bound); 12 (stress) | Set by each contract; no public schedule [4][5] |
| Availability A | 97%; no payment during maintenance | Technical basis, B; [2] |
| Activation energy | Assumed net zero | Limitation |

### 2.3 Scenario C
10 MW stay in symmetric aFRR around the clock. The other 10 MW trade in the same hours as
scenario A, so their arbitrage revenue is half of scenario A. The energy check is in the
technical basis, section C.

## 3. Results (USD per year, after 97% availability)
| Item | Period 1 | Period 2 | Worse |
|---|---|---|---|
| A — arbitrage, ceiling | 2,615,463 | 3,220,809 | 2,615,463 |
| A — arbitrage, realistic | 2,430,967 | 2,949,083 | **2,430,967** |
| Capture rate (realistic / ceiling) | 92.9% | 91.6% | |
| B — aFRR, 18 MW | 2,825,083 | 2,825,083 | **2,825,083** |
| C — aFRR part, 10 MW | 1,569,490 | 1,569,490 | |
| C — arbitrage part, 10 MW | 1,215,484 | 1,474,541 | |
| C — total | 2,784,974 | 3,044,032 | **2,784,974** |
| Merchant share of C | 43.6% | 48.4% | |
| Stress: B with 12 paid hours | 1,412,541 | 1,412,541 | 1,412,541 |
| Stress: C with 12 paid hours | 2,000,229 | 2,259,287 | 2,000,229 |
| Best 30 days, share of ceiling revenue | 14.4% | 11.8% | |

## 4. Robustness (Concept Note, criterion E)
- **Two price periods:** both tested; Period 1 is worse and is carried to the financial model.
- **Red flag (best 30 days > 50% of revenue):** not triggered (14.4% and 11.8%).
- **Paid aFRR hours:** stress of 12 hours per day reported above.
- **Spread compression from new storage and price-cap changes:** tested in 04 as revenue sensitivities.

## 5. Limitations
- Intraday (IDM) and balancing-market revenue is not included (upside).
- Charging 47 MWh in two hours exceeds 20 MW (it takes about 2.35 hours), which slightly flatters arbitrage.
- Prices of 2025–2026 are used as a proxy for operation from 2028; more storage may narrow spreads.
- aFRR: paid hours are not published, activation energy is assumed net zero, and a new long-term
  auction is needed. Without one, aFRR would be sold in short-term auctions as merchant revenue.
- One exchange rate for the whole period.

## 6. Inputs to the financial model (04)
| Scenario | Revenue, year 1 (USD million) | Merchant share | Contract |
|---|---|---|---|
| A | 2.43 | 100% | None |
| B | 2.83 | 0% | aFRR, 5 years, EUR-indexed |
| C | 2.78 | 44% | aFRR for 10 MW, 5 years, EUR-indexed |

## Sources
1. Market Operator — hourly DAM prices; see `data/raw/SOURCE.md` in this repository.
2. LibMod — Unlocked Potential for Grid Stability in Ukraine (Dec 2025), Tables 2–3: https://libmodredaktion.fra1.digitaloceanspaces.com/wp-content/uploads/20260325112034/LibMod_PP_Ukr_AuctGridStability.pdf
3. Interfax-Ukraine — final results of the 4th aFRR auction, Jul 2, 2025: https://interfax.com.ua/news/general/1084652.html
4. NEURC Resolution No. 1172 of Jun 26, 2024 — special auctions for ancillary services: https://nerc.gov.ua/storage/app/uploads/public/667/d19/6fd/667d196fd62b6077612409.pdf
5. Interfax-Ukraine — four special auctions, services bought "during specified hours", Jan 2, 2026: https://en.interfax.com.ua/news/economic/1133189.html
6. Technical basis (document 02): `docs/technical-basis.md`
7. Concept note (document 01): `docs/concept-note.md`
