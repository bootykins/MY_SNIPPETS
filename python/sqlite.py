import sqlite3
from sqlalchemy import create_engine
import csv
import pandas as pd
import requests
import json

#df = pd.read_csv('auto.csv')
#print(df)

#endpoint = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange?filter=record_date:eq:2023-12-31'

#resp = requests.request('get',url=endpoint).json()

#print(resp)


con = sqlite3.connect(':memory:')
# or sqlalchemy
#engine = create_engine(url='sqlite://', echo=False)
print(type(con))

sql = 'create table test (date date, desc varchar, termed bool)'

output = con.execute(sql).fetchone()
print(output)

