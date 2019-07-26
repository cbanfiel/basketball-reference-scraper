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
    "Team": "duke"
  },
  {
    "Team": "virginia"
  },
  {
    "Team": "north-carolina"
  },
  {
    "Team": "gonzaga"
  },
  {
    "Team": "tennessee"
  },
  {
    "Team": "michigan-state"
  },
  {
    "Team": "kentucky"
  },
  {
    "Team": "michigan"
  },
  {
    "Team": "houston"
  },
  {
    "Team": "texas-tech"
  },
  {
    "Team": "louisiana-state"
  },
  {
    "Team": "purdue"
  },
  {
    "Team": "kansas"
  },
  {
    "Team": "florida-state"
  },
  {
    "Team": "kansas-state"
  },
  {
    "Team": "virginia-tech"
  },
  {
    "Team": "marquette"
  },
  {
    "Team": "auburn"
  },
  {
    "Team": "wisconsin"
  },
  {
    "Team": "mississippi-state"
  },
  {
    "Team": "villanova"
  },
  {
    "Team": "maryland"
  },
  {
    "Team": "buffalo"
  },
  {
    "Team": "iowa-state"
  },
  {
    "Team": "louisville"
  },
  {
    "Team": "nevada"
  },
  {
    "Team": "cincinnati"
  },
  {
    "Team": "wofford"
  },
  {
    "Team": "virginia-commonwealth"
  },
  {
    "Team": "syracuse"
  },
  {
    "Team": "mississippi"
  },
  {
    "Team": "utah-state"
  },
  {
    "Team": "washington"
  },
  {
    "Team": "central-florida"
  },
  {
    "Team": "baylor"
  },
  {
    "Team": "oklahoma"
  },
  {
    "Team": "iowa"
  },
  {
    "Team": "seton-hall"
  },
  {
    "Team": "minnesota"
  },
  {
    "Team": "florida"
  },
  {
    "Team": "ohio-state"
  },
  {
    "Team": "belmont"
  },
  {
    "Team": "temple"
  },
  {
    "Team": "saint-marys-ca"
  },
  {
    "Team": "arizona-state"
  },
  {
    "Team": "murray-state"
  },
  {
    "Team": "st-johns-ny"
  },
  {
    "Team": "oregon"
  },
  {
    "Team": "new-mexico-state"
  },
  {
    "Team": "liberty"
  },
  {
    "Team": "california-irvine"
  },
  {
    "Team": "vermont"
  },
  {
    "Team": "saint-louis"
  },
  {
    "Team": "northeastern"
  },
  {
    "Team": "yale"
  },
  {
    "Team": "old-dominion"
  },
  {
    "Team": "georgia-state"
  },
  {
    "Team": "northern-kentucky"
  },
  {
    "Team": "montana"
  },
  {
    "Team": "colgate"
  },
  {
    "Team": "bradley"
  },
  {
    "Team": "abilene-christian"
  },
  {
    "Team": "gardner-webb"
  },
  {
    "Team": "iona"
  },
  {
    "Team": "prairie-view"
  },
  {
    "Team": "fairleigh-dickinson"
  },
  {
    "Team": "north-dakota-state"
  },
  {
    "Team": "north-carolina-central"
  }
]

names = json.dumps(teams)
names2 = json.loads(names)
print(len(names2))
for team in names2:
    try:
        url = "https://www.sports-reference.com/cbb/schools/" + team["Team"] + "/2019.html"
        soup = make_soup(url)
        table_roster = soup.select('table#roster')
        table_stats = soup.select('table#per_game')
        players_roster = table_roster[0].select('tbody')
        player_statistics = table_stats[0].select('tbody')
        player_stats_tr = players_roster[0].find_all('tr')

        index = -1
        for row in player_stats_tr:
            playerData += team["Team"] +','
            index += 1
            for cell in row.find_all('th'):
                playerData = playerData + cell.text + ","
            for cell in row.find_all('td'):
                playerData = playerData + cell.text + ","
            playerData += "\n"

        for row in player_statistics[0].find_all('tr'):
          playerStatistics += team["Team"] + ','
          index += 1
          for cell in row.find_all('th'):
            playerStatistics = playerStatistics + cell.text + ","
          for cell in row.find_all('td'):
            playerStatistics = playerStatistics + cell.text + ","
          playerStatistics += "\n"
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
file = open(os.path.expanduser("Basketball.csv"),"wb")
file.write(bytes(playerData, encoding="ascii", errors="ignore"))

file = open(os.path.expanduser("Statistics.csv"),"wb")
file.write(bytes(playerStatistics, encoding="ascii", errors="ignore"))
