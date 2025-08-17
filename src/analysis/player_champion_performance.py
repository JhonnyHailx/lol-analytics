import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
# Seleciona somente os jogadores
player_df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top', 'jng', 'mid', 'bot', 'sup')",
    conn
)
conn.close()

# Agrupa por jogador + campeão
player_champ_stats = player_df.groupby(['playername', 'champion']).agg({
    'kills': 'sum',
    'deaths': 'sum',
    'assists': 'sum',
    'damagetochampions': 'sum',
    'result': ['sum', 'count']  # soma de vitórias e número total de jogos com o champion
}).reset_index()

# Ajusta os nomes das colunas
player_champ_stats.columns = ['playername', 'champion',
                              'kills', 'deaths', 'assists',
                              'damagetochampions', 'wins', 'games_played']

# Calcula taxa de vitória e outras métricas relevantes
player_champ_stats['winrate'] = player_champ_stats['wins'] / player_champ_stats['games_played']
player_champ_stats['avg_kills'] = player_champ_stats['kills'] / player_champ_stats['games_played']
player_champ_stats['avg_deaths'] = player_champ_stats['deaths'] / player_champ_stats['games_played']
player_champ_stats['avg_assists'] = player_champ_stats['assists'] / player_champ_stats['games_played']
player_champ_stats['avg_damage'] = player_champ_stats['damagetochampions'] / player_champ_stats['games_played']

# Salva o relatório
player_champ_stats.to_csv('data/reports/player_champion_performance.csv', index=False)
print(player_champ_stats.head(20))
print("Relatório salvo em data/reports/player_champion_performance.csv")
