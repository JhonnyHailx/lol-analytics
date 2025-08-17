import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")

# Seleciona somente as linhas "team"
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Métricas importantes para times
team_summary = team_df.groupby("teamname").agg({
    'teamkills': 'sum',
    'dragons': 'sum',
    'barons': 'sum',
    'heralds': 'sum',
    'towers': 'sum',
    'totalgold': 'sum',
    'visionscore': 'sum'
}).reset_index()

# Salva relatório
team_summary.to_csv("data/reports/team_stats_summary.csv", index=False)
print(team_summary.head(10))
print("Relatório salvo em data/reports/team_stats_summary.csv")
