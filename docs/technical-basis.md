# Technical Basis — Ukraine Grid-Scale Battery Storage

**Document 02** · **Stage:** Phase 1 (BESS) · **Fixed:** 2026-11-21
**Currency:** USD. NREL items in 2024 prices; Ukrainian items in 2026 prices, converted at the
NBU official rate of 20 Nov 2026: 45.05 UAH/USD, 49.53 UAH/EUR [11].

## Summary
| Item | Value |
|---|---|
| Asset | 20 MW / 40 MWh LFP battery (2-hour), Kyiv oblast, DSO connection at 35 kV |
| CAPEX | **USD 18.71 million** (USD 468/kWh; USD 935/kW) |
| OPEX | **USD 1.30 million per year** (6.9% of CAPEX) |
| Efficiency · life · availability | 85% round trip · 15 years · 97% |
| Operating scenarios for revenue analysis (03) | A: arbitrage only · B: aFRR only · C: 10 MW aFRR + 10 MW arbitrage |
| Construction | ~8 months from supplier selection to operation (DTEK precedent); year 0 in the model |

The Concept Note's indicative CAPEX (≈ USD 17 million) is replaced by USD 18.71 million:
physical protection and the grid connection fee are added; US sales tax is removed.

## A. Project description
| Item | Base case | Basis |
|---|---|---|
| Technology | LFP (lithium iron phosphate) battery in containers; reference product Fluence Gridstack | Used in DTEK's 200 MW / 400 MWh portfolio in Ukraine [4][5] |
| Size | 20 MW / 40 MWh usable (2-hour) | DTEK's six sites are 20–50 MW, 2-hour [4] |
| Site | Kyiv oblast, rural area of a district near Kyiv | Lowest connection rate in the oblast [6] |
| Grid connection | DSO: DTEK Kyiv Regional Electric Networks, 35 kV (voltage class 1) | [6][22] |
| Main equipment | Battery containers (cells, racks, BMS, thermal management, fire suppression); bi-directional inverters (PCS); MV transformers; 35 kV switchgear; SCADA/EMS; commercial metering | NREL bottom-up model [1]; metering rules [26] |

**Why 35 kV.** Current at full power:

$$I = \frac{P}{\sqrt{3}\,V} = \frac{20 \times 10^{6}\ \text{W}}{\sqrt{3} \times 35 \times 10^{3}\ \text{V}} \approx 330\ \text{A}$$

At 20 kV the current would be ≈ 577 A. 35 kV also keeps the project in distribution
class 1: UAH 621.52/MWh, against UAH 2,175.33/MWh for class 2 at the same DSO [22].

## B. Operating parameters
| Parameter | Value | Basis |
|---|---|---|
| Round-trip efficiency (AC–AC) | 85% | NREL 2025 [1]; ATB 2025 [2] |
| Lifetime | 15 years | NREL 2025 [1] |
| Cycling | 1 full cycle per day | NREL's O&M cost assumes about one cycle per day [1] |
| Capacity over life | Kept at rated level by augmentation, paid from O&M | [1][2] |
| Availability | 97% | DNV: Fluence fleet 98.7% (99.3% for fleets ≥ 50 MW); industry figures 95–98% [16]. We use a value inside the industry range |
| aFRR response | Change output within 15 minutes on the dispatcher's command | Ukrenergo auction rules [28][29] |
| aFRR duration | Full output held for 1 hour | ⚠️ Sizing assumption, to be confirmed against Ukrenergo requirements |

## C. Operating scenarios (input to the revenue analysis)
The same MW cannot be sold twice in the same hour, so power and energy are shared:

$$P_{aFRR} + P_{arb} \le 20\ \text{MW}, \qquad E_{aFRR} + E_{arb} \le 40\ \text{MWh}$$

Symmetric aFRR needs stored energy to deliver and empty space to absorb, each for one hour:

$$E_{aFRR} = 2 \times P_{aFRR} \times 1\ \text{h}$$

| Scenario | aFRR (symmetric) | Arbitrage | Energy used |
|---|---|---|---|
| A — arbitrage only | 0 | 20 MW × 2 h | 40 MWh |
| B — aFRR only | ≈ 18 MW | 0 | 36 MWh (10% state-of-charge margin) |
| C — split | 10 MW | 10 MW × 2 h | 20 + 20 = 40 MWh |

Long-term aFRR contracts pay the auction price in certain hours only [28]. Capacity outside
those hours may be free for arbitrage. This is modelled in 03.

