import csv

player_dict = {}
with open("player_data.csv") as f:
    for val in csv.reader(f):
        player_name = val[0]

        if player_name == "Metta World Peace":
            player_name = "Ron Artest"
        if player_name == "Tiny Archibald":
            player_name = "Nate Archibald" 

        player_dict[player_name] = {}
        player_dict[player_name]["year_start"] = val[1]
        player_dict[player_name]["year_end"] = val[2]

stat_collector = {}
stat_ind = [("ptotal", 52), ("atotal", 47), ("rtotal", 46), ("stotal", 48), ("btotal", 49)]
accolade_files = [("dpoy_cleaned.csv", "dpoy"), ("mvp_cleaned.csv", "mvp"), ("fmvp_cleaned.csv", "fmvp")]

with open("Seasons_Stats.csv") as f:
    season_file = csv.reader(f)

    for i, val in enumerate(season_file):
        if i == 0:
            continue
        if not val[1]:
            continue

        player_name = val[2]
        if player_name.endswith("*"):
            player_name = player_name[:-1]
        if player_name == "Metta World":
            player_name = "Ron Artest"
        if player_name == "Jo Jo":
            player_name = "Jo Jo White"
        if player_name == "Tiny Archibald":
            player_name = "Nate Archibald" 

        if player_name not in stat_collector:
            stat_collector[player_name] = {}
            for i in stat_ind:
                stat_collector[player_name][i[0]] = [0,0]
            for i in accolade_files:
                stat_collector[player_name][i[1]] = 0
            stat_collector[player_name]["allstar"] = 0

        for i in stat_ind:
            if val[i[1]] and stat_collector[player_name][i[0]] != "NA":
                stat_collector[player_name][i[0]][0] += int(val[i[1]])
                stat_collector[player_name][i[0]][1] += int(val[6])
            else:
                stat_collector[player_name][i[0]] = "NA"

for player in stat_collector:
    for stat in stat_ind:
        if not stat_collector[player][stat[0]][1]:
            stat_collector[player][stat[0]] = 0
            continue
        if stat_collector[player][stat[0]] == "NA":
            continue
        stat_per_game = stat_collector[player][stat[0]][0] / stat_collector[player][stat[0]][1]
        stat_collector[player][stat[0]] = round(stat_per_game, 2)

accolade_files = ["dpoy", "mvp", "fmvp"]
for accolade in accolade_files:
    with open(accolade + "_cleaned.csv") as f:
        accolade_file = csv.reader(f)
        for i, row in enumerate(accolade_file):
            if i == 0:
                continue
            stat_collector[row[2]][accolade] += 1

all_type_accolades = ['allstar', 'allnba']
for accolade in all_type_accolades:
    with open(accolade + "_cleaned.csv") as f:
        for i, val in enumerate(csv.reader(f)):
            if i == 0:
                continue
            if not stat_collector.get(val[1], False):
                continue
            stat_collector[val[1]][accolade] = int(val[2])

fields = ["name", "ppg", "apg", "rpg", "spg", "bpg", "dpoy", "mvp", "fmvp", "allstar", "allnba"]
rows = [[row] + [stat_collector[row][x] for x in stat_collector[row]] for row in stat_collector]

with open("new_nba_stats", "w") as f:
    new_csv = csv.writer(f)
    new_csv.writerow(fields)
    new_csv.writerows(rows)



        


        

