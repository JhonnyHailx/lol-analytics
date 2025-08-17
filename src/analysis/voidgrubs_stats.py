import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

void_stats = team_df.groupby(['teamname']).agg({
    'void_grubs': ['sum', 'mean'],
    'opp_void_grubs': 'sum',
    'result': ['sum', 'count']
}).reset_index()

void_stats.columns = [
    'teamname',
    'void_grubs_sum','void_grubs_avg',
    'opp_void_grubs_sum',
    'wins','games'
]

void_stats['voidgrubs_ratio'] = void_stats['void_grubs_sum'] / (void_stats['void_grubs_sum'] + void_stats['opp_void_grubs_sum']).replace(0, 1)
void_stats['winrate'] = void_stats['wins'] / void_stats['games']

void_stats.to_csv('data/reports/voidgrubs_stats.csv', index=False)
print(void_stats.sort_values('voidgrubs_ratio', ascending=False).head())
print('Relatório salvo em data/reports/voidgrubs_stats.csv')
