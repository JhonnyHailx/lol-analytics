import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Exemplo: dragões capturados média aos 15min
team_df['dragons_per_game'] = team_df['dragons'] / team_df['partidas'] if 'partidas' in team_df.columns else team_df['dragons'] # fallback
team_time_obj = team_df.groupby('teamname').agg({
    'dragons_per_game': 'mean',
    'heralds': 'mean',
    'barons': 'mean',
    'towers': 'mean',
    'gamelength': 'mean'
}).reset_index()
team_time_obj.to_csv('data/reports/team_objectives_per_game.csv', index=False)
print(team_time_obj.head())
print("Relatório salvo em data/reports/team_objectives_per_game.csv")
