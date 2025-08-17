import requests
import pandas as pd
import os

def get_patch_champion_and_item_data(patch):
    """
    Baixa e processa dados dos campeões e itens do patch especificado via Data Dragon.
    Salva arquivos em: data/external/patch_<version>/
    Args:
        patch: str, versão do patch (ex: '25.16.1')
    """
    # URLs do Data Dragon com dados em inglês, troque o idioma se quiser (ex: 'pt_BR')
    champ_url = f"https://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/champion.json"
    item_url = f"https://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/item.json"

    print(f"Baixando dados do patch {patch}...")
    # Baixa dados dos campeões
    champ_data = requests.get(champ_url).json()["data"]
    champ_list = []
    for cname, c in champ_data.items():
        champ_list.append({
            "champion": cname,
            "title": c.get("title", ""),
            "tags": ",".join(c.get("tags", [])),  # Mage, Marksman, etc.
            "attackrange": c["stats"].get("attackrange", None),
            "difficulty": c["info"].get("difficulty", None),
            "attack": c["info"].get("attack", None),
            "defense": c["info"].get("defense", None),
            "magic": c["info"].get("magic", None),
            "hp_base": c["stats"].get("hp", None),
            "ad_base": c["stats"].get("attackdamage", None),
            "ap_base": c["stats"].get("spellblock", None),
            "movespeed": c["stats"].get("movespeed", None),
            "role": ",".join(c.get("tags", []))
            # Adicione outros stats se quiser maior granularidade
        })
    df_champs = pd.DataFrame(champ_list)

    # Baixa dados dos itens
    item_data = requests.get(item_url).json()["data"]
    item_list = []
    for iid, itm in item_data.items():
        item_list.append({
            "itemId": iid,
            "name": itm.get("name", ""),
            "goldBase": itm.get("gold", {}).get("base", ""),
            "goldTotal": itm.get("gold", {}).get("total", ""),
            "purchasable": itm.get("gold", {}).get("purchasable", ""),
            "description": itm.get("description", ""),
            "stats": itm.get("stats", {}),
            # Adicione mais campos se necessário (ex: tags, effects)
        })
    df_items = pd.DataFrame(item_list)

    # Salvar como CSV para cada patch
    outdir = f"data/external/patch_{patch.replace('.', '_')}"
    os.makedirs(outdir, exist_ok=True)
    df_champs.to_csv(f"{outdir}/champions.csv", index=False)
    df_items.to_csv(f"{outdir}/items.csv", index=False)
    print(f"Gerados os arquivos: {outdir}/champions.csv e {outdir}/items.csv\n")

if __name__ == "__main__":
    get_patch_champion_and_item_data("15.16.1") # Atual (coloque a versão exata usada pelas ligas principais)
    get_patch_champion_and_item_data("15.15.1") # Anterior, para ligas que ainda jogam no patch anterior
