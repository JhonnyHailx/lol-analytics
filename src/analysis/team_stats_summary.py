import sqlite3
import pandas as pd

drake_types = ['infernals', 'mountains', 'clouds', 'oceans', 'chemtechs', 'hextechs', 'elders']

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

team_df['dragons_total'] = team_df[drake_types].sum(axis=1)

team_summary = team_df.groupby("teamname").agg({
    'teamkills': 'sum',
    'dragons_total': 'sum',
    'barons': 'sum',
    'heralds': 'sum',
    'towers': 'sum',
    'totalgold': 'sum',
    'visionscore': 'sum'
}).reset_index()

team_summary.to_csv("data/reports/team_stats_summary.csv", index=False)
print(team_summary.head(10))
print("Relatório salvo em data/reports/team_stats_summary.csv")
