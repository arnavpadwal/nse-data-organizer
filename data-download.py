import jugaad_data.nse as jd
from datetime import date
import pandas as pd

# variables
download_path = "//home//arnav//Work//VSCode//nse-data-organizer//daily_bhav"
start_date = date(2022, 12, 1)
end_date = date.today()

dates = pd.date_range(start_date, end_date)
for i in dates:
    try:
        jd.nse.bhavcopy_save(i, download_path)
    except Exception:
        continue

"""
url format: https://www1.nseindia.com/content/historical/EQUITIES/{DAY}/{MONTH}/cm{DAY}{MONTH}{YEAR}bhav.csv.zip
"""
