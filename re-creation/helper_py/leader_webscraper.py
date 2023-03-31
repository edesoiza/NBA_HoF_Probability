from bs4 import BeautifulSoup as soup
import os
from urllib.request import urlopen as uReq
import csv

script_dir = os.path.dirname(__file__) 
raw_path = os.path.join(script_dir, '../../data/raw')

base_url = "https://www.basketball-reference.com/leaders/pts_per_g_yearly.html"
urls = [("https://www.basketball-reference.com/leaders/pts_per_g_yearly.html", "ppg_leaders"), 
("https://www.basketball-reference.com/leaders/trb_per_g_yearly.html", "rpg_leaders"),
("https://www.basketball-reference.com/leaders/ws_yearly.html", "apg_leaders"),
("https://www.basketball-reference.com/leaders/ws_yearly.html", "ws_leaders")]
for url in urls:
    uPPG = uReq(url[0])
    ppg_html = uPPG.read()
    uPPG.close()
    ppg_soup = soup(ppg_html, "lxml")

    fields = ["Player"]

    ppg_container = ppg_soup.find("table", {"id" : "leaders"})
    leaders = ppg_container.find_all("tr")

    rows = []
    for i in leaders[1:]:
        j = i.find_all("td")
        if j[2].strong:
            rows.append([j[2].strong.a.text])
        else:
            rows.append([j[2].a.text])

    with open(raw_path + "/" + url[1] + ".csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)
    print(url[1])
