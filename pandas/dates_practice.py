import pandas as pd

dates = pd.Series(["2026-01-15", "2026-02-20", "2026-03-10", "2026-04-18"])
dates = pd.to_datetime(dates)

print(dates.dt.year)
print(dates.dt.day)
print(dates.dt.month)
print(dates.dt.day_name())