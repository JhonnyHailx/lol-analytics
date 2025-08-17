import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches WHERE position IN ('top','jng','mid','bot','sup')", conn)
conn.close()

if 'golddiffat10' in df.columns and 'csdiffat10' in df.columns:
    lane_dom = df.groupby('position').agg({
        'golddiffat10': 'mean',
        'csdiffat10': 'mean'
    }).reset_index()
    lane_dom.to_csv('data/reports/lane_dominance_by_role.csv', index=False)
    print(lane_dom.head())
    print("Relatório salvo em data/reports/lane_dominance_by_role.csv")
else:
    print("Colunas golddiffat10/csdiffat10 não presentes.")
