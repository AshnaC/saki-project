from data.utils import get_files, files_to_ignore
import pandas as pd
import sqlite3

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

connection = sqlite3.connect(parent_dir + "/data/dataset.sqlite")

df_obj = {}


def read_all_files():
    files = get_files()
    for file in files:
        read_file(file)
    read_temperature_file()


def read_file(file_name):
    field = file_name.replace('.csv', '')
    df = read_csv_file(file_name)
    df.rename(columns={df.columns[0]: "Type"}, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    df.columns = df.columns.astype(str)
    df.rename(lambda x: x[0:4], axis='columns', inplace=True)
    df_obj[field] = customize_df(df, field)
    return df_obj[field]


def read_temperature_file():
    field = 'temperature'
    df = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/export?gid=0&format=csv',
        header=None).transpose()
    df = df.set_axis(df.iloc[0], axis=1).drop(df.index[0])
    df.rename(columns={df.columns[0]: "Type"}, inplace=True)
    df.columns = df.columns.astype(str).str.split('.').str[0]
    cols = ['Type'] + list(df.columns[103:142])
    df_obj[field] = df[cols]


def customize_df(df, name):
    if name == 'Nature Conservation':
        conservation_cols = ['Type'] + list(df.columns[67:])
        df = df[conservation_cols]
    return df


def read_csv_file(file_name):
    file_url = parent_dir + '/datasets/indicators/' + file_name
    return pd.read_csv(file_url, delimiter=';', decimal=',')


def create_combined_df():
    count = 0
    read_all_files()
    df_list = []
    keys = []
    for key, value in df_obj.items():
        if key not in files_to_ignore:
            count = count + 1
            value['Type'] = key + '--' + value['Type']
            # print(key)
            # print(value)
            keys.append(key)
            df_list.append(value)
    # print(keys)
    indicator_df = pd.concat(df_list, axis=0, ignore_index=True)
    sorted_cols = ['Type'] + sorted(indicator_df.columns[1:])
    indicator_df = indicator_df[sorted_cols]
    # print('count', count)
    # print(indicator_df)
    return indicator_df


def load_files():
    endangered_df = read_file('Endangered species.csv')
    endangered_df = endangered_df.transpose()
    # temp_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
    #                       'export?gid=0&format=csv')
    indicator_df = create_combined_df()
    indicator_df.to_sql('env_indicators', connection,
                        if_exists='replace', index=False)
    # temp_df.to_sql('temperature', connection, if_exists='replace', index=False)
    endangered_df.to_sql('endangered', connection,
                         if_exists='replace', index=False)
    # connection.close()


def load_temperature_file():
    temp_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1o4CAldClFDAskwaXhDe0Hw7r4WY7VyDL91o51c4py_c/'
                          'export?gid=0&format=csv')
    temp_df.to_sql('temperature', connection, if_exists='replace', index=False)


# load_files()
load_temperature_file()
# print(df_obj)
