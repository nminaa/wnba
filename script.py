from nba_api.stats.endpoints import playercareerstats
import pandas as pd
# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()

for entry in career.get_dict():
    print(entry)