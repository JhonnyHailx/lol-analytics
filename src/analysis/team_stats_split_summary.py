import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Agrupando por teamname e split
team_split_summary = team_df.groupby(['teamname', 'split']).agg({
    'teamkills': 'sum',
    'dragons': 'sum',
    'barons': 'sum',
    'heralds': 'sum',
    'towers': 'sum',
    'totalgold': 'sum'
}).reset_index()

team_split_summary.to_csv('data/reports/team_stats_split_summary.csv', index=False)
print(team_split_summary.head(20))
print("Relatório salvo em data/reports/team_stats_split_summary.csv")
