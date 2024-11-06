import requests

url = "https://wnba-api.p.rapidapi.com/player-advanced-stats"

querystring = {"playerId":"4433403"}

headers = {
	"x-rapidapi-key": "bbab47d613mshc6d4bd010325bd8p15a54bjsn74ce75016aad",
	"x-rapidapi-host": "wnba-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())