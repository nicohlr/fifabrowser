import pandas as pd
from unidecode import unidecode


def clean_playername(name):
    return unidecode(name.replace('.', '').replace(' ', '_').upper())


def get_player_list():
    df = pd.read_csv('data/data.csv')
    record = df[['Name', 'Flag']].to_dict('record')
    return [list(r.values()) for r in record]


def get_player_pattern():
    df = pd.read_csv('data/data.csv')
    return (df['Name'].to_string(index=False)
                      .replace('  ', '')
                      .replace('\n ', '|')
                      .replace('\n', '|'))


def get_player_attributes(playername):

    cols_to_drop = [
        'Value', 'Wage', 'Special', 'Joined', 'Loaned From', 'LS', 'ST', 'RS',
        'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'RDM',
        'Contract Valid Until', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RWB',
        'LB', 'LCB', 'CB', 'RCB', 'RB', 'Photo', 'Club Logo'
    ]

    df = pd.read_csv('data/data.csv')
    df = df[df.drop(cols_to_drop, 1).columns.tolist()[2:-1]]

    temp_wr = df['Work Rate'].str.split('/', expand=True)
    df['Work Rate'] = temp_wr[0] + ' / ' + temp_wr[1]

    df['NameFMT'] = df['Name'].apply(clean_playername)

    return df[df['NameFMT'] == playername].to_dict('records')[0]
