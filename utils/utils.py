from unidecode import unidecode


def clean_playername(name):
    return unidecode(name.replace(".", "").replace(" ", "_").upper())


def get_player_list(df):
    record = df[["Name", "Flag"]].to_dict("records")
    return [list(r.values()) for r in record]


def get_player_pattern(df):
    return (
        df["Name"]
        .to_string(index=False)
        .replace("  ", "")
        .replace("\n ", "|")
        .replace("\n", "|")
    )


def get_player_attributes(df, playername):
    temp_wr = df["Work Rate"].str.split("/", expand=True)
    df["Work Rate"] = temp_wr[0] + " / " + temp_wr[1]

    df["NameFMT"] = df["Name"].apply(clean_playername)

    return df[df["NameFMT"] == playername].to_dict("records")[0]
