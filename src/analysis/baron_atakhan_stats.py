import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Verifica quais colunas existem
cols = df.columns

agg_dict = {
    'barons': 'sum',
    'firstbaron': 'sum' if 'firstbaron' in cols else lambda x: 0,
    'atakhans': 'sum' if 'atakhans' in cols else lambda x: 0,
    'gamelength': 'mean',
    'result': 'sum'
}

# Remove as que não existem
agg_dict = {k: v for k, v in agg_dict.items() if k in cols}

obj_stats = df.groupby('teamname').agg(agg_dict).reset_index()

# Calcula por partida
games = df.groupby('teamname').size()
obj_stats['games'] = games.values
obj_stats['barons_per_game'] = obj_stats['barons'] / obj_stats['games']
if 'atakhans' in obj_stats.columns:
    obj_stats['atakhans_per_game'] = obj_stats['atakhans'] / obj_stats['games']
obj_stats.to_csv('data/reports/baron_atakhan_stats.csv', index=False)
print(obj_stats.head())
print('Relatório salvo em data/reports/baron_atakhan_stats.csv')
