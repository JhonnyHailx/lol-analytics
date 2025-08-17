import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

ward_stats = df.groupby('playername').agg({
    'wardsplaced':'sum',
    'wardskilled':'sum',
    'controlwardsbought':'sum',
    'visionscore':'sum'
}).reset_index()
ward_stats['games_played'] = df.groupby('playername').size().values

ward_stats['ward_placement_rate'] = ward_stats['wardsplaced'] / ward_stats['games_played']
ward_stats['ward_kill_rate'] = ward_stats['wardskilled'] / ward_stats['games_played']
ward_stats['controlward_rate'] = ward_stats['controlwardsbought'] / ward_stats['games_played']
ward_stats['visionscore_rate'] = ward_stats['visionscore'] / ward_stats['games_played']

ward_stats.to_csv('data/reports/player_wards_stats.csv', index=False)
print(ward_stats.head())
print("Relatório salvo em data/reports/player_wards_stats.csv")
