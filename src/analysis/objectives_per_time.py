import sqlite3
import pandas as pd

drake_types = ['infernals', 'mountains', 'clouds', 'oceans', 'chemtechs', 'hextechs', 'elders']

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

if 'partidas' not in team_df.columns:
    partidas = team_df.groupby('teamname').size().reset_index(name='partidas')
    team_df = pd.merge(team_df, partidas, on='teamname', how='left')

team_df['dragons_total'] = team_df[drake_types].sum(axis=1)
team_df['dragons_per_game'] = team_df['dragons_total'] / team_df['partidas']

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
