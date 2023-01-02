from datetime import date, timedelta
from zipfile import ZipFile as zf
import platform
import requests
import mysql.connector as mcon
import shutil
from io import BytesIO

# setup sql connection
# db = mcon.connect(host='localhost', user='root',
#                   passwd='root', database='nse-data')
# sql_cursor = db.cursor()

# user variables
start_date = date(2022, 12, 1)
end_date = date.today()

# function variables (don't change)
if platform.system() == 'Windows':
    download_path = ".\\daily_bhav_test"
elif platform.system() == 'Linux':
    download_path = ".//daily_bhav_test"
months = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN',
          7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}
start_year = int(start_date.strftime("%Y"))
end_year = int(end_date.strftime("%Y"))
start_month = months[int(start_date.strftime("%m"))]
end_month = months[int(end_date.strftime("%m"))]


def daterange():
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


for single_date in daterange():
    year = single_date.strftime("%Y")
    month = months[int(single_date.strftime("%m"))]
    day = single_date.strftime("%d")
    # print(year, month, day)
    url = f"https://www1.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{day}{month}{year}bhav.csv.zip"
    print(url)
    try:
        r = requests.get(url).content
        # extract the csv file from zip and save in download_path
    except Exception as E:
        print(E)
        break  # remove this once try block is complete

"""
url format: https://www1.nseindia.com/content/historical/EQUITIES/{YEAR}/{MONTH}/cm{DAY}{MONTH}{YEAR}bhav.csv.zip
example   : https://www1.nseindia.com/content/historical/EQUITIES/2022/DEC/cm20DEC2022bhav.csv.zip
example   : https://www1.nseindia.com/content/historical/EQUITIES/2022/DEC/cm02DEC2022bhav.csv.zip
"""
