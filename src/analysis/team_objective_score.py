import sqlite3
import pandas as pd

drake_types = ['infernals', 'mountains', 'clouds', 'oceans', 'chemtechs', 'hextechs', 'elders']

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

team_df['dragons_total'] = team_df[drake_types].sum(axis=1)

team_df['objective_score'] = (
    team_df['dragons_total']*2 +
    team_df['barons']*3 +
    team_df['heralds'] +
    team_df['towers']*1.5 +
    team_df['firstdragon'] +
    team_df['firstbaron'] +
    team_df['firstherald']
)

score_summary = team_df.groupby('teamname').agg({
    'objective_score':'mean',
    'result':'sum'
}).reset_index()

score_summary.to_csv('data/reports/team_objective_score.csv',index=False)
print(score_summary.sort_values('objective_score',ascending=False).head())
print('Relatório salvo em data/reports/team_objective_score.csv')
