import sqlite3
import pandas as pd

drake_types = ['infernals','mountains','clouds','oceans','chemtechs','hextechs','elders']

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

team_df['dragons_total'] = team_df[drake_types].sum(axis=1)

drake_stats = team_df.groupby('teamname').agg({
    'infernals': 'sum',
    'mountains': 'sum',
    'clouds': 'sum',
    'oceans': 'sum',
    'chemtechs': 'sum',
    'hextechs': 'sum',
    'elders': 'sum',
    'dragons_total': 'sum',
    'result': ['sum', 'count']
}).reset_index()

drake_stats.columns = [
    'teamname',
    'infernals','mountains','clouds','oceans',
    'chemtechs','hextechs','elders','dragons_total',
    'wins','games'
]
# Taxa de drake por vitória
for key in ['infernals','mountains','clouds','oceans','chemtechs','hextechs','elders','dragons_total']:
    drake_stats[f'{key}_per_win'] = drake_stats[key]/drake_stats['wins'].replace(0,1)

drake_stats.to_csv('data/reports/drake_stats_by_team.csv',index=False)
print(drake_stats.sort_values('elders',ascending=False).head())
print('Relatório salvo em data/reports/drake_stats_by_team.csv')
