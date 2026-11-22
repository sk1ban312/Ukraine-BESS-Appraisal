"""Parse Market Operator monthly price_DAM_IDM_MM.YYYY.xls files into one tidy hourly CSV.
Handles clock-change days: 23-hour spring day (blank last hour) and 25-hour autumn day (extra column)."""
import sys, glob, calendar, re
import xlrd
import pandas as pd

folder, out_csv = sys.argv[1], sys.argv[2]
rows, notes = [], []
for path in sorted(glob.glob(folder + "/price_DAM_IDM_*.xls")):
    month, year = map(int, re.search(r"_(\d{2})\.(\d{4})\.xls$", path).groups())
    wb = xlrd.open_workbook(path, ignore_workbook_corruption=True)
    sheets = {}
    for sh_name, key in [("Ціна_РДН", "dam"), ("Ціна_ВДР", "idm")]:
        sh = wb.sheet_by_name(sh_name)
        nh = sum(1 for x in sh.row_values(1)[1:] if x != "")
        sheets[key] = {int(v[0]): v[1:1 + nh] for v in (sh.row_values(r) for r in range(3, sh.nrows))
                       if isinstance(v[0], float)}
    ndays = calendar.monthrange(year, month)[1]
    assert set(sheets["dam"]) == set(range(1, ndays + 1)) == set(sheets["idm"]), f"day gap in {path}"
    for d in range(1, ndays + 1):
        dam_vals, idm_vals = sheets["dam"][d], sheets["idm"][d]
        n_dam = sum(1 for x in dam_vals if x != "")
        n_idm = sum(1 for x in idm_vals if x != "")
        assert n_dam == n_idm, f"DAM/IDM hour count mismatch {year}-{month}-{d}"
        if n_dam != 24:
            notes.append(f"{year}-{month:02d}-{d:02d}: {n_dam}-hour day")
        for h, (dv, iv) in enumerate(zip(dam_vals, idm_vals), start=1):
            if dv == "" and iv == "":
                continue
            assert dv != "" and iv != "", f"one-sided blank {year}-{month}-{d} h{h}"
            rows.append({"date": f"{year}-{month:02d}-{d:02d}", "hour": h,
                         "hours_in_day": n_dam, "dam_uah_mwh": dv, "idm_uah_mwh": iv})
df = pd.DataFrame(rows)
df.to_csv(out_csv, index=False)
print("\n".join(notes))
print(f"rows={len(df)} days={df.date.nunique()} first={df.date.min()} last={df.date.max()}")
print(f"DAM range {df.dam_uah_mwh.min():.2f}..{df.dam_uah_mwh.max():.2f} | IDM range {df.idm_uah_mwh.min():.2f}..{df.idm_uah_mwh.max():.2f}")
