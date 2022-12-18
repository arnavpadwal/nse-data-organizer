from nsetools import Nse as ns
from datetime import date, timedelta
import requests
import io
import zipfile
import jugaad_data.nse
import time
import pandas as pd

# variables
download_path = "//home//arnav//Work//VSCode//nse-data-organizer//daily_bhav"
start_date = date(2022, 12, 1)
end_date = date.today()
holidays = []

dates = pd.date_range(start_date, end_date)
for i in dates:
    try:
        jugaad_data.nse.bhavcopy_save(i, download_path)
    except Exception:
        continue


# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)


# for single_date in daterange(start_date, end_date):
#     try:
#         jugaad_data.nse.bhavcopy_save(single_date, download_path)
#     except Exception:
#         holidays.append(str(single_date))
#         continue


"""
url format: https://www1.nseindia.com/content/historical/EQUITIES/{DAY}/{MONTH}/cm{DAY}{MONTH}{YEAR}bhav.csv.zip
"""
