import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top', 'jng', 'mid', 'bot', 'sup')",
    conn
)
conn.close()

# Group by playername and position, calc total kills, assists, damage
role_stats = player_df.groupby(['position', 'playername']).agg({
    'kills': 'sum',
    'deaths': 'sum',
    'assists': 'sum',
    'damagetochampions': 'sum'
}).reset_index()

# RANK: cria ranking de melhores jogadores por posição (exemplo: maior kills)
best_by_kills = role_stats.sort_values(['position', 'kills'], ascending=[True, False]).groupby('position').head(1)
print("Melhor jogador por role (por kills):")
print(best_by_kills)
best_by_kills.to_csv('data/reports/best_player_by_role.csv', index=False)
print("Relatório salvo em data/reports/best_player_by_role.csv")
