import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top', 'jng', 'mid', 'bot', 'sup')",
    conn)
conn.close()

# Cria "score" personalizado (ajuste conforme seu critério!)
player_df['score'] = player_df['kills'] + player_df['assists'] + player_df['damagetochampions'] / 1000

overall_stats = player_df.groupby('playername').agg({
    'score': 'sum',
    'kills': 'sum',
    'deaths': 'sum',
    'assists': 'sum',
    'damagetochampions': 'sum'
}).reset_index().sort_values('score', ascending=False)
print("Ranking geral dos melhores jogadores (score):")
print(overall_stats.head(10))
overall_stats.to_csv('data/reports/best_player_overall.csv', index=False)
print("Relatório salvo em data/reports/best_player_overall.csv")
