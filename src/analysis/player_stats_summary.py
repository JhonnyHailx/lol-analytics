import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")

# Seleciona somente as linhas de jogadores (top, jng, mid, bot, sup)
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top', 'jng', 'mid', 'bot', 'sup')",
    conn)
conn.close()

# Métricas importantes para jogadores
player_summary = player_df.groupby("playername").agg({
    'kills': 'sum',
    'deaths': 'sum',
    'assists': 'sum',
    'damagetochampions': 'sum',
    'dpm': 'mean',
    'visionscore': 'sum',
    'totalgold': 'sum'
}).reset_index()

# Salva relatório
player_summary.to_csv("data/reports/player_stats_summary.csv", index=False)
print(player_summary.head(10))
print("Relatório salvo em data/reports/player_stats_summary.csv")
