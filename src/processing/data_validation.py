import sqlite3
import pandas as pd

conn = sqlite3.connect("data/curated/historical_matches.db")
df = pd.read_sql_query("SELECT * FROM matches", conn)
conn.close()

# Relatório de nulos por coluna
nulos = df.isnull().sum().sort_values(ascending=False)
print("Quantidade de valores nulos por coluna:")
print(nulos)

# Pequeno resumo por tipo
tipos = df.dtypes
print("\nTipos de dados por coluna:")
print(tipos)

# Contagem de linhas por 'position' (jogador vs time)
print("\nContagem de linhas por tipo de registro (position):")
print(df['position'].value_counts())

# Salvar tudo em um CSV de relatório para registro
df.describe(include='all').to_csv("data/reports/data_profile.csv")
print("\nRelatório estatístico salvo em data/reports/data_profile.csv")
