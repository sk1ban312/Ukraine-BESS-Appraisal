# Technical Basis — Ukraine Grid-Scale Battery Storage

**Document 02** · **Stage:** Phase 1 (BESS) · **Fixed:** 2026-11-21 · **Revised:** 2026-11-22 (connection fee rule, calendar, itemized market-price case)
**Currency:** USD. NREL items in 2024 prices; Ukrainian items in 2026 prices, converted at the
NBU official rate of 20 Nov 2026: 45.05 UAH/USD, 49.53 UAH/EUR [11].

## Summary
| Item | Value |
|---|---|
| Asset | 20 MW / 40 MWh LFP battery (2-hour), Kyiv oblast, DSO connection at 35 kV |
| CAPEX | **USD 19.73 million** (USD 493/kWh; USD 986/kW) — base case, NREL |
| CAPEX, market-price case | USD 11.57 million (USD 289/kWh), itemized, see D.5 |
| OPEX | **USD 1.32 million per year** (6.7% of CAPEX) |
| Efficiency · life · availability | 85% round trip · 15 years · 97% |
| Operating scenarios for revenue analysis (03) | A: arbitrage only · B: aFRR only · C: 10 MW aFRR + 10 MW arbitrage |
| Calendar | Construction in 2027 (~8 months, DTEK precedent) = year 0; commercial operation from 1 Jan 2028 |
| E&S risk (World Bank ESF) | Moderate (expected), see J |

The Concept Note's indicative CAPEX (≈ USD 17 million) is replaced by USD 19.73 million:
physical protection and the grid connection fee (withdrawal plus release capacity) are added;
US sales tax is removed.

## A. Project description
| Item | Base case | Basis |
|---|---|---|
| Technology | LFP (lithium iron phosphate) battery in containers; reference product Fluence Gridstack | Used in DTEK's 200 MW / 400 MWh portfolio in Ukraine [4][5] |
| Size | 20 MW / 40 MWh usable (2-hour) | DTEK's six sites are 20–50 MW, 2-hour [4] |
| Site | Kyiv oblast, rural area of Obukhiv or Fastiv district (south of Kyiv): lowest connection fee for storage and outside the areas occupied in 2022 | See D.1 and J [6][30][34] |
| Grid connection | DSO: DTEK Kyiv Regional Electric Networks, 35 kV (voltage class 1) | [6][22] |
| Main equipment | Battery containers (cells, racks, BMS, thermal management, fire suppression); bi-directional inverters (PCS); MV transformers; 35 kV switchgear; SCADA/EMS; commercial metering | NREL bottom-up model [1]; metering rules [26] |

**Why 35 kV.** Current at full power:

$$I = \frac{P}{\sqrt{3}\,V} = \frac{20 \times 10^{6}\ \text{W}}{\sqrt{3} \times 35 \times 10^{3}\ \text{V}} \approx 330\ \text{A}$$

At 20 kV the current would be ≈ 577 A. 35 kV also keeps the project in distribution
class 1: UAH 621.52/MWh, against UAH 2,175.33/MWh for class 2 at the same DSO [22].

