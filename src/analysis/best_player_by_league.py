import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top', 'jng', 'mid', 'bot', 'sup')",
    conn)
conn.close()

league_stats = player_df.groupby(['league', 'playername']).agg({
    'kills': 'sum',
    'deaths': 'sum',
    'assists': 'sum',
    'damagetochampions': 'sum'
}).reset_index()

# Top player de cada league por kills:
best_by_league = league_stats.sort_values(['league', 'kills'], ascending=[True, False]).groupby('league').head(1)
print("Melhor jogador por league:")
print(best_by_league)
best_by_league.to_csv('data/reports/best_player_by_league.csv', index=False)
print("Relatório salvo em data/reports/best_player_by_league.csv")
