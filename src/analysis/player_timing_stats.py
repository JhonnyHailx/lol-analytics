import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query(
    "SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", 
    conn
)
conn.close()

timing_cols = [
    # 10min
    "goldat10","xpat10","csat10","opp_goldat10","opp_xpat10","opp_csat10",
    "golddiffat10","xpdiffat10","csdiffat10","killsat10","assistsat10","deathsat10",
    "opp_killsat10","opp_assistsat10","opp_deathsat10",
    # 15min
    "goldat15","xpat15","csat15","opp_goldat15","opp_xpat15","opp_csat15",
    "golddiffat15","xpdiffat15","csdiffat15","killsat15","assistsat15","deathsat15",
    "opp_killsat15","opp_assistsat15","opp_deathsat15",
    # 20min
    "goldat20","xpat20","csat20","opp_goldat20","opp_xpat20","opp_csat20",
    "golddiffat20","xpdiffat20","csdiffat20","killsat20","assistsat20","deathsat20",
    "opp_killsat20","opp_assistsat20","opp_deathsat20",
    # 25min
    "goldat25","xpat25","csat25","opp_goldat25","opp_xpat25","opp_csat25",
    "golddiffat25","xpdiffat25","csdiffat25","killsat25","assistsat25","deathsat25",
    "opp_killsat25","opp_assistsat25","opp_deathsat25"
]

# Confirmar só colunas existentes (se alguma não estiver no seu banco, não vai dar erro!)
timing_cols = [c for c in timing_cols if c in df.columns]

timing_summary = df.groupby('playername')[timing_cols].mean().reset_index()
timing_summary.to_csv('data/reports/player_timing_stats.csv', index=False)
print(timing_summary.head(10))
print("Relatório salvo em data/reports/player_timing_stats.csv")
