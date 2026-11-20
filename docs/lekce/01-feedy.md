# Lekce 01 – Feedy: XML, CSV, kódování a validace dat

**Čas:** 5–10 hodin · **Výsledek:** program, který načte produktový feed a skladový export,
zkontroluje je a vypíše srozumitelný report chyb.

## Situace

Nový klient, e-shop **Pražírna Plus** (káva, čaj, příslušenství), přechází na nový systém.
Poslal ti dva soubory:

- `data/vstup/feed_produkty.xml` – produktový feed z e-shopu (zjednodušený formát ve stylu Heureky),
- `data/vstup/sklad_export.csv` – export zásob z jejich starého skladového programu.

Než cokoli napojíš, musíš vědět, jestli jsou data v pořádku. V praxi implementátora je to první krok
u každého klienta: **data od klienta nikdy nejsou čistá.** Klient ti to ale neřekne, protože o tom neví.

V souborech jsou schované chyby. Kolik jich je, ti neřeknu. Tvůj program je má najít všechny.
Výsledek pak zkontrolujeme spolu v chatu.

---

## 1. Pojmy

### XML feed

```xml
<SHOP>
  <SHOPITEM>
    <ITEM_ID>KAV-001</ITEM_ID>
    <PRODUCTNAME>Etiopie Yirgacheffe 250 g</PRODUCTNAME>
    <PRICE_VAT>349</PRICE_VAT>
    ...
  </SHOPITEM>
</SHOP>
```

- `SHOP` je kořen, každý `SHOPITEM` je jeden produkt, uvnitř jsou pole.
- XML je **přísné**: když je soubor poškozený (třeba znak `&` místo `&amp;`), nejde načíst vůbec.
  Proto se XML čte knihovnou (v Pythonu `xml.etree.ElementTree`), ne ručním hledáním textu.
- Pole v našem feedu: `ITEM_ID`, `PRODUCTNAME`, `URL`, `IMGURL`, `PRICE_VAT` (cena s DPH),
  `VAT` (sazba DPH v %), `EAN`, `MANUFACTURER`, `CATEGORYTEXT`, `DELIVERY_DATE` (dny do expedice).

### CSV ze starého systému

- Oddělovač je **středník**, protože české Excely a staré systémy používají čárku jako desetinnou.
- Čísla jsou s **desetinnou čárkou**: `142,50`. `float("142,50")` v Pythonu spadne.
- Kódování je **Windows-1250**, ne UTF-8. Když ho otevřeš špatně, z „Keňa“ bude nesmysl, nebo program spadne.
  Kódování se z obsahu souboru spolehlivě nepozná, musíš ho vědět (zeptat se klienta) nebo ověřit.
- Pro čtení použij modul `csv`, ne `split(";")`. Proč, zjistíš sám.

### Pravidla platnosti (co je „správný“ produkt)

Tohle je **zadání od tebe jako implementátora**. Sepiš je ve specifikaci (viz níže). Pro začátek:

| Pole | Pravidlo |
|---|---|
| `ITEM_ID` | povinné, unikátní v celém feedu |
| `PRODUCTNAME` | povinné, neprázdné |
| `PRICE_VAT` | číslo, větší než 0 |
| `VAT` | jedna z platných sazeb DPH v ČR: 0, 12, 21 |
| `EAN` | 13 číslic, správná kontrolní číslice |
| CSV `kod` | povinný |
| CSV `mnozstvi` | celé číslo ≥ 0 |
| CSV řádek | přesně 5 sloupců |
| feed ↔ sklad | ke každému kódu ze skladu existuje produkt ve feedu a naopak (s výjimkami, které si zdůvodníš) |

**Kontrolní číslice EAN-13:** vezmi prvních 12 číslic. Číslice na lichých pozicích (1., 3., …) násob 1,
na sudých 3. Sečti. Kontrolní číslice je to, co chybí do nejbližšího vyššího násobku 10
(když je součet už násobkem 10, je to 0).
Příklad: `859400000001?` → součet 47 → do 50 chybí **3** → `8594000000013`.

---

## 2. Stavba

Postup **specifikace → testy → kód**, po malých krocích. Claude Code ti pomáhá, ale ty rozhoduješ a spouštíš.

### Krok 1: Specifikace (bez kódu)

Vytvoř `docs/spec/01-validace-feedu.md` a sepiš (stačí odrážky):

