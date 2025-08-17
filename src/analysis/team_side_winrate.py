import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

side_win = df.groupby('side').agg({
    'result': ['sum','count']
}).reset_index()
side_win.columns = ['side','wins','total_games']
side_win['winrate'] = side_win['wins'] / side_win['total_games']
side_win.to_csv('data/reports/team_side_winrate.csv', index=False)
print(side_win)
print("Relatório salvo em data/reports/team_side_winrate.csv")