20 MW in both directions is at the upper end for 35 kV. The project therefore assumes its own
cell on the 35 kV busbar of a 110/35 kV substation, not a tap on an existing feeder (engineering
judgement, to be confirmed in the DSO's technical conditions). A dedicated cell also keeps the
battery off the feeders that are switched off under outage schedules. The DSO may instead
require 110 kV (see K).

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
| 1 | Battery system and balance of plant: NREL overnight capital cost | Energy 241 USD/kWh × 40,000 kWh = 9.64; power 372 USD/kW × 20,000 kW = 7.44 [1] | 17.08 | 86.6% |
| 2 | Less: US sales tax included in item 1 | 17 of 334 USD/kWh (5.1%) in NREL's breakdown, see D.2 [1] | −0.87 | −4.4% |
| 3 | Ukrainian import duty and VAT | Exempt or recoverable, see D.3 | 0.00 | 0.0% |
| 4 | DSO connection fee: withdrawal plus release capacity | UAH 3.053 thousand/kW × 20,000 kW = UAH 61.06 million, see table below [6][30] | 1.36 | 6.9% |
| 5 | Physical protection (level-2 proxy) | UAH 24.32 billion / ~250 objects ≈ UAH 97.3 million per object [12] | 2.16 | 10.9% |
| | **Total CAPEX** | | **19.73** | **100%** |
| | Per kWh / per kW | | 493 / 986 USD | |

$$\text{CAPEX}_{NREL} = 241\ \tfrac{\text{USD}}{\text{kWh}} \times 40{,}000\ \text{kWh} + 372\ \tfrac{\text{USD}}{\text{kW}} \times 20{,}000\ \text{kW} = \text{USD}\ 17.08\ \text{million}$$

- **Contingency:** NREL includes about 2.1% (≈ USD 0.36 million) inside item 1 [1]. Cost overruns
  are tested with the CAPEX stress tests in 04, not with a separate contingency line.
- **Connection fee:** since 1 Sep 2026 a storage facility pays the rate for withdrawal capacity
  (charging) plus the rate for release capacity (discharging) [30]. The old rule, the average of
  the two rates, applies only to storage commissioned before 1 Jan 2027 [31], so not to this
  project. Withdrawal uses NEURC's rates for installations that consume electricity; release uses
  the rates for installations that produce it [6][30].
- **Physical protection:** by late 2025 practically all energy facilities had level-2 protection [12].
  Check: one transformer shelter costs UAH 120–130 million excl. VAT (≈ USD 2.7–2.9 million) [13].
  Stress test from the Concept Note: CAPEX × 2.

**Connection rates for storage, 2026** — DTEK Kyiv Regional Electric Networks, 35 kV, rural area,
reliability category III, UAH thousand per kW [6]:

| District (DSO unit) | Release (production rate) | Withdrawal (consumption rate) | Sum = rate for storage |
|---|---|---|---|
| Obukhiv, Fastiv and most other districts | 1.231–1.448 | 1.605–1.822 | **3.053** |
| Borodianka, Yahotyn | 0.763 | 2.326–2.330 | 3.089–3.093 |
| Kyiv-Sviatoshynskyi, Vasylkiv | 0.763 | 2.448–2.581 | 3.211–3.344 |
| Boryspil | 0.763 | 2.824 | 3.587 |
| Irpin | 0.763 | 3.053 | 3.816 |

In most districts the two rates add up to the same UAH 3.053 thousand/kW. The six suburban
districts with the lowest release rate (cheap for generators where load is high) are 1–25% more
expensive for storage, so the site is placed outside them, in Obukhiv or Fastiv district (see J
for the second reason). Which table is release and which is withdrawal was read from the PDF's
flattened text and follows the logic of locational rates; the sum, which is what storage pays,
does not depend on it. Rates for 2027 are not yet published; NEURC sets them every year.

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
  the on-site substation, design and permitting [1, Table 3]. NREL's substation steps medium
  voltage up to high voltage; at 35 kV the project does not need that step, so this part of
  NREL's cost is probably an overestimate (not quantified, see risk 12).
- **Not included, added separately:** network upgrades, which NREL excludes ("Cost of
  interconnection upgrades are not included") [1]. In Ukraine this is the DSO connection fee
  (item 4). Physical protection (item 5) is also added.
- **Land:** not in the cost. NREL assumes a land lease [1, Table 3], so land goes to OPEX.
- **US-specific items:** sales tax is removed (item 2). NREL prices also reflect US tariffs on
  Chinese cells and a US manufacturing tax credit [1, Table 3]. The cross-check in D.4 shows that
  our estimate sits above the Ukrainian benchmarks.

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
| **This study, excluding physical protection** | | **439** |
| **This study, including physical protection** | | **493** |
| KSE bachelor thesis (Hunko, 2026) | Assumed CAPEX [15] | 148 |

Before protection, our estimate is 15–20% above both Ukrainian benchmarks. Part of the gap is
expected: one 20 MW site has less scale than DTEK's 200 MW portfolio, NREL reflects US costs, and
the scope of the benchmark figures (connection, protection, development) is not published.
The thesis assumption is 3 times lower and is not used.

### D.5 Market-price case (sensitivity)
NREL reflects US costs in 2024. A purchase for Ukraine in 2027 is closer to the export prices of
Chinese suppliers, which fell sharply in 2025. The case is built item by item, like D.1.

**Why a single benchmark is not used.** BNEF's turnkey price (Europe 2025: USD 177/kWh [36])
covers only the battery containers (DC block), the inverter (PCS) and the energy management
system (EMS). It excludes installation and construction (EPC: engineering, procurement and
construction) and grid connection [38]. The first version of this case treated it as the whole
system and so left out installation (see revision log).

| # | Item | Basis | USD million |
|---|---|---|---|
| 1 | Battery containers (DC block): cells, racks, BMS, cooling, fire suppression | Free-on-board price in China of 2-hour DC-side systems for Europe, mid-2026: USD 71–89/kWh [37]; middle value 80 × 40,000 kWh | 3.20 |
| 2 | Freight and insurance to site | 5% of item 1 ⚠️ assumption | 0.16 |
| 3 | Inverter (PCS) and EMS | About 10% of the USD 75/kWh core equipment of a 4-hour system [39] → USD 30/kW × 20,000 kW | 0.60 |
| 4 | EPC: transformers, switchgear, cables, civil works, installation, commissioning | USD 50/kWh for 4-hour projects outside China and the US (tenders in Saudi Arabia, Italy, India) [39], converted to 2 hours below | 3.37 |
| 5 | Development, owner's costs and contingency | 10% of items 1–4 ⚠️ assumption | 0.73 |
| 6 | DSO connection fee | As in D.1 | 1.36 |
| 7 | Physical protection | As in D.1 | 2.16 |
| 8 | Import duty and VAT | As in D.3 | 0.00 |
| | **Total CAPEX, market case** | | **11.57 (289 USD/kWh)** |

**EPC for 2 hours.** Ember's figure is per kWh of a 4-hour project. In NREL's cost, everything
except battery cabinets and inverter is 31 USD/kWh (241 − 210) plus 268 USD/kW (372 − 4 × 26),
i.e. 98 USD/kWh at 4 hours. EPC is assumed to split the same way:

$$EPC = 50 \times \frac{31 \times 40{,}000 + 268 \times 20{,}000}{98} \approx \text{USD}\ 3.37\ \text{million}$$

**Range and cross-check** (all-in CAPEX, USD/kWh):

| Estimate | USD/kWh |
|---|---|
| Market case, DC block at 71–89 | 279–300 |
| Market DC block (items 1–2), all other items at NREL's US cost | 358–377 |
| DTEK–Fluence, Ukraine 2025 (D.4) | 365 |
| NREL base case (D.1) | 493 |

The market case rests on installation prices from very large tenders where land is provided.
Ember notes that equipment can cost USD 100/kWh or more where tariffs are higher or standards
stricter, and that smaller projects may not get comparable quotes [39]. For one 20 MW site the
market case is therefore the optimistic end; the only Ukrainian benchmark (DTEK) sits next to the
variant with NREL installation costs. China's export tax rebate on batteries falls from 13% to 6%
and reaches zero in January 2027, which raises prices somewhat [37].

In this case O&M is 4% of items 1–5 (USD 0.32 million per year) and insurance is 2% of CAPEX
(USD 0.23 million); total OPEX is USD 0.80 million per year.

**Status:** sensitivity case. The base case stays NREL, following the Concept Note principle of
the conservative choice when sources disagree. The financial analysis (04) reports both cases and
the break-even price; the final CAPEX must be confirmed by EPC bids.

## E. Operating cost (OPEX)
| Item | Basis | USD million per year |
|---|---|---|
| O&M including augmentation | 4% × NREL CAPEX of USD 17.08 million [1][2] | 0.68 |
| War and political-risk insurance | 2% × CAPEX of USD 19.73 million. MIGA and DFC charge about 2%; market benchmark 1–3% per year [17] | 0.39 |
| Network charges on net losses | 2,499 MWh × UAH 1,643.69/MWh, see E.1 | 0.09 |
| Other: land lease, security, market fees, guarantees, administration | ⚠️ Estimate, not sourced | 0.15 |
| **Total** | | **1.32** |

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
| **Indicative calendar** | Development and connection agreement: H1 2027 · construction: H2 2027 · commercial operation: 1 Jan 2028 | Assumption |
| **Model convention** | Year 0 = 2027: construction, 100% of CAPEX. Years 1–15 = 2028–2042: operation | Assumption |

Why the date matters:
- equipment must be imported before 1 Jan 2029 to keep the tax exemption [7]; the calendar
  leaves about one year of buffer;
- a start after 1 Jan 2027 means the new connection-fee rule applies (D.1) [31];
- hourly prices of 2025–2026 are used as a proxy for 2028 onwards (tested in 03).

## H. End of life
Decommissioning cost is assumed equal to salvage value, so the net value in year 15 is zero.
⚠️ Assumption.

## I. Technical risks and open items
| # | Item | Effect | Treatment |
|---|---|---|---|
| 1 | aFRR contracts pay in certain hours only | Revenue of scenarios B and C | Hours defined in 03 |
| 2 | No new long-term aFRR auction announced | Contracted revenue may be unavailable | Concept Note risk; scenario A is the fallback |
| 3 | Reliability category (II or III), DSO hosting capacity, 2027 connection rates | Connection fee and timing | Confirm through the DSO's technical conditions |
| 4 | O&M basis (2-hour or 4-hour cost) | +USD 0.39 million per year | Stress test in 04 |
| 5 | "Other" OPEX not sourced | ±USD 0.15 million per year | Stress × 2 in 04 |
| 6 | Physical protection cost | Base +USD 2.16 million | CAPEX × 2 stress (Concept Note) |
| 7 | Import exemption ends 1 Jan 2029 | ≈ USD 1.9 million of VAT tied up | Schedule |
| 8 | Insurance availability and terms | OPEX | Sensitivity in 04 |
| 9 | aFRR duration assumption (1 hour) | Size of scenarios B and C | Confirm with Ukrenergo |
| 10 | NREL 2024 prices not escalated | About ±5% | NREL projects a real decline of ≈ 2.5% per year to 2035 [1], roughly offsetting US inflation over 2024–2026 |
| 11 | Flexible connection: non-guaranteed capacity is paid at 30% of the rate, but the DSO's automation may limit charging or discharging [30] | Lower connection fee, curtailment risk | Not in the base case; option to test in 04 |
| 12 | NREL includes an MV-to-HV substation that a 35 kV connection does not need; a 20 MW site has less scale than NREL's 60 MW reference | The first lowers CAPEX, the second raises it; neither is quantified | CAPEX ±20% sensitivity in 04 |
| 13 | Communication and cyber security of the AGC link and remote control | Availability for aFRR | Redundant channels; cyber requirements in the supply contract |
| 14 | Physical protection against fire safety | Barriers can block cooling and fire-fighting access | Protection designed together with the fire safety design |
| 15 | aFRR cycling in scenarios B and C may exceed 1 cycle per day | Warranty and degradation | Checked in 03 |

## J. Environmental and social (E&S) screening
Expected classification under the World Bank Environmental and Social Framework (ESF):
**Moderate**. Precedent: the Bank's battery storage project for Ukrhydroenergo (P176114), where
the environmental, social and overall risks are all rated Moderate [32].

| Risk | ESF standard | Measure in this project | Basis |
|---|---|---|---|
| Fire (thermal runaway of battery cells) | ESS4 Community health and safety | Containers with built-in fire suppression (in CAPEX item 1); spacing between containers and distance to homes under fire regulations; emergency plan with the State Emergency Service; extra protection if close to homes | [1][32] |
| Oil leaks from transformers | ESS3 Resource efficiency and pollution prevention | Oil containment under MV transformers | [32] |
| Noise (cooling, inverters, construction) | ESS3, ESS4 | Rural site with distance to homes | [32] |
| Worker safety, including air-raid alerts | ESS2 Labour and working conditions | Labour management plan; shelter access during air-raid alerts | [32] |
| Unexploded ordnance (UXO) | ESS4 | Site outside the areas occupied in 2022 (communities in Vyshhorod, Bucha and Brovary districts [34]); UXO survey before construction | [34] |
| Land | ESS5 Land acquisition and land use | Leased land, no resettlement; agricultural land may need re-zoning; leases of up to 49 years are common | [23][32] |
| Environmental impact assessment (EIA, ОВД) | ESS1 Assessment of E&S risks | Screening needed: utility-scale storage may trigger an EIA depending on scale and location; an EIA then covers hazardous materials, fire safety and waste [23]. Study costs are inside NREL's soft costs [1] | [1][23] |
| End-of-life batteries | ESS3 | Ukraine is drafting a law aligned with the EU Battery Regulation, including extended producer responsibility [33]; battery take-back to be written into the supply contract. ⚠️ Net-zero end-of-life value (H) remains an assumption | [33] |
| Community | ESS10 Stakeholder engagement | Consultation with the local community before the land lease and permits | [32] |

## K. Alternatives considered
| Alternative | Decision | Reason | Basis |
|---|---|---|---|
| 1-hour battery (20 MW / 20 MWh) | Rejected | Cannot hold symmetric aFRR at full power for 1 hour: 2 × 20 MW × 1 h = 40 MWh | Section C |
| 4-hour battery (20 MW / 80 MWh) | Not tested in Phase 1 | CAPEX 56% higher (NREL formula: USD 26.72 million against 17.08 million); longer evening peaks may add arbitrage revenue | [1] |
| 110 kV connection | Alternative; the DSO decides in its technical conditions | Connection fee about half: UAH 1.438 against 3.053 thousand/kW, i.e. USD 0.64 million against 1.36 million [6]. Needs a 110 kV substation: NREL's cost already includes one, but for 20 MW it costs more per kW than in NREL's 60 MW reference. 35 kV stays the base case | [1][6] |
| Other battery chemistry (e.g. NMC) | Rejected | NREL's reference system and cost data are for LFP | [1] |
| FCR instead of aFRR | Rejected | Ukrenergo's FCR need (99 MW) is fully contracted for 5 years from October 2025 | [35] |
| Suburban districts (Boryspil, Irpin and others) | Rejected | Connection fee for storage 1–25% higher | Section D.1 |
| Brovary or Vyshhorod district | Rejected | Parts were occupied in 2022 (UXO risk) | [34] |
| Gas-engine CHP; hybrid BESS + CHP | Later phases | Phases 2 and 3 of the Concept Note | Concept Note |
| No project | Counterfactual | Used in the economic analysis (05) | — |

## Revision log
| Date | Change |
|---|---|
| 2026-11-21 | First version |
| 2026-11-21 | Connection fee corrected to NEURC Res. No. 1356 (withdrawal plus release, in force from 1 Sep 2026): USD 0.34 million → 1.36 million; CAPEX USD 18.71 million → 19.73 million. Site moved out of six suburban districts. Indicative calendar added |
| 2026-11-21 | Sections J (E&S screening) and K (alternatives considered) added; site narrowed to Obukhiv or Fastiv district |
| 2026-11-21 | Engineering review: release and withdrawal labels corrected (sum unchanged); 110 kV kept as an alternative with about half the fee; dedicated 35 kV cell assumed; risks 12–15 added |
| 2026-11-21 | Market-price case (D.5) added as a sensitivity after the financial analysis showed the NREL case fails; base case unchanged |
| 2026-11-22 | D.5 rebuilt item by item. BNEF's turnkey price excludes installation (EPC) and grid connection, which the first version missed. Market case USD 11.77 million (294/kWh) → 11.57 million (289/kWh); cross-check with NREL installation costs: 358–377/kWh |

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
30. NEURC Resolution No. 1356 of Aug 11, 2026 — changes to the connection-fee methodology (withdrawal plus release; flexible connection): https://www.nerc.gov.ua/storage/app/uploads/public/6a7/c20/faa/6a7c20faa1604634270814.pdf
31. Forbes Ukraine — new grid connection rules from Sep 1, 2026 (transitional rule for storage): https://forbes.ua/news/v-ukraini-sprostili-pravila-priednannya-do-elektromerezh-shcho-zminilos-01092026-41632
32. World Bank — Concept Environmental and Social Review Summary, Improving Power System Resilience for European Power Grid Integration (P176114): https://documents1.worldbank.org/curated/en/382411616808322035/text/Concept-Environmental-and-Social-Review-Summary-ESRS-Improving-Power-System-Resilience-for-European-Power-Grid-Integration-P176114.txt
33. Ministry of Economy of Ukraine — harmonisation with the EU Battery Regulation, draft law on batteries and waste batteries, Sep 18, 2026: https://me.gov.ua/News/Detail/ad05e765-24b4-4ad5-a6fd-ae0969232c7b
34. Ukrinform — anniversary of Kyiv region's liberation: 15 communities in Vyshhorod, Bucha and Brovary districts were occupied, Apr 2, 2023: https://www.ukrinform.net/rubric-ato/3690552-anniversary-of-kyiv-regions-liberation-15-communities-used-to-be-under-russian-occupation.html
35. Interfax-Ukraine — FCR auction: 99 MW on 5-year contracts: https://interfax.com.ua/news/economic/1014424.html
36. Energy-Storage.news — BNEF and Ember: battery storage system prices continue to fall sharply, Dec 16, 2025: https://www.energy-storage.news/battery-storage-system-prices-continue-to-fall-sharply-bnef-and-ember-reports-find/
37. ESS News — Chinese export tax rebate cuts to raise European BESS costs, Jun 18, 2026: https://www.ess-news.com/2026/06/18/chinese-export-tax-rebate-cuts-to-raise-european-bess-costs/
38. Energy-Storage.news — Behind the numbers: BNEF finds 40% year-on-year drop in BESS costs (turnkey = DC block, PCS and EMS, excluding EPC and grid connection): https://www.energy-storage.news/behind-the-numbers-bnef-finds-40-year-on-year-drop-in-bess-costs
39. Ember — How cheap is battery storage? All-in BESS capex of USD 125/kWh as of October 2025: https://ember-energy.org/latest-insights/how-cheap-is-battery-storage/
