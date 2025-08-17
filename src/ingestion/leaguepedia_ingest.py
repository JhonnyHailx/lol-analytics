import pandas as pd
from typing import List
import os

def download_leaguepedia_tables(league_urls: List[str], output_dir: str = "data/bronze"):
    """
    Busca e salva todas as tabelas úteis (picks, bans, match history) de cada URL de liga/tourney na Leaguepedia.
    """
    os.makedirs(output_dir, exist_ok=True)
    keywords = ["Pick", "Ban", "Champion", "Result", "Team", "Player", "Side", "Winner", "Patch", "GameID", "Duration"]
    for url in league_urls:
        print(f"Buscando tabelas de {url}")
        try:
            tables = pd.read_html(url)
            saved = 0
            for i, table in enumerate(tables):
                # Salve só se colunas importantes estiverem presentes
                if any(any(kw.lower() in str(c).lower() for kw in keywords) for c in table.columns):
                    url_base = url.rstrip("/").split("/")[-1]
                    out_path = f"{output_dir}/leaguepedia_{url_base}_table{i}.csv"
                    table.to_csv(out_path, index=False)
                    print(f"Gerou: {out_path}")
                    saved += 1
            if saved == 0:
                print("Nenhuma tabela relevante nesta URL.")
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")

if __name__ == "__main__":
    league_urls = [
        "https://lol.fandom.com/wiki/LCK/2025_Season",
        "https://lol.fandom.com/wiki/LEC/2025_Season",
        "https://lol.fandom.com/wiki/LCS/2025_Season",
        "https://lol.fandom.com/wiki/LPL/2025_Season",
        # Adicione outras ligas ou anos!
    ]
    download_leaguepedia_tables(league_urls)
