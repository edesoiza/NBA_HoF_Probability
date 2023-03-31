import csv
import os

script_dir = os.path.dirname(__file__) 
cleaned_data_path = os.path.join(script_dir, '../../data/cleaned')
final_data_path  = os.path.join(script_dir, '../../data/final')

players_dict = {}
accolade_files = ["dpoy", "mvp", "fmvp"]
all_type_accolades = ['allstar', 'allnba']
all_def = "alldef"
leaders = ["ppg_leader", "rpg_leader", "apg_leader", "ws_leader"]
hof = "hof"

with open(cleaned_data_path + "/" + "player_data_bbr_cleaned.csv") as f:
    readerrrr = csv.reader(f)
    for i, val in enumerate(readerrrr):
        if i == 0:
            fields = val[2:]
            total_fields = val[1:] + accolade_files + all_type_accolades + [all_def] + leaders + [hof]
            continue
        try:
            player_dict = {"Player": val[1]} 
            for j, x in enumerate(val[2:]):
                player_dict[fields[j]] = float(x)
        except:
            continue
        for accolade in accolade_files:
            player_dict[accolade] = 0
        for acc in all_type_accolades:
            player_dict[acc] = 0
        player_dict[all_def] = 0
        for leader in leaders:
            player_dict[leader] = 0
        player_dict[hof] = 0

        players_dict[val[1]] = player_dict


for accolade in accolade_files:
    with open(cleaned_data_path + "/" + accolade + "_cleaned.csv") as f:
        accolade_file = csv.reader(f)
        for i, row in enumerate(accolade_file):
            if i == 0:
                continue
            if row[2] in players_dict:
                players_dict[row[2]][accolade] += 1

for accolade in all_type_accolades:
    with open(cleaned_data_path + "/" + accolade + "_cleaned.csv") as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue
            if row[1] in players_dict:
                players_dict[row[1]][accolade] = int(row[2])

with open(cleaned_data_path + "/" + all_def + "_formatted_cleaned.csv") as f:
    for i, row in enumerate(csv.reader(f)):
        if i == 0:
            continue
        if row[1] in players_dict:
            players_dict[row[1]][all_def] += 1

for leader in leaders:
    with open(cleaned_data_path + "/" + leader + "s_cleaned.csv") as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue
            if row[1] in players_dict:
                players_dict[row[1]][leader] += 1
            else:
                print("here", row[1])
with open(cleaned_data_path + "/" + "hof_cleaned.csv") as f:
    for i, row in enumerate(csv.reader(f)):
        if i == 0:
            continue

        if row[1] in players_dict:
            players_dict[row[1]][hof] += 1
        else:
            print("here", row[1])
        

with open(final_data_path + "/" + "final_player_data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames= total_fields)
    writer.writeheader()
    writer.writerows(players_dict.values())


