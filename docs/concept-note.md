# Concept Note — Ukraine Grid-Scale Battery Storage

**Stage:** Phase 1 (BESS) · **Criteria fixed:** 2026-11-17, before any revenue or financial calculation (DSCR threshold pending)

## 1. Context
- Russian attacks on generation and grid assets cause scheduled outages across
  Ukraine — in October 2025, up to three outage queues, with some areas without
  power up to 11 hours a day [1].
- Ukrenergo, the transmission system operator, buys fast frequency reserves through
  special auctions: 99 MW of FCR on 5-year contracts and 500 MW of aFRR (August 2024),
  plus 249 MW of aFRR in May 2025 for delivery from December 2026 [2][3][4].
- Storage is scaling fast: 2.9 GWh installed in 2025 (including portable systems) and
  1.6–1.9 GWh in H1 2026 [5]. Largest example: DTEK's 200 MW / 400 MWh portfolio
  of six sites [6].
- The World Bank Group and EBRD launched RAMP UP, targeting ~1,000 MW of new
  renewable and battery capacity and ~€1.5 billion of private investment [7].
- Prior work: a 2026 KSE bachelor thesis models a 20 MW / 80 MWh BESS in Ukraine
  (IRR ≈ 45%), assuming CAPEX ≈ $148/kWh and two cycles per day [14].

## 2. Question
Is a grid-scale battery (BESS) in Ukraine worth building, and does adding gas-engine
cogeneration (CHP) create value beyond what each delivers alone — for an investor
and for Ukraine?

| Phase | Scope | Status |
|---|---|---|
| 1 | BESS alone — technical, financial and economic analysis | In progress (target 2026-11-20) |
| 2 | CHP alone | Planned |
| 3 | Hybrid BESS + CHP — synergy test | Planned |

## 3. Phase 1 base case
| Item | Base case | Basis |
|---|---|---|
| Asset | 20 MW / 40 MWh LFP battery (2-hour) | Size of DTEK's sites: 20–50 MW, 2-hour [6] |
| Location | Kyiv oblast, district near Kyiv | Load centre; lowest connection rates in the oblast [8] |
| Grid connection | DSO (DTEK Kyiv Regional Electric Networks), 35 kV | [8] |
| Revenue | 1) aFRR reserves for Ukrenergo — contracted; 2) day-ahead arbitrage — merchant | [2][3][4] |
| Indicative CAPEX | ≈ $17 million, to be confirmed in 02 | NREL 2025 cost projections [9]; cross-checked with DTEK's reported investment [6] |

## 4. Approach (World Bank appraisal structure)
| # | Document | Content |
|---|---|---|
| 01 | Concept note | Question, scope, decision criteria (this file) |
| 02 | Technical basis | Design, CAPEX, OPEX, grid connection, protection, operating parameters |
| 03 | Revenue analysis | Arbitrage on hourly DAM prices + reserve revenue |
| 04 | Financial analysis | 15-year cash flow: NPV, equity IRR, DSCR; commercial vs IFI-supported financing |
| 05 | Economic analysis | ENPV/EIRR for Ukraine vs a no-project counterfactual |
| 06 | Appraisal memo | Decision, risks, recommendations |

Principles: public data only · every number traced to a source · criteria fixed
before analysis, changes logged · conservative choice when sources disagree ·
financial and economic views kept separate.

## 5. Decision criteria (fixed before analysis)

**A. Financial — would a private investor build it?**
| Metric | Threshold | Basis |
|---|---|---|
| Equity IRR (after tax, USD) | ≥ 15% | Target return of foreign investors in Ukraine [10]; European BESS investors mostly target 11–12% [11] |

Tested under two financing structures: (1) commercial debt; (2) IFI-supported —
IFC/EBRD debt, RAMP UP risk mitigation, MIGA political-risk insurance.

**B. Bankability — would a lender finance it?**
| Metric | Threshold | Basis |
|---|---|---|
| Merchant (uncontracted) revenue share | ≤ 60% | Lenders surveyed mostly accept up to 41–60% [11] |
| DSCR | Reported; threshold to be sourced before 04 | — |

**C. Economic — is it worth it for Ukraine?**
| Metric | Threshold | Basis |
|---|---|---|
| ENPV | ≥ 0 at 6%; sensitivity at 3% and 10% | World Bank benchmark 6%; 2–10% range recommended; higher rates may apply after conflict [12] |

**D. Decision matrix**
| | ENPV ≥ 0 | ENPV < 0 |
|---|---|---|
| Equity IRR ≥ 15% with commercial debt | **Go** — private sector can build it alone | Private project; no case for IFI support |
| ≥ 15% only with IFI support | **Go with IFI support** (additionality) | No-go |
| < 15% even with IFI support | No-go | No-go |

