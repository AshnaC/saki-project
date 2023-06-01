import pandas as pd
import sqlite3
from utils import table_names
from os import listdir
from os.path import isfile, join

connection = sqlite3.connect("dataset.sqlite")

df_obj = {}



def get_files():
    file_list = [f for f in listdir('../datasets/indicators/') if isfile(join('../datasets/indicators/', f))
                 and f.endswith('.csv')]
    return file_list


def read_all_files():
    files = get_files()
    for file in files:
        field = file.replace('.csv', '')
        df_obj[field] = read_csv_file(file)


def read_csv_file(file_name):
    file_url = '../datasets/indicators/' + file_name
    return pd.read_csv(file_url, delimiter=';', decimal=',')


# read_all_files()
# print(df_obj)

indicators_additional_df = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
    'export?gid=1924564310&format=csv')

temp_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
                      'export?gid=0&format=csv')

# Household waste - kg/head
waste_df = pd.read_csv(
    '../datasets/indicators/household_waste.csv', delimiter=';')

# Green House gases  - Million tons of carbon dioxide equivalents
green_house_gases_df = pd.read_csv(
    '../datasets/indicators/greenhouse_gas.csv', delimiter=';')
green_house_gases_df.rename(
    columns={green_house_gases_df.columns[0]: "Type"}, inplace=True)
green_house_gases_df.dropna(how='all', axis=1, inplace=True)

# no2 emission - tons
no2_emission_df = pd.read_csv(
    '../datasets/indicators/nitrogen_oxide_emission.csv', delimiter=';', decimal=',')
no2_emission_df.rename(
    columns={no2_emission_df.columns[0]: "Type"}, inplace=True)

# no2 concentration -  Annual mean value in micrograms per cubic meter
no2_concentration_df = pd.read_csv(
    '../datasets/indicators/no2_concentration_urban.csv', delimiter=';', decimal=',')
no2_concentration_df.rename(
    columns={no2_concentration_df.columns[0]: "Type"}, inplace=True)
no2_concentration_df.at[0, 'Type'] = 'Nitrogen dioxide concentration'

# Particulate matter emissions - toms
particulate_matter_df = pd.read_csv('../datasets/indicators/Particulate matter emissions.csv', delimiter=';',
                                    index_col=[0]).transpose()
particulate_matter_df = particulate_matter_df.reset_index()
particulate_matter_df.rename(
    columns={particulate_matter_df.columns[0]: "Type"}, inplace=True)
particulate_matter_df.columns = particulate_matter_df.columns.astype(str)

# Ozone Concentration - Number of hourly mean values above 180 micrograms per cubic meter
ozone_concentration_df = pd.read_csv(
    '../datasets/indicators/o3-concentration-urban.csv', delimiter=';')
ozone_concentration_df.rename(
    columns={ozone_concentration_df.columns[0]: "Type"}, inplace=True)
ozone_concentration_df.at[0, 'Type'] = 'Ozone concentration'

# Recycling rate - Recycling rate in percent
recycling_df = pd.read_csv(
    '../datasets/indicators/Recycling rate.csv', delimiter=';')
recycling_df.rename(columns={recycling_df.columns[0]: "Type"}, inplace=True)

# Land Consumption - Hectare per day
consumption_df = pd.read_csv(
    '../datasets/indicators/Land consumption.csv', delimiter=';')
consumption_df.rename(
    columns={consumption_df.columns[0]: "Type"}, inplace=True)
print('Land', consumption_df.columns)
# Remove some formatting issues in columns
consumption_df.rename(lambda x: x[0:4], axis='columns', inplace=True)

# Settlement area - square meters of settlement area per head
settlement_df = pd.read_csv(
    '../datasets/indicators/Settlement area.csv', delimiter=';')
settlement_df.rename(columns={settlement_df.columns[0]: "Type"}, inplace=True)

# Heavy metal discharge at rural stations -Normalization to 1986 = 1.0
heavy_metal_df = pd.read_csv(
    '../datasets/indicators/heavy_metal_rural.csv', delimiter=';')
heavy_metal_df.rename(
    columns={heavy_metal_df.columns[0]: "Type"}, inplace=True)

#  Nitrate concentration in groundwater
# Percentage of monitoring sites with nitrate contamination above 50 milligrams per liter
nitrate_concentration_df = pd.read_csv(
    '../datasets/indicators/Nitrate concentration in groundwater.csv', delimiter=';')
nitrate_concentration_df.rename(
    columns={nitrate_concentration_df.columns[0]: "Type"}, inplace=True)

#  Nature conservation areas
# Percentage of the state's land area
conservation_area_df = pd.read_csv(
    '../datasets/indicators/Nature Conservation.csv', delimiter=';')
conservation_area_df.rename(
    columns={conservation_area_df.columns[0]: "Type"}, inplace=True)
conservation_cols = ['Type'] + list(conservation_area_df.columns[67:])
conservation_area_df = conservation_area_df[conservation_cols]

# kilo equivalents per hectare
acid_input_df = pd.read_csv(
    '../datasets/indicators/acid_input.csv', delimiter=';')
acid_input_df.rename(
    columns={acid_input_df.columns[0]: "Type"}, inplace=True)

# Maybe a measure of Climate change
endangered_df = pd.read_csv(
    '../datasets/indicators/Endangered species.csv', delimiter=';')
endangered_df.rename(columns={endangered_df.columns[0]: "Type"}, inplace=True)
endangered_df['Type'] = endangered_df['Type'].map(lambda x: x[0:4])
endangered_df = endangered_df.transpose()

datasets_list = [no2_emission_df, ozone_concentration_df,
                 waste_df, green_house_gases_df, no2_concentration_df,
                 particulate_matter_df, recycling_df, consumption_df,
                 settlement_df, heavy_metal_df, nitrate_concentration_df,
                 conservation_area_df, acid_input_df]

for i, dataset_df in enumerate(datasets_list):
    table_name = table_names[i]
    dataset_df['Type'] = table_name + '_' + dataset_df['Type']
    dataset_df.to_sql(table_name, connection, if_exists='replace', index=False)

indicator_df = pd.concat(datasets_list, axis=0, ignore_index=True)
sorted_cols = ['Type'] + sorted(indicator_df.columns[1:])

indicator_df = indicator_df[sorted_cols]
print(indicator_df)

indicator_df.to_sql('env_indicators', connection, if_exists='replace', index=False)
temp_df.to_sql('temperature', connection, if_exists='replace', index=False)
endangered_df.to_sql('endangered', connection, if_exists='replace', index=False)
print(indicator_df)
