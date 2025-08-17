import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches", conn)
conn.close()

# Relatório de nulos por coluna
nulos = df.isnull().sum().sort_values(ascending=False)

# Opcional: criar um dataframe dos campos mais críticos
nulos_df = pd.DataFrame({"column": nulos.index, "missing": nulos.values})
nulos_df['pct_missing'] = (nulos_df['missing'] / len(df)) * 100

print("Top 10 colunas com maior % de nulos:")
print(nulos_df.head(10))

# Salve relatório CSV para consultar depois
nulos_df.to_csv('data/reports/missing_data_report.csv', index=False)
print("Relatório de ausências salvo em data/reports/missing_data_report.csv")
