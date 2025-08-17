import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

if 'opp_totalgold' in df.columns:
    df['gold_diff'] = df['totalgold'] - df['opp_totalgold']
    champ_gold_diff = df.groupby(['playername','champion']).agg({
        'gold_diff':'mean',
        'totalgold':'mean'
    }).reset_index()
    champ_gold_diff['games_played'] = df.groupby(['playername','champion']).size().values
    champ_gold_diff.to_csv('data/reports/player_gold_diff_by_champion.csv', index=False)
    print(champ_gold_diff.head())
    print("Relatório salvo em data/reports/player_gold_diff_by_champion.csv")
else:
    print("Campo 'opp_totalgold' não existe. Adicione ou revise para cálculo correto.")
