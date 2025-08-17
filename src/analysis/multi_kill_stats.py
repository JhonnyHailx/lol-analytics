import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

multi_stats = df.groupby('playername').agg({
    'doublekills':'sum',
    'triplekills':'sum',
    'quadrakills':'sum',
    'pentakills':'sum'
}).reset_index()
multi_stats.to_csv('data/reports/player_multi_kill_stats.csv',index=False)
print(multi_stats.sort_values('pentakills',ascending=False).head())
print("Relatório salvo em data/reports/player_multi_kill_stats.csv")
