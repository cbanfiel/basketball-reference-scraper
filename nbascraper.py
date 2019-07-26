import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import json


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerData=""
player_stats =""
playerStatistics = ""

teams = [
  {
    "Team": "ATL"
  },
  {
    "Team": "BOS"
  },
  {
    "Team": "BRK"
  },
  {
    "Team": "CHA"
  },
  {
    "Team": "CHH"
  },
  {
    "Team": "CHI"
  },
  {
    "Team": "CLE"
  },
  {
    "Team": "DAL"
  },
  {
    "Team": "DEN"
  },
  {
    "Team": "DET"
  },
  {
    "Team": "GSW"
  },
  {
    "Team": "HOU"
  },
  {
    "Team": "IND"
  },
  {
    "Team": "LAC"
  },
  {
    "Team": "LAL"
  },
  {
    "Team": "MEM"
  },
  {
    "Team": "MIA"
  },
  {
    "Team": "MIL"
  },
  {
    "Team": "MIN"
  },
  {
    "Team": "NJN"
  },
  {
    "Team": "NOH"
  },
  {
    "Team": "NOK"
  },
  {
    "Team": "NOP"
  },
  {
    "Team": "OKC"
  },
  {
    "Team": "NYK"
  },
  {
    "Team": "ORL"
  },
  {
    "Team": "PHI"
  },
  {
    "Team": "PHO"
  },
  {
    "Team": "POR"
  },
  {
    "Team": "SAS"
  },
  {
    "Team": "SAC"
  },
  {
    "Team": "SEA"
  },
  {
    "Team": "TOR"
  },
  {
    "Team": "UTA"
  },
  {
    "Team": "VAN"
  },
  {
    "Team": "WAS"
  },
  {
    "Team": "WSB"
  }
]


names = json.dumps(teams)
names2 = json.loads(names)
print(len(names2))
for team in names2:
    try:
        url = "https://www.basketball-reference.com/teams/" + team["Team"] + "/1996.html"
        soup = make_soup(url)
        table_roster = soup.select('table#roster')
        players_roster = table_roster[0].select('tbody')

        player_stats_tr = players_roster[0].find_all('tr')

        index = -1
        for row in player_stats_tr:
            playerData += team["Team"] +','
            index += 1
            for cell in row.find_all('th'):
                playerData = playerData + cell.text + ","
            for cell in row.find_all('td'):
                playerData = playerData + cell.text + ","
                for link in cell.find_all('a', href=True):
                    playerData = playerData + link['href'] + ","
            playerData += "\n"



    except:
        print('err ' + team["Team"])


# print(playerData)

# for tr in players_roster:
#     td = tr.findAll('td')
#     row = [i.text for i in td]
#     print(row)


#
# for record in soup.select('table#roster'):
#     for data in record.findAll('tbody'):
#             for player in data.findAll('tr'):
#                 playerData+="Duke,"
#                 for stats in player.findAll('td'):
#                     playerData+= ","+stats.text
#                 playerData+="\n"
#
# for record in soup.select('table#per_game'):
#     for data in record.findAll('tbody'):
#             for player in data.findAll('tr'):
#                 for stats in player.findAll('td'):
#                     player_stats+= ","+stats.text
#                 player_stats+="\n"
#
# newData = ""
# for record in zip(playerData, player_stats):
#     newData += " ".join(record)
#
#
#
#
#
#
file = open(os.path.expanduser("NBABasketball.csv"),"wb")
file.write(bytes(playerData, encoding="ascii", errors="ignore"))

