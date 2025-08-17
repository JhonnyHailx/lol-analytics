import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

h2h = df.groupby(['gameid','teamname','champion']).agg({
    'result': 'sum'
}).reset_index()
h2h_summary = h2h.groupby(['teamname','champion']).agg({
    'result':'sum',
    'gameid':'count'
}).reset_index()
h2h_summary['winrate'] = h2h_summary['result'] / h2h_summary['gameid']
h2h_summary.to_csv('data/reports/h2h_team_champion.csv', index=False)
print(h2h_summary.head())
print("Relatório salvo em data/reports/h2h_team_champion.csv")
