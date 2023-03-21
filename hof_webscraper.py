from bs4 import BeautifulSoup as soup
import bs4
from urllib.request import urlopen as uReq
import csv
from file_cleaner import cleanAchievementData, exportData

base_url = "https://en.hispanosnba.com/players/hall-of-fame/index"
uClient = uReq(base_url)
hof_html = uClient.read()
uClient.close()
hof_soup = soup(hof_html, "lxml")

fields = ["Player"]
hof_container = hof_soup.find("table", {"class":"tblprm"})
print(hof_container.tbody)

players = []
for row in hof_container.tbody:
    print(type(row))
    if row.th["class"] == "tra":
        continue
    players.append([row.th.a.text])

with open("hof.csv", "w") as f:
    hof_writer = csv.writer(f)
    hof_writer.writerow(fields)
    hof_writer.writerows(players)

hof_df = cleanAchievementData("hof.csv")
exportData(hof_df, "hof")