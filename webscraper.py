from bs4 import BeautifulSoup as soup
import bs4
from urllib.request import urlopen as uReq
import csv
import time

def parse_all_alphabet(url):
    base_url = "https://www.basketball-reference.com/"
    uAlpha = uReq(url)
    abc_html = uAlpha.read()
    uAlpha.close()
    abc_soup = soup(abc_html, "lxml")

    fields = ["Player", "start", "end", "ppg", "apg", "rpg", "spg", "bpg"]
    create_csv(fields)

    abc_container = abc_soup.find("div", {"id": "all_alphabet"})
    for element in abc_container:
        if not isinstance(element, bs4.element.Comment):
            continue
        abc_lst = element.split("href=\"")
        for letter in abc_lst:
            if letter[0] != "/":
                continue
            letter_url = base_url + letter[1:11]
            time.sleep(10)
            parse_single_alphabet(letter_url)
            

def parse_single_alphabet(url):
    uLetter = uReq(url)
    letter_html = uLetter.read()
    uLetter.close()
    a_soup = soup(letter_html, "lxml")

    alpha_container = a_soup.find("div", {"id" :"div_players"})
    alpha_table = alpha_container.find("table").tbody
    for trow in alpha_table:
        if not isinstance(trow, bs4.element.Tag):
            continue
        player_url = url + trow.th["data-append-csv"] + ".html"
        player_name = trow.th.a.text
        year_start = int(trow.find("td", {"data-stat":"year_min"}).text)
        year_end = int(trow.find("td", {"data-stat":"year_max"}).text)

        row = [player_name, year_start, year_end]
        time.sleep(5)
        try:
            row += parse_single_player(player_url)
        except:
            row += ["Error"] * 5

        print(player_name)
        update_csv(row)
        
def parse_single_player(url):
    uPlayer = uReq(url)
    player_html = uPlayer.read()
    uPlayer.close()
    player_soup = soup(player_html, "lxml")

    stats = ["pts", "ast", "trb", "stl", "blk"]
    total_stat_lst = [[0,0],[0,0],[0,0],[0,0],[0,0]]

    total_table = player_soup.find("div", {"id": "div_totals"}).table.tbody
    for row in total_table:
        if not isinstance(row, bs4.element.Tag):
            continue
        if row["class"] != ["full_table"]:
            continue

        g_played = int(row.find("td", {"data-stat": "g"}).text)
        for i, stat in enumerate(stats):
            try:
                value = int(row.find("td", {"data-stat": stat}).text)
                total_stat_lst[i][0] += value
                total_stat_lst[i][1] += g_played
            except:
                continue

    career_averages = [round(x[0] / x[1], 2) if x[1] else 0 for x in total_stat_lst]
    return career_averages

def create_csv(fields):
    with open("player_data_bbr.csv", "w") as f:
        new_csv = csv.writer(f)
        new_csv.writerow(fields)

def update_csv(row):
    with open("player_data_bbr.csv", "a") as f:
        curr_csv = csv.writer(f)
        curr_csv.writerow(row)

if __name__ == "__main__":
    abc_url = "https://www.basketball-reference.com/players/"
    parse_all_alphabet(abc_url)