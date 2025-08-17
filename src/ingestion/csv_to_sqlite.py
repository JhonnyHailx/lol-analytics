import pandas as pd
import sqlite3
from pathlib import Path

# Path para o CSV e para o banco SQLite
csv_file = Path("data/raw/historical_matches.csv")
sqlite_db = Path("data/curated/historical_matches.db")
table_name = "matches"

# Carregar CSV com pandas
df = pd.read_csv(csv_file)

# Abrir conexão SQLite
conn = sqlite3.connect(sqlite_db)

# Gravar no banco
df.to_sql(table_name, conn, if_exists="replace", index=False)

print(f"Importação concluída! {len(df)} linhas inseridas em '{sqlite_db}' na tabela '{table_name}'.")
conn.close()
