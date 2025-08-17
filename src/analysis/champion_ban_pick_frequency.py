import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

ban_cols = [f'ban{i}' for i in range(1,6) if f'ban{i}' in df.columns]
bans_melted = df.melt(id_vars=['gameid','teamname'], value_vars=ban_cols, value_name='banned_champion').dropna()
ban_freq = bans_melted['banned_champion'].value_counts().reset_index()
ban_freq.columns = ['champion','ban_count']

pick_cols = [f'pick{i}' for i in range(1,6) if f'pick{i}' in df.columns]
picks_melted = df.melt(id_vars=['gameid','teamname'], value_vars=pick_cols, value_name='picked_champion').dropna()
pick_freq = picks_melted['picked_champion'].value_counts().reset_index()
pick_freq.columns = ['champion','pick_count']

ban_freq.to_csv('data/reports/champion_ban_frequency.csv', index=False)
pick_freq.to_csv('data/reports/champion_pick_frequency.csv', index=False)
print(ban_freq.head())
print(pick_freq.head())
print("Relatórios de bans e picks salvos.")
