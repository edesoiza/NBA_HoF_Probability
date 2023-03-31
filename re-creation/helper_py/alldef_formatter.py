import pandas as pd
import os

def format_data(path, file_name):
    alldef_pd = pd.read_csv(path + file_name)

    new_all_def = pd.DataFrame(columns = ["Player"])
    new_all_def["Player"] = alldef_pd.iloc[1:,1] 
    for i in alldef_pd.iloc[1:,3]:
        new_all_def = new_all_def.append({"Player": i}, ignore_index = True)

    new_all_def.to_csv(path + "alldef_formatted.csv")


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    raw_data_path = os.path.join(script_dir, '../../data/raw')

    format_data(raw_data_path + '/', "alldef.csv")
