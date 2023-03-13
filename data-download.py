from nsetools import Nse as ns
from datetime import date
import requests
import io
import zipfile
import time
import os

# import mysql.connector as mcon

# # db = mcon.connect(host='localhost', user='root',
# #                   passwd='root', database='nse_bhav')

# variables
months = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC",
}
months_days_dict = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31,
}
download_path = ".//daily_bhav"

date_from = date(2020, 1, 1)
date_to = date.today()

start_year = int(date_from.strftime("%Y"))
start_month = int(date_from.strftime("%m"))
start_day = int(date_from.strftime("%d"))

end_year = int(date_to.strftime("%Y")) + 1
end_month = int(date_to.strftime("%m")) + 1
end_day = int(date_to.strftime("%d")) + 1

# downloadings bhav files
for year in range(start_year, end_year):
    for month in range(start_month, end_month):
        for day in range(start_day, end_day):
            m = months[month]
            filename = f"cm{day}{m}{year}bhav.csv"
            file_exists = os.path.exists(os.path.join(download_path, filename))
            if file_exists == False:
                try:
                    url = f"http://www1.nseindia.com/content/historical/EQUITIES/{year}/{m}/cm{day}{m}{year}bhav.csv.zip"
                    session_obj = requests.Session()
                    r = session_obj.get(
                        url, headers={"User-Agent": "Mozilla/5.0"}, stream=True
                    )
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall(download_path)
                    # renaming files
                    if len(month) == 1:
                        nm = f"0{month}"
                    new_path = os.rename(
                        f"{download_path}//cm{day}{m}{year}bhav.csv",
                        f"{download_path}//{day}-{nm}-{year}cmbhav.csv",
                    )
                    os.rename()
                except Exception:
                    continue

# Notes
"""
url format: https://www1.nseindia.com/content/historical/EQUITIES/{YEAR}/{MONTH}/cm{DAY}{MONTH}{YEAR}bhav.csv.zip
"""