**E. Robustness**
- The decision is tested on both price periods (Jan–Dec 2025; Nov 2025–Oct 2026);
  the worse result counts.
- Red flag: if the best 30 days give more than 50% of annual revenue → priority stress test.
- Stress tests reported: spread compression from new storage; protection level 2
  (CAPEX × 2); price-cap changes.

## 6. Key risks (initial)
- **Revenue:** FCR need fully contracted for 5 years from October 2025 [2]; regulator-set
  price caps; spreads may compress as storage grows [5].
- **Reserve contracts:** remaining aFRR need ≈ 400 MW (estimate from Ukrenergo auction
  results [3][4]); no new long-term auction announced — without one, revenue is fully merchant.
- **War:** physical damage; insurance limited to MIGA/DFC-type cover.
- **Regulatory:** storage licence above 5 MW; non-standard connection takes 120–350 days [13].
- **Currency:** CAPEX in USD/EUR; DAM revenue in UAH; reserve contracts indexed to EUR.

## 7. Decision log
| Date | Decision |
|---|---|
| 2026-11-03 | Idea: World Bank–style appraisal of energy storage in Ukraine |
| 2026-11-05 | Hourly DAM/IDM prices (Jan 2025 – Oct 2026) collected; validated against Market Operator's monthly BASE indices |
| 2026-11-06 | Repository created; first screening criteria (payback-based) |
| 2026-11-06 | Revenue focus revised: Ukrainian BESS earn mainly from Ukrenergo reserve contracts, not arbitrage alone |
| 2026-11-10 | Site set: Kyiv oblast, DSO connection at 35 kV |
| 2026-11-16 | Raw price data committed |
| 2026-11-16 | Scope: Phase 1 = BESS; CHP and hybrid moved to later phases |
| 2026-11-16 | Criteria redefined: payback screen replaced by equity IRR, merchant share and ENPV with sourced thresholds |
| 2026-11-17 | Concept note committed; criteria frozen before any revenue or financial calculation |

## Sources
1. Komersant — outage schedules, Oct 2025: https://komersant.ua/en/ukrenerho-opryliudnylo-hrafiky-vidkliuchen-na-24-zhovtnia-hodyn-zi-svitlom-bude-bilshe
2. Interfax-Ukraine — FCR auction, 99 MW, 5 years: https://interfax.com.ua/news/economic/1014424.html
3. Mind.ua — aFRR auction, 500 MW, Aug 2024: https://mind.ua/news/amp/20277978-ukrenergo-provela-chergovij-aukcion-iz-zakupivli-rezerviv-rezultati-ta-plani-na-majbutne
4. Interfax-Ukraine — 4th aFRR auction, May 2025: https://interfax.com.ua/news/economic/1075561.html
5. ESS News — Ukraine storage additions, H1 2026: https://www.ess-news.com/2026/09/28/ukraine-adds-between-1-6-1-9-gwh-of-energy-storage-in-h1-2026/
6. Fluence — DTEK 200 MW / 400 MWh: https://ir.fluenceenergy.com/news-releases/news-release-details/dtek-selects-fluence-deliver-200-mw-advanced-energy-storage
7. World Bank — RAMP UP, Jun 29, 2026: https://www.worldbank.org/en/news/press-release/2026/06/29/new-world-bank-group-support-will-help-mobilize-investment-for-ukraine-recovery
8. NEURC Resolution No. 2231 — 2026 connection rates: https://www.nerc.gov.ua/storage/app/uploads/public/695/509/cec/695509cecf950239464870.pdf
9. NREL — Cost Projections for Utility-Scale Battery Storage, 2025: https://docs.nrel.gov/docs/fy25osti/93281.pdf
10. Energynomics — target returns in Ukraine (Integrites, 2025): https://www.energynomics.ro/en/ukraine-investors-have-to-spend-almost-4-more-due-to-risk/
11. ESS News — DLA Piper survey of storage investors and lenders, Jun 2026: https://www.ess-news.com/2026/06/22/storage-lenders-cap-merchant-exposure-at-60-finds-dla-piper/
12. World Bank — Discounting Costs and Benefits in Economic Analysis (2016): https://documents1.worldbank.org/curated/en/099610503022315638/pdf/IDU02e978a2a023f704c140bb1b082595e67e593.pdf
13. AmCham Ukraine — Legal and regulatory guide for RE and storage, Jul 2026: https://chamber.ua/wp-content/uploads/2026/07/Guide-on-Legal-and-Regulatory-Framework-for-Renewable-Energy-and-Energy-Storage-Projects-in-Ukraine.pdf
14. Hunko, M. (2026). Resilient Energy Infrastructure in Wartime (KSE BA thesis): https://kse.ua/wp-content/uploads/2026/07/diploma-main-doc-hunko.pdf
