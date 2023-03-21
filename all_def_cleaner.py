import csv
from file_cleaner import cleanAchievementData, exportData

all_def_file_name = "alldef.csv"
with open(all_def_file_name) as f:
    all_def_reader = csv.reader(f)

    new_all_def = [["Player"]]
    for i, row in enumerate(all_def_reader):
        if i <= 1:
            continue
        new_all_def.append([row[1]])
        new_all_def.append([row[3]])

all_def_formatted = "all_def_formatted.csv"
with open(all_def_formatted, "w") as f:
    all_def_writer = csv.writer(f)
    all_def_writer.writerows(new_all_def)

alldef_df = cleanAchievementData(all_def_formatted)

alldef_cleaned = "alldef"
exportData(alldef_df, alldef_cleaned)