## D. Capital cost (CAPEX)

### D.1 Cost estimate
| # | Item | Basis | USD million | Share |
|---|---|---|---|---|
| 1 | Battery system and balance of plant: NREL overnight capital cost | Energy 241 USD/kWh × 40,000 kWh = 9.64; power 372 USD/kW × 20,000 kW = 7.44 [1] | 17.08 | 91.3% |
| 2 | Less: US sales tax included in item 1 | 17 of 334 USD/kWh (5.1%) in NREL's breakdown, see D.2 [1] | −0.87 | −4.6% |
| 3 | Ukrainian import duty and VAT | Exempt or recoverable, see D.3 | 0.00 | 0.0% |
| 4 | DSO connection fee | UAH 0.763 thousand/kW × 20,000 kW = UAH 15.26 million [6] | 0.34 | 1.8% |
| 5 | Physical protection (level-2 proxy) | UAH 24.32 billion / ~250 objects ≈ UAH 97.3 million per object [12] | 2.16 | 11.5% |
| | **Total CAPEX** | | **18.71** | **100%** |
| | Per kWh / per kW | | 468 / 935 USD | |

$$\text{CAPEX}_{NREL} = 241\ \tfrac{\text{USD}}{\text{kWh}} \times 40{,}000\ \text{kWh} + 372\ \tfrac{\text{USD}}{\text{kW}} \times 20{,}000\ \text{kW} = \text{USD}\ 17.08\ \text{million}$$

- **Contingency:** NREL includes about 2.1% (≈ USD 0.36 million) inside item 1 [1]. Cost overruns
  are tested with the CAPEX stress tests in 04, not with a separate contingency line.
- **Connection fee:** NEURC rate for 2026 at 35 kV, rural area, reliability category III, in the
  cheapest districts near Kyiv. Rates differ up to about 4× across the oblast [6].
- **Physical protection:** by late 2025 practically all energy facilities had level-2 protection [12].
  Check: one transformer shelter costs UAH 120–130 million excl. VAT (≈ USD 2.7–2.9 million) [13].
  Stress test from the Concept Note: CAPEX × 2.

### D.2 What NREL's cost includes
NREL splits the owner's overnight capital cost into ten subcomponents [1, Sec. 2.2].
Breakdown of the 4-hour reference system (USD 334/kWh, 2024 prices):

| Subcomponent | What it covers | USD/kWh | Share |
|---|---|---|---|
| 1. Battery cabinets | Cells, modules, racks, BMS, thermal management, fire suppression | 210 | 62.9% |
| 2. Inverter | Bi-directional DC/AC conversion (PCS) | 26 | 7.8% |
| 3. Structural BOS | Site preparation, concrete pads | 5 | 1.5% |
| 4. Electrical BOS | Transformers, switchgear, cables, grounding, SCADA, substation, 2.4-mile line | 44 | 13.2% |
| 5, 6, 8, 9. Soft costs | Installation labour; permitting and interconnection studies; contingency; developer overhead (logistics, design, engineering, management) | 18 | 5.4% |
| 7. Sales tax | 5.8% of items 1–4 | 17 | 5.1% |
| 10. Profit | 5% of items 1–4 | 14 | 4.2% |
| **Total** | | **334** | **100%** |

Values are read from NREL's Fig. 1. The assignment to categories is checked by arithmetic:
total = 334; sales tax = 5.8% × 285 = 16.5; profit = 5% × 285 = 14.3.

What this means for the project:
- **Already included, not added again:** the line to the grid (NREL includes a 2.4-mile line),
  the on-site substation, design and permitting [1, Table 3].
