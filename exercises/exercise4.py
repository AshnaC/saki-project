import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import create_engine, types

zip_url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
zip_path = 'data.zip'
urllib.request.urlretrieve(zip_url, zip_path)

extract_path = 'files'
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

csv_path = 'files/data.csv'
columns_to_read = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C",
                   "Geraet aktiv"]
df = pd.read_csv(csv_path, sep=';', decimal=',', usecols=columns_to_read, index_col=False, header=0)
new_column_names = {'Temperatur in °C (DWD)': 'Temperatur', 'Batterietemperatur in °C': 'Batterietemperatur'}

df = df.rename(columns=new_column_names)

# print(df)
def convert_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


df["Temperatur"] = df["Temperatur"].apply(convert_to_fahrenheit)
df["Batterietemperatur"] = df["Batterietemperatur"].apply(convert_to_fahrenheit)


engine = create_engine('sqlite:///temperatures.sqlite')

dtypes = {'Geraet': types.INTEGER,
          'Hersteller': types.TEXT,
          'Model': types.TEXT,
          'Monat': types.INTEGER,
          'Temperatur': types.FLOAT,
          'Batterietemperatur': types.FLOAT,
          'Geraet aktiv': types.TEXT,
          }
df.to_sql('temperatures', engine, if_exists='replace', index=False, dtype=dtypes)

engine.dispose()
