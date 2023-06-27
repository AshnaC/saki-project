from os import listdir
from os.path import isfile, join

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

table_names = ['no2_emission', 'ozone_concentration',
               'waste', 'green_house_gases', 'no2_concentration',
               'particulate_matter', 'recycling', 'consumption',
               'settlement', 'heavy_metal', 'nitrate_concentration',
               'conservation_area', 'acid_input']

files_to_ignore = ['Agricultural land with high natural value', 'Particulate matter emissions',
                   'Endangered species', 'nlr-02-artenvielfalt', 'Ecological condition of surface watercourses',
                   'noise_pollution_night', 'noise_pollution_day']


def print_colored(text, color):
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m'
    }
    color_code = color_codes.get(color.lower())
    if color_code:
        print(f"{color_code}{text}\033[0m")
    else:
        print(text)


def get_file_prefixes():
    files = get_files()
    prefixes = []
    for file in files:
        if file.replace('.csv', '') not in files_to_ignore:
            prefixes.append(file.replace('.csv', ''))
    return prefixes


def get_files():
    file_list = [f for f in listdir(parent_dir + '/datasets/indicators/') if
                 isfile(join(parent_dir + '/datasets/indicators/', f))
                 and f.endswith('.csv')]
    return file_list

# Function to print colored text
