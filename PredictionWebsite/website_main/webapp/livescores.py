import requests
import json

url = "https://api.sofascore.com/api/v1/sport/cricket/events/live"

payload = ""
headers = {
    'authority': "api.sofascore.com",
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9",
    'if-none-match': "W/^\^4291778428^^",
    'origin': "https://www.sofascore.com",
    'referer': "https://www.sofascore.com/",
    'sec-ch-ua': "^\^"
    }

response = requests.request("GET", url, data=payload, headers=headers)

jsondata = json.loads(response.text)


match_data = []

for i in range(len(jsondata['events'])):
    if jsondata['events'][i]['tournament']['name'] == 'Indian Premier League':
        team1 = jsondata['events'][i]['homeTeam']['name']
        team2 = jsondata['events'][i]['awayTeam']['name']

        try:
            team1_runs = jsondata['events'][i]['homeScore']['innings']['inning1']['score']
            team1_wickets = jsondata['events'][i]['homeScore']['innings']['inning1']['wickets']
            team1_overs = jsondata['events'][i]['homeScore']['innings']['inning1']['overs']
            # team2_runs = jsondata['events'][i]['homeScore']['innings']['inning2']['score']
            # team2_wickets = jsondata['events'][i]['homeScore']['innings']['inning2']['wickets']
            # team2_overs = jsondata['events'][i]['homeScore']['innings']['inning2']['overs']
        except KeyError:
            try:
                team1_runs = jsondata['events'][i]['homeScore']['innings']['inning2']['score']
                team1_wickets = jsondata['events'][i]['homeScore']['innings']['inning2']['wickets']
                team1_overs = jsondata['events'][i]['homeScore']['innings']['inning2']['overs']
            except KeyError:
                team1_runs = 0
                team1_wickets = 0
                team1_overs = 0

        try:
            team2_runs = jsondata['events'][i]['awayScore']['innings']['inning1']['score']
            team2_wickets = jsondata['events'][i]['awayScore']['innings']['inning1']['wickets']
            team2_overs = jsondata['events'][i]['awayScore']['innings']['inning1']['overs']
            # team1_runs = jsondata['events'][i]['homeScore']['innings']['inning2']['score']
            # team1_wickets = jsondata['events'][i]['homeScore']['innings']['inning2']['wickets']
            # team1_overs = jsondata['events'][i]['homeScore']['innings']['inning2']['overs']
        except KeyError:
            try:
                team2_runs = jsondata['events'][i]['awayScore']['innings']['inning2']['score']
                team2_wickets = jsondata['events'][i]['awayScore']['innings']['inning2']['wickets']
                team2_overs = jsondata['events'][i]['awayScore']['innings']['inning2']['overs']
            except KeyError:
                team2_runs = 0
                team2_wickets = 0
                team2_overs = 0

        match_data.append(
            {
                'team1': team1,
                'team1_runs': team1_runs,
                'team1_wickets': team1_wickets,
                'team1_overs': team1_overs,
                'team2': team2,
                'team2_runs': team2_runs,
                'team2_wickets': team2_wickets,
                'team2_overs': team2_overs,
            }
        )

print(match_data)
