import sqlite3
import pandas as pd

drake_types = ["infernals", "mountains", "clouds", "oceans", "chemtechs", "hextechs"]

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

# Soma dos dragões elementais + elder por time/jogo
df['total_elemental_drakes'] = df[drake_types].sum(axis=1)
df['dragons_total'] = df['total_elemental_drakes'] + df['elders']

# Define a alma do jogo por maior quantidade de elemental no game
soul_per_game = df.groupby('gameid')[drake_types].sum()
soul_type_dict = soul_per_game.apply(lambda row: row.idxmax(), axis=1).to_dict()
df['soul_type'] = df['gameid'].map(soul_type_dict)

# Tem alma se fez 4 elementais
df['has_soul'] = df['total_elemental_drakes'] >= 4

result = df[['gameid', 'teamname', 'total_elemental_drakes', 'elders', 'dragons_total', 'soul_type', 'has_soul']]
result.to_csv('data/reports/dragon_soul_true_logic.csv', index=False)
print(result.head(20).to_string())
print("Relatório salvo em data/reports/dragon_soul_true_logic.csv")
