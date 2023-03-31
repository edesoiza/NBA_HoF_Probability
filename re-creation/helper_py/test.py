import os
import pandas as pd
script_dir = os.path.dirname(__file__) 
raw_data_path = os.path.join(script_dir, '../../data/raw')
shit = pd.read_csv(raw_data_path + "/hof.csv")
print(shit)
print(raw_data_path)
