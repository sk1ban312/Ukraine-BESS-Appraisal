"""Day-ahead market (DAM) arbitrage revenue of a 20 MW / 40 MWh battery in Ukraine, 2025-2026.

One value per day, in UAH:
  ceiling    - perfect foresight, as in sheet A_Ceiling: charge in the 2 cheapest hours and discharge
               in the 2 most expensive hours of the day; no trade if the margin is negative.
  realistic  - as in sheet A_Realistic: the charge and discharge hours are chosen from the average
               price profile of the previous 28 full (24-hour) days, with charge hours before
               discharge hours, and then applied to the actual prices of the day. The day's own
               prices are not used, and the battery trades even if the margin turns out negative.
               On the first day of data and on clock-change days (no comparable profile) the
               perfect-foresight value with charge-before-discharge is used.

Revenue of a day:  R = E * (mean(P_discharge) - mean(P_charge) / RTE)

Usage:  python arb_strategies.py data/processed/dam_idm_hourly_2025_2026.csv daily_arbitrage.csv
"""
import sys

import numpy as np
import pandas as pd

E_MWH, RTE, AVAIL, FX = 40.0, 0.85, 0.97, 45.05   # see docs/technical-basis.md
LOOKBACK_DAYS = 28
PERIODS = [("Period 1", "2025-01-01", "2025-12-31"), ("Period 2", "2025-11-01", "2026-10-31")]


def revenue(p, charge, discharge):
    return E_MWH * (p[discharge].mean() - p[charge].mean() / RTE)


def best_hours(p):
    """Best 2 charge hours placed before the best 2 discharge hours, for the price vector p."""
    best = (-np.inf, None, None)
    for split in range(2, len(p) - 1):
        charge = np.argsort(p[:split], kind="stable")[:2]
        discharge = split + np.argsort(p[split:], kind="stable")[-2:]
        if len(discharge) < 2:
            continue
        r = revenue(p, charge, discharge)
        if r > best[0]:
            best = (r, charge, discharge)
    return best


def main(csv_in, csv_out):
    df = pd.read_csv(csv_in, parse_dates=["date"])
    days = sorted(df["date"].unique())
    prices = {pd.Timestamp(d): g.sort_values("hour")["dam_uah_mwh"].to_numpy() for d, g in df.groupby("date")}

    rows = []
    for i, d in enumerate(days):
        d = pd.Timestamp(d)
        p = prices[d]
        ceiling = max(0.0, E_MWH * (np.sort(p)[-2:].mean() - np.sort(p)[:2].mean() / RTE))
        history = [prices[pd.Timestamp(x)] for x in days[max(0, i - LOOKBACK_DAYS):i]
                   if len(prices[pd.Timestamp(x)]) == 24]
        if history and len(p) == 24:
            _, charge, discharge = best_hours(np.mean(history, axis=0))
            realistic, note = revenue(p, charge, discharge), ""
        else:
            realistic, charge, discharge = best_hours(p)
            realistic, note = max(0.0, realistic), "no profile: ceiling used"
        rows.append({"date": d.date(), "ceiling_uah": ceiling, "realistic_uah": realistic,
                     "charge_hours": ",".join(str(h + 1) for h in sorted(charge)),
                     "discharge_hours": ",".join(str(h + 1) for h in sorted(discharge)), "note": note})

    out = pd.DataFrame(rows).set_index("date")
    out.to_csv(csv_out)
    out.index = pd.to_datetime(out.index)
    for name, start, end in PERIODS:
        x = out.loc[start:end]
        ceil_usd = x["ceiling_uah"].sum() * AVAIL / FX
        real_usd = x["realistic_uah"].sum() * AVAIL / FX
        print(f"{name}: {len(x)} days | ceiling USD {ceil_usd:,.0f} | realistic USD {real_usd:,.0f} | "
              f"capture {real_usd / ceil_usd:.1%} | negative days {int((x['realistic_uah'] < 0).sum())}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
