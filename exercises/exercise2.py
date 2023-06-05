import pandas as pd
from sqlalchemy import create_engine, types

df = pd.read_csv('https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV', sep=';',
                 decimal=',')
df.drop(['Status'], inplace=True, axis=1)
df = df.dropna(how='any')

# print(df.columns)
# print(df.dtypes)

valid_verkehr_cols = ["FV", "RV", "nur DPN"]
df = df[df.Verkehr.isin(valid_verkehr_cols)]
# print(df.Betreiber_Nr.unique())

df = df[df.Laenge.between(-90, 90)]
df = df[df.Breite.between(-90, 90)]

pattern = "[A-Za-z]{2}:\d+:\d+(?::\d+)?$"

df = df[df.IFOPT.str.match(pattern)]

engine = create_engine('sqlite:///trainstops.sqlite')

dtypes = {'EVA_NR': types.INTEGER,
          'DS100': types.TEXT,
          'IFOPT': types.TEXT,
          'NAME': types.TEXT,
          'Verkehr': types.TEXT,
          'Laenge': types.FLOAT,
          'Breite': types.FLOAT,
          'Betreiber_Name': types.TEXT,
          'Betreiber_Nr': types.FLOAT
          }
df.to_sql('trainstops', engine, if_exists='replace', index=False, dtype=dtypes)

engine.dispose()