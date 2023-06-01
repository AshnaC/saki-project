from os import listdir
from os.path import isfile, join

table_names = ['no2_emission', 'ozone_concentration',
               'waste', 'green_house_gases', 'no2_concentration',
               'particulate_matter', 'recycling', 'consumption',
               'settlement', 'heavy_metal', 'nitrate_concentration',
               'conservation_area', 'acid_input']

files_to_ignore = ['Agricultural land with high natural value', 'temperature', 'Particulate matter emissions',
                   'Endangered species', 'nlr-02-artenvielfalt', 'Ecological condition of surface watercourses',
                   'noise_pollution_night', 'noise_pollution_day']


def get_file_prefixes():
    files = get_files()
    prefixes = []
    for file in files:
        if file.replace('.csv', '') not in files_to_ignore:
            prefixes.append(file.replace('.csv', ''))
    return prefixes


def get_files():
    file_list = [f for f in listdir('../datasets/indicators/') if isfile(join('../datasets/indicators/', f))
                 and f.endswith('.csv')]
    return file_list

