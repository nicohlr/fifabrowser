import pandas as pd


def get_player_list():
    df = pd.read_csv('data/data.csv')
    record = df[['Name', 'Flag']].to_dict('record')
    return [list(r.values()) for r in record]


def get_player_pattern():
    df = pd.read_csv('data/data.csv')
    return df['Name'].to_string(index=False).replace('  ', '').replace('\n ', '|').replace('\n', '|')
