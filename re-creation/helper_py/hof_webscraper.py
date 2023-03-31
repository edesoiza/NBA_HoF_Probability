from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
from file_cleaner import cleanAchievementData, exportData
import os

script_dir = os.path.dirname(__file__) 
raw_path = os.path.join(script_dir, '../../data/raw')

base_url = "https://en.hispanosnba.com/players/hall-of-fame/index"
uClient = uReq(base_url)
hof_html = uClient.read()
uClient.close()
hof_soup = soup(hof_html, "lxml")

fields = ["Player"]
hof_container = hof_soup.find("table", {"class":"tblprm"})

players = []
for row in hof_container.tbody:
    if row.th["class"] == "tra":
        continue
    players.append([row.th.a.text])

with open(raw_path + "/" +" hof.csv", "w") as f:
    hof_writer = csv.writer(f)
    hof_writer.writerow(fields)
    hof_writer.writerows(players)
