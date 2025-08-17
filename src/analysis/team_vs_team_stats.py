import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Exemplo: ranking por dragons, teamkills, towers
team_rank = team_df.groupby('teamname').agg({
    'dragons': 'sum',
    'teamkills': 'sum',
    'towers': 'sum',
    'totalgold': 'sum'
}).reset_index().sort_values('dragons', ascending=False)

print("Ranking equipes por dragons:")
print(team_rank.head(10))
team_rank.to_csv('data/reports/team_dragons_ranking.csv', index=False)
print("Relatório salvo em data/reports/team_dragons_ranking.csv")
