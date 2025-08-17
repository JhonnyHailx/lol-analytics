import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

consistency = player_df.groupby('playername').agg({
    'kills': ['mean','std'],
    'deaths': ['mean','std'],
    'damagetochampions': ['mean','std']
}).reset_index()
consistency.columns = ['playername',
                       'mean_kills','std_kills',
                       'mean_deaths','std_deaths',
                       'mean_damage','std_damage']
consistency.to_csv('data/reports/player_consistency_score.csv', index=False)
print(consistency.head())
print("Relatório salvo em data/reports/player_consistency_score.csv")