- **Not included, added separately:** network upgrades, which NREL excludes ("Cost of
  interconnection upgrades are not included") [1]. In Ukraine this is the DSO connection fee
  (item 4). Physical protection (item 5) is also added.
- **Land:** not in the cost. NREL assumes a land lease [1, Table 3], so land goes to OPEX.
- **US-specific items:** sales tax is removed (item 2). NREL prices also reflect US tariffs on
  Chinese cells and a US manufacturing tax credit [1, Table 3]. The cross-check in D.4 shows the
  net result for Ukraine is a higher, i.e. conservative, estimate.

### D.3 Import taxes
| Equipment | Import duty | VAT | Basis |
|---|---|---|---|
| Lithium-ion batteries (UKT ZED 8507 60 00 00, incl. LFP) | 0 | 0 | Laws No. 4698-IX and No. 4710-IX: exemption until 1 Jan 2029 [7][8]. Excluded: storage below 300 W and goods from the aggressor state [8][9] |
| Inverters, transformers (EU origin) | 0 | 20%, recoverable as input VAT | EU–Ukraine DCFTA: 96% of EU exports liberalised by 2023 [10] |
| Services and other materials | — | 20%, recoverable | Standard VAT credit; timing of recovery ignored (limitation) |

Risk: if equipment is imported after 31 Dec 2028, batteries pay 20% VAT. About
USD 1.9 million would be tied up until recovered.

### D.4 Cross-check
| Benchmark | Basis | USD/kWh |
|---|---|---|
| DTEK–Fluence, 200 MW / 400 MWh (2025) | EUR 125 million (USD 146 million) invested [5] | 365 |
| National Renewable Energy Action Plan to 2030 | 656 MW of storage, USD 502 million of investment [14]; 2-hour assumed | ≈ 383 |
| **This study, excluding physical protection** | | **414** |
| **This study, including physical protection** | | **468** |
| KSE bachelor thesis (Hunko, 2026) | Assumed CAPEX [15] | 148 |

Before protection, our estimate is 8–13% above both Ukrainian benchmarks, so it is conservative.
The thesis assumption is 2.8 times lower and is not used.

## E. Operating cost (OPEX)
| Item | Basis | USD million per year |
|---|---|---|
| O&M including augmentation | 4% × NREL CAPEX of USD 17.08 million [1][2] | 0.68 |
| War and political-risk insurance | 2% × CAPEX of USD 18.71 million. MIGA and DFC charge about 2%; market benchmark 1–3% per year [17] | 0.37 |
| Network charges on net losses | 2,499 MWh × UAH 1,643.69/MWh, see E.1 | 0.09 |
| Other: land lease, security, market fees, guarantees, administration | ⚠️ Estimate, not sourced | 0.15 |
| **Total** | | **1.30** |

- **O&M:** NREL's 2024 edition used 2.5% [3]; the 2025 edition raised it to 4% [1][2]. We use
  4% because CAPEX comes from the same edition. If NREL's 4% is read as 4% of a 4-hour battery's
  cost (USD 1,336/kW), O&M would be USD 1.07 million per year. This is a stress test in 04.
- **Insurance:** cover is limited. MIGA's minimum is USD 5 million; DFC's term is 3 years [17].

### E.1 Network charges
Under the energy storage law (No. 2046-IX, 2022) and NEURC's 2022 amendments to the
transmission and distribution codes, a storage operator pays transmission, dispatch and
distribution charges on the absolute difference between monthly withdrawal and monthly
release. That is, it pays on losses, not on all charging energy [18][19][20].

$$E_{loss} = \left(\frac{40}{0.85} - 40\right)\ \frac{\text{MWh}}{\text{day}} \times 365 \times 0.97 \approx 2{,}499\ \frac{\text{MWh}}{\text{year}}$$

| Charge | UAH/MWh | Basis |
|---|---|---|
| Transmission (Ukrenergo) | 903.53 | NEURC draft from 1 Jul 2026 (current 742.90); the higher value is used [21] |
| Dispatch (Ukrenergo) | 118.64 | NEURC draft (current 110.03) [21] |
| Distribution, class 1 (DTEK Kyiv Regional) | 621.52 | From 1 May 2026 [22] |
| **Total** | **1,643.69** | |

If the charges applied to all charging energy, they would cost about USD 0.61 million per year.
The net rule saves the project about USD 0.52 million per year.

## F. Requirements for the two revenue streams
| Stream | Requirement | Cost / timing | Basis |
|---|---|---|---|
| Both | NEURC energy storage licence (required above 5 MW) | — | [23][24] |
| Both | Agreement with Ukrenergo on imbalance settlement: own balance responsible party or a balancing group | In "other" OPEX | [25, cl. 1.4.1][23] |
| Both | Separate commercial metering of storage flows | In CAPEX (electrical BOS) | [26] |
| aFRR | Win Ukrenergo's special auction. Contract of 1–5 years, price fixed in EUR, start may be deferred up to 3 years | — | NEURC Res. No. 1172 [27] |
| aFRR | Deposit of EUR 5,000 per facility; financial security of EUR 30,000/MW, returned within 30 days after the service starts | ≈ EUR 0.6 million for 20 MW, tied up during construction | [27] |
| aFRR | Ukrenergo conformity certificate; response within 15 minutes | In CAPEX (SCADA) | [27][28][29] |
| Arbitrage | Application and participation agreement with the Market Operator; registration within about 4 working days; fixed software fee | Small | [25, cl. 2.1] |
| Arbitrage | Escrow account: electricity for charging is prepaid before trading | About one day of charging, ≈ USD 5 thousand | [25, cl. 2.2.5] |

Long-term aFRR auctions: four have been held (August and December 2024, May 2025). The last one
covers delivery from 1 Dec 2026 to 30 Nov 2031 [28]. No new auction has been announced (see
Concept Note, key risks).

## G. Implementation schedule
| Phase | Duration | Basis |
|---|---|---|
| Development: land, technical conditions, design, permits, licence | Before the investment decision; cost inside NREL soft costs | [1] |
| Grid connection (non-standard) | 120–350 days | [23] |
| Supplier selection → commercial operation | ~8 months (DTEK: January → September 2025) | [5] |
| Construction | ~6 months (DTEK: March → August 2025) | [5] |
| aFRR auction → service start | ~1.5 years (4th auction) | [28] |
| **Model convention** | Year 0: construction, 100% of CAPEX. Years 1–15: operation | Assumption |

Equipment must be imported before 1 Jan 2029 to keep the tax exemption [7].

## H. End of life
Decommissioning cost is assumed equal to salvage value, so the net value in year 15 is zero.
⚠️ Assumption.

## I. Technical risks and open items
| # | Item | Effect | Treatment |
|---|---|---|---|
| 1 | aFRR contracts pay in certain hours only | Revenue of scenarios B and C | Hours defined in 03 |
| 2 | No new long-term aFRR auction announced | Contracted revenue may be unavailable | Concept Note risk; scenario A is the fallback |
| 3 | Reliability category (II or III) and DSO hosting capacity | Connection fee and timing | Confirm through the DSO's technical conditions |
| 4 | O&M basis (2-hour or 4-hour cost) | +USD 0.39 million per year | Stress test in 04 |
| 5 | "Other" OPEX not sourced | ±USD 0.15 million per year | Stress × 2 in 04 |
| 6 | Physical protection cost | Base +USD 2.16 million | CAPEX × 2 stress (Concept Note) |
| 7 | Import exemption ends 1 Jan 2029 | ≈ USD 1.9 million of VAT tied up | Schedule |
| 8 | Insurance availability and terms | OPEX | Sensitivity in 04 |
| 9 | aFRR duration assumption (1 hour) | Size of scenarios B and C | Confirm with Ukrenergo |
| 10 | NREL 2024 prices not escalated | About ±5% | NREL projects a real decline of ≈ 2.5% per year to 2035 [1], roughly offsetting US inflation over 2024–2026 |

## Sources
1. NREL (Cole et al.) — Cost Projections for Utility-Scale Battery Storage: 2025 Update: https://docs.nrel.gov/docs/fy25osti/93281.pdf
2. NREL ATB 2025 — Utility-Scale Battery Storage: https://atb.nlr.gov/electricity/2025/utility-scale_battery_storage
3. NREL ATB 2024 — Utility-Scale Battery Storage (O&M 2.5%): https://atb.nrel.gov/electricity/2024/utility-scale_battery_storage
4. Fluence — DTEK selects Fluence for 200 MW energy storage: https://ir.fluenceenergy.com/news-releases/news-release-details/dtek-selects-fluence-deliver-200-mw-advanced-energy-storage
5. Energy-Storage.news — DTEK and Fluence turn on 200 MW Ukraine BESS, Sep 11, 2025: https://www.energy-storage.news/storage-as-fundamental-as-generation-dtek-and-fluence-turn-on-200mw-ukraine-bess/
6. NEURC Resolution No. 2231 — 2026 connection rates: https://www.nerc.gov.ua/storage/app/uploads/public/695/509/cec/695509cecf950239464870.pdf
7. Forbes Ukraine — import benefits for energy equipment extended to 2029, Jan 29, 2026: https://forbes.ua/news/podatkovi-pilgi-na-vvezennya-energetichnogo-obladnannya-prodovzhili-do-2029-roku-29012026-35902
8. Buhplatforma — Laws No. 4698-IX and No. 4710-IX, code 8507 60 00 00: https://buhplatforma.com.ua/news/111666-pilgove-vvezennia-energoobladnannia-prodovzhyly-do-2029-roku
9. Liga:Zakon — State Customs Service on storage import exemption, Aug 1, 2024: https://jurliga.ligazakon.net/news/229523_derzhmitsluzhba-rozyasnila-yak-ustanovki-zbergannya-energ-zvlnyayutsya-vd-opodatkuvannya-pd-chas-vvezennya-v-ukranu
10. European Commission — EU–Ukraine Deep and Comprehensive Free Trade Area: https://trade.ec.europa.eu/access-to-markets/en/content/eu-ukraine-deep-and-comprehensive-free-trade-area
11. Dengi.ua — NBU official rates for Nov 20, 2026 (check against bank.gov.ua): https://dengi.ua/finance/9763624-kurs-valyut-na-20112026
12. Ekonomichna Pravda — protection of energy facilities in 2026: https://epravda.com.ua/finances/yak-v-ukrajini-zamovlyayut-zahist-elektropidstanciy-u-2026-roci-821442/
13. Telegraf — Kudrytskyi on protection of energy facilities, Nov 15, 2025: https://news.telegraf.com.ua/ukr/ukraina/2025-11-15/5925608-yaki-obekti-energetiki-otrimuyut-zakhist-vid-obstriliv-kudritskiy-poyasniv
14. Ministry of Energy of Ukraine — BESS report, Aug 2025: https://mev.gov.ua/sites/default/files/2025-08/bess-report-ukraine-v3-18.08.2025_1.pdf
15. Hunko, M. (2026). Resilient Energy Infrastructure in Wartime (KSE BA thesis): https://kse.ua/wp-content/uploads/2026/07/diploma-main-doc-hunko.pdf
16. Energy-Storage.news — DNV verifies 98.7% availability of Fluence's fleet: https://www.energy-storage.news/dnv-verifies-98-7-availability-of-fluences-global-battery-energy-storage-fleet/
17. GMK Center — who insures the Ukrainian economy against war risks, Jan 23, 2026: https://gmk.center/en/posts/business-in-a-minefield-who-insures-the-ukrainian-economy-against-missiles-and-losses-and-how/amp/
18. CEE Legal Matters — regulatory framework for energy storage in Ukraine expanded: https://ceelegalmatters.com/ukraine/19309-the-regulatory-framework-for-energy-storage-in-ukraine-has-been-expanded
19. NEURC — Transmission System Code amendments for storage, justification and text (2022): https://www.nerc.gov.ua/storage/app/uploads/public/633/1c8/11e/6331c811e1429434098499.pdf
20. NEURC — Distribution System Code amendments for storage, justification and text (2022): https://www.nerc.gov.ua/storage/app/uploads/public/635/956/775/635956775bd64598600658.pdf
21. Forbes Ukraine — Ukrenergo transmission and dispatch tariffs, May 26, 2026: https://forbes.ua/news/regulyator-skhvaliv-pidvishchennya-tarifiv-ukrenergo-na-peredachu-ta-dispetcherizatsiyu-na-22-i-8-vidpovidno-26052026-39105
22. Interfax-Ukraine — DSO distribution tariffs from May 1, 2026: https://interfax.com.ua/news/economic/1161718.html
23. AmCham Ukraine — Legal and regulatory guide for RE and storage, Jul 2026: https://chamber.ua/wp-content/uploads/2026/07/Guide-on-Legal-and-Regulatory-Framework-for-Renewable-Energy-and-Energy-Storage-Projects-in-Ukraine.pdf
24. Avellum — Law No. 4777-IX on energy markets, Mar 23, 2026: https://avellum.com/?p=14844
25. Market Operator — Day-ahead and intraday market rules (NEURC Res. No. 308): https://oree.com.ua/index.php/web/10503
26. NEURC Resolution No. 1358 of Aug 11, 2026 — Commercial Metering Code changes: https://www.nerc.gov.ua/storage/app/uploads/public/6a7/c24/bae/6a7c24bae3ecd787198845.pdf
27. Liga:Zakon — special ancillary-services auctions, key facts (NEURC Res. No. 1172), Jul 9, 2024: https://biz.ligazakon.net/analitycs/228985_zapusk-spetsalnikh-auktsonv-na-dopomzhn-poslugi-klyuchov-fakti
28. Interfax-Ukraine — 4th aFRR auction, final results, Jul 2, 2025: https://interfax.com.ua/news/general/1084652.html
29. Forbes Ukraine — Ukrenergo announces first long-term ancillary-services auctions, Aug 6, 2024: https://forbes.ua/news/ukrenergo-ogolosilo-pershi-dovgostrokovi-auktsioni-zakupivli-dopomizhnikh-poslug-06082024-22854
