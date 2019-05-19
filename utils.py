import pandas as pd


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
        ['Potential', 'Value', 'Wage', 'Real Face', 'Special', 'International Reputation', 'Joined', 'Loaned From',
         'Contract Valid Until', 'LS', 'ST', 'RS', 'LW',
         'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB',
         'LB', 'LCB', 'CB', 'RCB', 'RB', ], 1).columns.tolist()[2:-1]]

    return df[df['Name'] == playername].to_dict('r')