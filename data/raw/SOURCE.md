# Source: hourly electricity prices, Ukraine

- **Publisher:** Market Operator of Ukraine — https://www.oree.com.ua
- **Data:** hourly day-ahead market (DAM) and intraday market (IDM) prices, UAH/MWh
- **Period:** 1 Jan 2025 – 31 Oct 2026 (22 monthly files, `price_DAM_IDM_MM.YYYY.xls`)
- **Format:** sheets `Ціна_РДН` (DAM) and `Ціна_ВДР` (IDM); rows = days, columns = hours 1–24
  (hour 25 on autumn clock-change days)
- **Downloaded:** 2026-11-05
- Files are unmodified originals.

## Checks
- 669 days, no missing hours.
- Clock-change days: 2025-03-30 and 2026-03-29 have 23 hours; 2025-10-26 and 2026-10-25 have 25 hours.
- Monthly average DAM prices match Market Operator's published BASE indices
  (e.g. May 2026: 5,068.72 UAH/MWh).
