import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position = 'team'", 
    conn
)
conn.close()

cols = [
    'firstmidtower',
    'firsttothreetowers',
    'turretplates',
    'opp_turretplates'
]

# Só mantém as colunas presentes
cols = [c for c in cols if c in df.columns]

turret_plate_stats = df.groupby('teamname')[cols].mean().reset_index()
turret_plate_stats['plate_diff'] = turret_plate_stats['turretplates'] - turret_plate_stats['opp_turretplates']

turret_plate_stats.to_csv('data/reports/team_turret_plate_stats.csv', index=False)
print(turret_plate_stats.head(10))
print("Relatório salvo em data/reports/team_turret_plate_stats.csv")
