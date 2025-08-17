import sqlite3
import pandas as pd

# Conectando à base
conn = sqlite3.connect("data/curated/historical_matches.db")

# Pegando apenas as linhas de equipes!
query = """
SELECT gameid, teamname, result
FROM matches
WHERE position = 'team'
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Sumarizando número de partidas e vitórias por confronto por time
bo_summary = df.groupby(['gameid', 'teamname']).agg(
    partidas=('result', 'count'),  # Quantidade de jogos (por time/confronto)
    vitorias=('result', 'sum')     # Soma das vitórias dentro do gameid para cada time
).reset_index()

# Definindo tipo de BO pelo número de partidas
def bo_type(row):
    if row['partidas'] == 1:
        return "BO1"
    elif row['partidas'] == 3:
        return "BO3"
    elif row['partidas'] == 5:
        return "BO5"
    else:
        return f"BO{row['partidas']}"

bo_summary['tipo_BO'] = bo_summary.apply(bo_type, axis=1)
bo_summary['vencedor'] = bo_summary['vitorias'] == bo_summary['partidas'] // 2 + 1

# Gerando relatório CSV para consulta/protocolo
bo_summary.to_csv("data/reports/bo_match_summary.csv", index=False)
print(bo_summary.head(20))
print("Relatório salvo em data/reports/bo_match_summary.csv")
