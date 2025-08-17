import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

df['cs_total'] = df['minionkills'] + df['monsterkills']
df['cspm'] = df['cs_total'] / df['gamelength']

cs_summary = df.groupby('playername').agg({
    'cs_total': 'sum',
    'cspm': 'mean',
    'minionkills': 'sum',
    'monsterkills': 'sum'
}).reset_index()
cs_summary['games_played'] = df.groupby('playername').size().values

cs_summary.to_csv('data/reports/player_cs_per_min_summary.csv', index=False)
print(cs_summary.head())
print("Relatório salvo em data/reports/player_cs_per_min_summary.csv")
