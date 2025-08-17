import sqlite3
import pandas as pd

drake_types = ['infernals','mountains','clouds','oceans','chemtechs','hextechs']

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Soma elementais por time/game
df['total_elemental_drakes'] = df[drake_types].sum(axis=1)

# Alma é o elemental com maior soma por partida
soul_per_game = df.groupby('gameid')[drake_types].sum()
soul_type_dict = soul_per_game.apply(lambda row: row.idxmax(), axis=1).to_dict()
df['soul_type'] = df['gameid'].map(soul_type_dict)

df['has_soul'] = df['total_elemental_drakes'] >= 4
df['elder_spawned'] = df['elders'] > 0

soul_stats = df.groupby('teamname').agg({
    'has_soul': 'sum',
    'soul_type': lambda x: x.value_counts().index[0] if any(x != 'none') else 'none',
    'elder_spawned': 'sum',
    'elders': 'sum',
    'result': 'sum',
    'total_elemental_drakes': 'sum'
}).reset_index()

soul_stats['games'] = df.groupby('teamname').size().values
soul_stats.to_csv('data/reports/soul_dragons_stats.csv', index=False)
print(soul_stats.head())
print('Relatório salvo em data/reports/soul_dragons_stats.csv')
