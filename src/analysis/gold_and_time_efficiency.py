import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

player_df['gpm'] = player_df['totalgold'] / player_df['gamelength']
player_df['dpm'] = player_df['damagetochampions'] / player_df['gamelength']
player_df['kills_per_min'] = player_df['kills'] / player_df['gamelength']
efficiency = player_df.groupby('playername').agg({
    'gpm': 'mean',
    'dpm': 'mean',
    'kills_per_min': 'mean'
}).reset_index()
efficiency.to_csv('data/reports/player_gold_time_efficiency.csv', index=False)
print(efficiency.head())
print("Relatório salvo em data/reports/player_gold_time_efficiency.csv")
