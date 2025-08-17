import sqlite3
import pandas as pd

drake_types = ['infernals', 'mountains', 'clouds', 'oceans', 'chemtechs', 'hextechs', 'elders']

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

team_df['dragons_total'] = team_df[drake_types].sum(axis=1)

team_rank = team_df.groupby('teamname').agg({
    'dragons_total': 'sum',
    'teamkills': 'sum',
    'towers': 'sum',
    'totalgold': 'sum'
}).reset_index().sort_values('dragons_total', ascending=False)

print("Ranking equipes por dragons (elementais + elder):")
print(team_rank.head(10))

team_rank.to_csv('data/reports/team_dragons_ranking.csv', index=False)
print("Relatório salvo em data/reports/team_dragons_ranking.csv")