- co program dostane na vstupu a co vrátí,
- seznam pravidel (můžeš převzít tabulku výše a doplnit, co tě napadne ze zkušenosti s Karatem),
- jak bude vypadat jedna nalezená chyba (např. `soubor, řádek/položka, kód produktu, pole, popis`),
- co se stane, když XML nejde vůbec načíst.

> Tip: nech Claude Code navrhnout první verzi a pak ji **přepiš po svém**. Co v ní chybělo nebo bylo navíc?
> Pokud něco podstatného, zapiš to do `docs/AI_CHYBY.md`.

### Krok 2: EAN (první funkce s testy)

1. V `tests/test_ean.py` napiš testy pro funkci `is_valid_ean13(ean: str) -> bool`:
   platný EAN, špatná kontrolní číslice, krátký, s písmenem, prázdný.
2. Spusť `uv run pytest`. Testy spadnou, protože funkce ještě neexistuje. **To je správně.**
3. Teprve teď napiš funkci v `src/most/validace.py` (sám, nebo s Claude Code).
4. Spusť testy, dokud neprojdou.

### Krok 3: Čtení XML

Funkce `load_feed(path) -> list[dict]`: načte feed a vrátí seznam produktů jako slovníky.
Zatím nic nekontroluje, jen čte. Test: z našeho feedu vrátí správný počet položek a první má `ITEM_ID == "KAV-001"`.

### Krok 4: Validace feedu

Funkce `validate_feed(products) -> list[Issue]`. `Issue` je jedna nalezená chyba (navrhni si ji ve specifikaci;
dobrá volba je `dataclass`). Každé pravidlo = vlastní test na malém ručně vytvořeném vstupu, ne na celém souboru.

### Krok 5: Čtení a validace CSV

Funkce `load_stock(path)` a `validate_stock(rows)`. Pozor na kódování, oddělovač a desetinnou čárku.
Vadný řádek nesmí shodit celý program. Musí skončit v reportu.

### Krok 6: Křížová kontrola feed ↔ sklad

Funkce `cross_check(products, stock) -> list[Issue]`. Tady narazíš na situace, které nejsou černobílé.
Rozhodni, co je chyba a co pravidlo, a **rozhodnutí zapiš do specifikace s důvodem**.

### Krok 7: Spouštění z příkazové řádky

`uv run python -m most.feed data/vstup/feed_produkty.xml data/vstup/sklad_export.csv`

Vypíše přehledný report: počet produktů, počet chyb podle typu, seznam chyb.
Zároveň uloží report do `data/vystup/report_feed.csv` (UTF-8, středník), aby šel otevřít v Excelu.

---

## 3. Rozbij to

1. Spusť program na `data/vstup/feed_rozbity.xml`. Co se stane? Program **nesmí spadnout s tracebackem**:
   musí srozumitelně říct, že soubor je poškozený, a **kde** (řádek a sloupec). Najdi příčinu v souboru
   (nespravuj ho, jen ji popiš) a napiš na tuhle situaci test.
2. Zkus načíst CSV jako UTF-8 místo Windows-1250. Jak se to projeví? Jak bys v programu poznal, že klient
   příště pošle soubor v jiném kódování? (Stačí návrh, implementace je bonus.)

---

## 4. Hotovo, když

- [ ] `docs/spec/01-validace-feedu.md` existuje a obsahuje i tvoje rozhodnutí z kroku 6,
- [ ] každé pravidlo má aspoň jeden test a `uv run pytest` projde,
- [ ] program na datech klienta najde všechny chyby (ověříme spolu v chatu),
- [ ] rozbitý feed nespadne s tracebackem,
- [ ] v `docs/AI_CHYBY.md` je aspoň jeden řádek, nebo umíš říct, proč AI v téhle lekci nechybovala,
- [ ] umíš odpovědět na kontrolní otázky.

### Kontrolní otázky

1. Proč nečteme CSV přes `line.split(";")`? Ukaž na konkrétním řádku z našich dat.
2. Jak poznáš, že soubor má špatné kódování, a proč se to nedá spolehlivě poznat automaticky?
3. Proč program vadné záznamy **hlásí**, a ne tiše opravuje (např. „1 290,00“ → 1290)? Kdy by tichá oprava byla v pořádku?
4. Ve feedu jsou dvě položky se stejným `ITEM_ID`. Co by se stalo, kdyby se takový feed poslal do skladu nebo ERP bez kontroly?
5. Dárkový poukaz není ve skladu. Chyba, nebo ne? Jak jsi to vyřešil a proč?
6. Kdyby klient poslal 50 000 produktů místo 21, co by se v tvém řešení muselo změnit (a co ne)?
