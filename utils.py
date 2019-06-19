import pandas as pd
import os
import sys


def resource_path(relative):
    application_path = os.path.abspath('.')
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    return os.path.join(application_path, relative)


def get_player_list():
    df = pd.read_csv('data/data.csv')
    record = df[['Name', 'Flag']].to_dict('record')
    return [list(r.values()) for r in record]


def get_player_pattern():
    df = pd.read_csv('data/data.csv')
    return df['Name'].to_string(index=False).replace('  ', '').replace('\n ', '|').replace('\n', '|')


def get_player_attributes(playername):
    df = pd.read_csv('data/data.csv')
    df = df[df.drop(
        ['Value', 'Wage', 'Special', 'Joined', 'Loaned From', 'Contract Valid Until', 'LS', 'ST', 'RS',
         'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM',
         'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', ], 1).columns.tolist()[2:-1]]
    temp = df['Work Rate'].str.split('/', expand=True)
    df['Work Rate'] = temp[0] + ' / ' + temp[1]
    return df[df['Name'] == playername].to_dict('r')[0]
