import pandas as pd
import sqlite3

connection = sqlite3.connect("dataset.db")

indicators_additional_df = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
    'export?gid=1924564310&format=csv')
    
# print(indicators_additional_df)

# indicators_additional_df.to_sql('env_indicators_additional', connection, if_exists='replace', index=False)


temp_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
                      'export?gid=0&format=csv')

# temp_df.to_sql('temperature', connection, if_exists='replace', index=False)

# df = pd.read_sql('select * from temperature', connection)
# print(df)

# Household waste - kg/head
# household_waste.csv
waste_df = pd.read_csv('../datasets/indicators/household_waste.csv', delimiter=';')
# print(waste_df.head(2))

# Green House gases  - Million tons of carbon dioxide equivalents
# greenhouse_gas.csv

green_house_gases_df = pd.read_csv('../datasets/indicators/greenhouse_gas.csv', delimiter=';')
green_house_gases_df.rename(columns={green_house_gases_df.columns[0]: "Type"}, inplace=True)
green_house_gases_df.dropna(how='all', axis=1, inplace=True)

# print(green_house_gases_df)

# no2 emission - tons
# nitrogen_oxide_emission.csv

no2_emission_df = pd.read_csv('../datasets/indicators/nitrogen_oxide_emission.csv', delimiter=';')
no2_emission_df.rename(columns={no2_emission_df.columns[0]: "Type"}, inplace=True)
# print(no2_emission_df)

# no2 concentration -  Annual mean value in micrograms per cubic meter
# no2_concentration_urban.csv

no2_concentration_df = pd.read_csv('../datasets/indicators/no2_concentration_urban.csv', delimiter=';')
no2_concentration_df.rename(columns={no2_concentration_df.columns[0]: "Type"}, inplace=True)
no2_concentration_df.at[0, 'Type'] = 'Nitrogen dioxide concentration'
# print(no2_concentration_df)

# Particulate matter emissions - toms
# Particulate matter emissions.csv
# Particulate matter concentration PM10 / PM2.5 in the urban background.csv
particulate_matter_df = pd.read_csv('../datasets/indicators/Particulate matter emissions.csv', delimiter=';',
                                    index_col=[0]).transpose()
particulate_matter_df = particulate_matter_df.reset_index()
particulate_matter_df.rename(columns={particulate_matter_df.columns[0]: "Type"}, inplace=True)
particulate_matter_df.columns = particulate_matter_df.columns.astype(str)
# print(particulate_matter_df.columns)

# Ozone Concentration - Number of hourly mean values above 180 micrograms per cubic meter
# o3-concentration-urban.csv

ozone_concentration_df = pd.read_csv('../datasets/indicators/o3-concentration-urban.csv', delimiter=';')
ozone_concentration_df.rename(columns={ozone_concentration_df.columns[0]: "Type"}, inplace=True)
ozone_concentration_df.at[0, 'Type'] = 'Ozone concentration'
# print(ozone_concentration_df)


# More Data sets to be imported in need

# Noise Pollution - day and night Number affected
# noise_pollution_day.csv
# noise_pollution_night.csv
# noise_pollution_day_df = pd.read_csv('../datasets/indicators/noise_pollution_day.csv', delimiter=';')
# print(noise_pollution_day_df)

# Recycling rate - Recycling rate in percent
# Recycling rate.csv
recycling_df = pd.read_csv('../datasets/indicators/Recycling rate.csv', delimiter=';')
recycling_df.rename(columns={recycling_df.columns[0]: "Type"}, inplace=True)
# print(recycling_df)


# Land Consumption - Hectare per day
# Land consumption.csv
consumption_df = pd.read_csv('../datasets/indicators/Land consumption.csv', delimiter=';')
consumption_df.rename(columns={consumption_df.columns[0]: "Type"}, inplace=True)
# Remove some formatting issues in columns
consumption_df.rename(lambda x: x[0:4], axis='columns', inplace=True)
# print(consumption_df.columns)


# Settlement area - square meters of settlement area per head
# Settlement area.csv
settlement_df = pd.read_csv('../datasets/indicators/Settlement area.csv', delimiter=';')
settlement_df.rename(columns={settlement_df.columns[0]: "Type"}, inplace=True)
print(settlement_df)

# Heavy metal discharge at rural stations -Normalization to 1986 = 1.0
# heavy_metal_rural.csv
heavy_metal_df = pd.read_csv('../datasets/indicators/heavy_metal_rural.csv', delimiter=';')
heavy_metal_df.rename(columns={heavy_metal_df.columns[0]: "Type"}, inplace=True)
# print(heavy_metal_df)


#  Nitrate concentration in groundwater
# Percentage of monitoring sites with nitrate contamination above 50 milligrams per liter
# Percentage of monitoring sites with nitrate levels above 50 mg/l

nitrate_concentration_df = pd.read_csv('../datasets/indicators/Nitrate concentration in groundwater.csv', delimiter=';')
nitrate_concentration_df.rename(columns={nitrate_concentration_df.columns[0]: "Type"}, inplace=True)
# print(nitrate_concentration_df)


#  Nature conservation areas
# Percentage of the state's land area
# Nature Conservation.csv
# Nitrate concentration in groundwater.csv
conservation_area_df = pd.read_csv('../datasets/indicators/Nature Conservation.csv', delimiter=';')
conservation_area_df.rename(columns={conservation_area_df.columns[0]: "Type"}, inplace=True)
conservation_cols =['Type'] + list(conservation_area_df.columns[67:])
conservation_area_df = conservation_area_df[conservation_cols]
# print(conservation_area_df)

# Nitrogen input
# kilograms per hectare
# nitrogen_input.csv

#  Acid input
#  kilo equivalents per hectare
# acid_input.csv

# Nitrogen area balance
# Kilograms of nitrogen per hectare
# Nitrogen area balance.csv

#  Agricultural land with high nature value (HNV)
# Percentage of total agricultural area
# Agricultural land with high natural value.csv

# Endangered species
# Percentage of endangerment categories
# Endangered species.csv

# Maybe a measure of Climate change
endangered_df = pd.read_csv('../datasets/indicators/Endangered species.csv', delimiter=';')
endangered_df.rename(columns={endangered_df.columns[0]: "Type"}, inplace=True)
endangered_df['Type'] = endangered_df['Type'].map(lambda x: x[0:4])
endangered_df = endangered_df.transpose()
# print(endangered_df)

indicator_df = pd.concat(
    [no2_emission_df, ozone_concentration_df,
     waste_df, green_house_gases_df, no2_concentration_df,
     particulate_matter_df, recycling_df, consumption_df,
     settlement_df, heavy_metal_df, nitrate_concentration_df,
     conservation_area_df], axis=0, ignore_index=True)
sorted_cols = ['Type'] + sorted(indicator_df.columns[1:])
# print(sorted_cols)

indicator_df = indicator_df[sorted_cols]
print(indicator_df)
# indicator_df.to_sql('env_indicators', connection, if_exists='replace', index=False)
