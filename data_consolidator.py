import csv
import pandas as pd

players_dict = {}
accolade_files = ["dpoy", "mvp", "fmvp"]
all_type_accolades = ['allstar', 'allnba']
all_def = "alldef"
hof = "hof"

with open("player_data_bbr_cleaned.csv") as f:
    readerrrr = csv.reader(f)
    for i, val in enumerate(readerrrr):
        if i == 0:
            fields = val[2:]
            total_fields = val[1:] + accolade_files + all_type_accolades + [all_def] + [hof]
            continue
        try:
            player_dict = {"Player": val[1]} 
            player_dict = {**player_dict, **{fields[i] : float(x) for i, x in enumerate(val[2:])}}
        except:
            print("ero", val[1])
            continue

        player_dict = {**player_dict, **{accolade : 0 for accolade in accolade_files}}
        player_dict = {**player_dict, **{accolade : 0 for accolade in all_type_accolades}}
        player_dict = {**player_dict, **{all_def : 0}}
        player_dict = {**player_dict, **{hof : 0}}

        players_dict[val[1]] = player_dict

for accolade in accolade_files:
    with open(accolade + "_cleaned.csv") as f:
        accolade_file = csv.reader(f)
        for i, row in enumerate(accolade_file):
            if i == 0:
                continue
            if row[2] in players_dict:
                players_dict[row[2]][accolade] += 1

for accolade in all_type_accolades:
    with open(accolade + "_cleaned.csv") as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue
            if row[1] in players_dict:
                players_dict[row[1]][accolade] = int(row[2])

with open(all_def + "_cleaned.csv") as f:
    for i, row in enumerate(csv.reader(f)):
        if i == 0:
            continue
        if row[1] in players_dict:
            players_dict[row[1]][all_def] += 1

with open("hof_cleaned.csv") as f:
    for i, row in enumerate(csv.reader(f)):
        if i == 0:
            continue

        if row[1] in players_dict:
            players_dict[row[1]][hof] += 1
        else:
            print(row[1])

with open("final_player_data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames= total_fields)
    writer.writeheader()
    writer.writerows(players_dict.values())


