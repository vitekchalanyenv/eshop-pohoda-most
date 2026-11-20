# Předání

**Relace:** 2026-11-20 večer (lekce 00 hotová, lekce 01 rozpracovaná, vedeno v chatu s lektorem)

## Kde jsme

- Lekce 00 je hotová: prostředí (uv, pytest), git smyčka, traceback cvičení, kontrolní otázky.
- Lekce 01: probrané **pojmy** (XML feed, CSV, kódování). Vítek otevřel oba soubory a sám určil:
  oddělovač `;`, desetinná čárka, CSV je ve Windows-1250 (Notepad dobře, `Get-Content -Encoding utf8` rozbité).
- Krok 1 (specifikace) je **probraný, ale soubor ještě neexistuje**. Návrh je níže.
- Vítek nemá VS Code (příkaz `code` nefunguje), používá Notepad.

## Co udělat dál

1. Vytvořit `docs/spec/01-validace-feedu.md` z návrhu níže. **Vítek ho má projít a upravit po svém**, pak commit `L01: specifikace validace`.
2. Lekce 01, krok 2: `is_valid_ean13` – nejdřív testy (`tests/test_ean.py`), pak funkce v `src/most/validace.py`.
3. Pokračovat kroky 3–7 lekce 01.

## Co Vítek pochopil a co ne (pro vedení lekce)

- Rozumí: KeyError vs. ValueError, oprava vzoru místo konkrétní hodnoty, commit vs. push, kódování (zrcadlový případ UTF-8 / Windows-1250).
- Potřeboval vést: syntaxe `.replace()` (uvozovky u textu), rozdíl terminál × soubor `.py`.
- Při navrhování pravidel měl sklon k **příliš přísným** pravidlům (IMGURL jen `.jpg`, EAN jen prefix 8594, cena bez haléřů). Probrali jsme, proč jsou škodlivá (falešné chyby, prefix GS1 ≠ země původu). Hlídej to i dál.

## Návrh specifikace (z diskuse v lekci, Vítek ho ještě neschválil)

```markdown
# Specifikace: validace feedu a skladového exportu (lekce 01)

## Vstup
- `feed_produkty.xml` – produktový feed e-shopu (UTF-8)
- `sklad_export.csv` – export ze skladu (Windows-1250, oddělovač `;`, desetinná čárka)

## Výstup
Seznam nalezených problémů. Každý problém má: soubor (feed / sklad), kde (číslo položky nebo řádku),
kód produktu (pokud je znám), pole, popis problému.
Program vadné záznamy hlásí, neopravuje. Žádný záznam se tiše nezahodí.

## Pravidla – feed
| Pole | Pravidlo |
|---|---|
| ITEM_ID | povinné, unikátní v celém feedu |
| PRODUCTNAME | nesmí být prázdný |
| PRICE_VAT | číslo větší než 0 (desetinná místa povolena) |
| VAT | jedna z platných sazeb v ČR: 0, 12, 21 |
| EAN | 13 číslic, správná kontrolní číslice (prefix se nekontroluje – dovážené zboží) |
| URL | musí začínat `https://` |
| IMGURL | musí začínat `https://` (přípona se nekontroluje) |
| DELIVERY_DATE | celé číslo ≥ 0 |

## Pravidla – sklad (CSV)
| Pole | Pravidlo |
|---|---|
| řádek | přesně 5 sloupců |
| kod | povinný |
| mnozstvi | celé číslo ≥ 0 |
| cena_nakup | číslo ≥ 0, desetinná čárka |

## Poškozený soubor
Když XML nejde načíst, program nespadne s tracebackem, ale vypíše, že soubor je poškozený, a kde (řádek, sloupec).

## Rozhodnutí
(doplní se v kroku 6 – křížová kontrola feed ↔ sklad)
```

## Otevřené otázky pro Vítka

- (žádné)

## Jak pracovat

- Začni `/navazani`, pak `/lekce`. Konec relace `/predani`.
- Kontrolu, zda program našel všechny chyby v datech, dělá Vítek s lektorem v chatu (klíč není v repu).
