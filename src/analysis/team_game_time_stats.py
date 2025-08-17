import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

game_time_stats = df.groupby('teamname').agg({
    'gamelength': ['mean', 'std', 'min', 'max']
}).reset_index()
game_time_stats.columns = ['teamname','game_time_mean','game_time_std','game_time_min','game_time_max']
game_time_stats.to_csv('data/reports/team_game_time_stats.csv', index=False)
print(game_time_stats.head())
print("Relatório salvo em data/reports/team_game_time_stats.csv")

