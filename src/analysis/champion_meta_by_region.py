import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position = 'team'", conn
)
conn.close()

# Picks por liga
pick_cols = [f'pick{i}' for i in range(1,6) if f'pick{i}' in df.columns]
picks_melted = df.melt(id_vars=['league','gameid','teamname'], value_vars=pick_cols, value_name='picked_champion').dropna()
pick_region_freq = picks_melted.groupby(['league','picked_champion']).size().reset_index(name='pick_count')
pick_region_freq = pick_region_freq.sort_values(['league','pick_count'], ascending=[True,False])

# Bans por liga
ban_cols = [f'ban{i}' for i in range(1,6) if f'ban{i}' in df.columns]
bans_melted = df.melt(id_vars=['league','gameid','teamname'], value_vars=ban_cols, value_name='banned_champion').dropna()
ban_region_freq = bans_melted.groupby(['league','banned_champion']).size().reset_index(name='ban_count')
ban_region_freq = ban_region_freq.sort_values(['league','ban_count'], ascending=[True,False])

pick_region_freq.to_csv('data/reports/champion_picks_by_region.csv', index=False)
ban_region_freq.to_csv('data/reports/champion_bans_by_region.csv', index=False)

print("Exemplo: TOP PICKS por liga")
for league in pick_region_freq['league'].unique():
    top_picks = pick_region_freq[pick_region_freq['league'] == league].head(5)
    print(f"\n{league}:")
    print(top_picks)

print("\nExemplo: TOP BANS por liga")
for league in ban_region_freq['league'].unique():
    top_bans = ban_region_freq[ban_region_freq['league'] == league].head(5)
    print(f"\n{league}:")
    print(top_bans)

print("Relatórios salvos: champion_picks_by_region.csv | champion_bans_by_region.csv")
