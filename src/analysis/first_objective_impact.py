import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
team_df = pd.read_sql_query("SELECT * FROM matches WHERE position = 'team'", conn)
conn.close()

def winrate_with_first(df, obj):
    if obj not in df.columns:
        print(f"Coluna '{obj}' não existe!")
        return 0, 0
    subset = df[df[obj] == 1]
    winrate = subset['result'].sum() / len(subset) if len(subset) > 0 else 0
    return winrate, len(subset)

fd_winrate, fd_count = winrate_with_first(team_df, 'firstdragon')
fb_winrate, fb_count = winrate_with_first(team_df, 'firstbaron')
fh_winrate, fh_count = winrate_with_first(team_df, 'firstherald')

print(f"Winrate com First Dragon: {fd_winrate:.2%} ({fd_count} jogos)")
print(f"Winrate com First Baron: {fb_winrate:.2%} ({fb_count} jogos)")
print(f"Winrate com First Herald: {fh_winrate:.2%} ({fh_count} jogos)")
