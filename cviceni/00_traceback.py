"""Cvičení k lekci 00: čtení tracebacku.

Skript má spočítat cenu bez DPH pro tři produkty. Obsahuje DVĚ chyby.
Neopravuj je naslepo a nedávej je hned AI. Postup je v docs/lekce/00-zaklady.md.

Spuštění:  uv run python cviceni/00_traceback.py
"""

PRODUKTY = [
    {"kod": "KAV-001", "nazev": "Etiopie Yirgacheffe 250 g", "cena_s_dph": "349", "dph": 12},
    {"kod": "KAV-002", "nazev": "Kolumbie Huila 250 g", "cena_s_dph": "329", "dph": 12},
    {"kod": "MLY-001", "nazev": "Ruční mlýnek Timemore C3", "cena_s_dph": "1 890", "dph": 21},
]


def cena_bez_dph(produkt):
    cena = float(produkt["cena_s_dph"].replace(" ", ""))
    sazba = produkt["dph"]
    return round(cena / (1 + sazba / 100), 2)


def main():
    for produkt in PRODUKTY:
        print(f"{produkt['kod']}: {cena_bez_dph(produkt)} Kč bez DPH")


if __name__ == "__main__":
    main()
