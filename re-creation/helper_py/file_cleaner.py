import pandas as pd
import re
import os
from unidecode import unidecode

def cleanAchievementData(file_name):
    data_raw = pd.read_csv(file_name)
    data_cleaned = data_raw[:]
    #Getting rid of special characters
    data_cleaned["Player"] = [unidecode(row) for row in data_cleaned["Player"]]
    data_cleaned["Player"] = [row[:-2] if row.endswith("SS") else row for row in data_cleaned["Player"]]

    regex = re.compile('[^a-zA-Z -\']')
    data_cleaned["Player"] = [regex.sub('', row) for row in data_cleaned["Player"]]

    data_cleaned["Player"] = [row[:-4] if row.endswith(" tie") else row for row in data_cleaned["Player"]]
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('^ +| +$', '')
    
    swap_names = [('Lew Alcindor', 'Kareem Abdul-Jabbar'), 
    ('Kareem AbdulJabbar', 'Kareem Abdul-Jabbar'), ('Luka Doni', 'Luka Doncic'), 
    ('Ron Artest', 'Metta World Peace'), ('Nate Archibald', 'Tiny Archibald'),
    ('Johnny Kerr', 'Red Kerr'), ('Penny Hardaway', 'Anfernee Hardaway'), ("Frank Brian", "Frankie Brian"),
    ("Dwight Eddleman", 'Dike Eddleman'), ("Rod Hundley", "Hot Rod Hundley"), 
    ("B J Armstrong", "BJ Armstrong"), ("Nathaniel Clifton", "Nat Clifton"), ("Billy Gabor", "Bill Gabor"),
    ("A C Green", "AC Green"), ("Lucious Jackson", "Luke Jackson"), ("P J Brown", "PJ Brown"),
    ("Mike Conley Jr", "Mike Conley"), ("Robert Williams III", "Robert Williams"),
    ("Akeem Olajuwon", "Hakeem Olajuwon"), ("Lafayette Lever", "Fat Lever"), ("T R Dunn", "TR Dunn"),
    ("Wayne Rollins", "Tree Rollins"), ("M L Carr", "ML Carr"), ("E C Coleman","EC Coleman"), 
    ("Don Watts", "Slick Watts")]
    for old,new in swap_names:
        data_cleaned["Player"] = data_cleaned["Player"].str.replace(old,new)

    return data_cleaned

def exportData(df, name, path):
    df.to_csv(path + name + "_cleaned.csv")

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    data_path = os.path.join(script_dir, '../../data')
    files_to_be_cleaned = ["dpoy.csv", "mvp.csv", "fmvp.csv", "allstar.csv", 
    "allnba.csv", "alldef_formatted.csv", "player_data_bbr.csv", "ppg_leaders.csv", 
    "rpg_leaders.csv", "apg_leaders.csv", "ws_leaders.csv", "hof.csv"]

    for file in files_to_be_cleaned:
        df = cleanAchievementData(data_path + '/raw/' + file)
        print(file[:-4])
        exportData(df, file[:-4], data_path + "/cleaned/")

