import pandas as pd
import re

def cleanAchievementData(file_name):
    data_raw = pd.read_csv(file_name)
    data_cleaned = data_raw[:]
    #Getting rid of special characters
    regex = re.compile('[^a-zA-Z -\']')
    data_cleaned["Player"] = [regex.sub('', row) for row in data_cleaned["Player"]]
    #Random Spaces at the end and beginning
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('^ +| +$', '')
    #Nikola Jokic Name Comes out weird
    data_cleaned["Player"] = data_cleaned["Player"].replace("Nikola Joki","Nikola Jokic")
    #Kareem used to be called Lew Alcindor
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('Lew Alcindor', 'Kareem Abdul-Jabbar')
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('Kareem AbdulJabbar', 'Kareem Abdul-Jabbar')
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('Tiny Archibald', 'Nate Archibald')
    data_cleaned["Player"] = data_cleaned["Player"].str.replace('Luka Doni', 'Luka Doncic')
    return data_cleaned

def exportData(df, name):
    df.to_csv(name + "_cleaned.csv")

files_to_be_cleaned = [("dpoy.csv", "dpoy"), ("mvp.csv", "mvp"), ("fmvp.csv", "fmvp"), ("allstar.csv", "allstar"), ("allnba.csv", "allnba")]

for tup in files_to_be_cleaned:
    df = cleanAchievementData(tup[0])
    print(tup[0][:-4])
    exportData(df, tup[1])

