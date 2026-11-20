# Slovníček

Pojmy z projektu, vysvětlené na příkladu z e-commerce. Doplňuje se průběžně.

| Pojem | Co to je | Příklad z projektu |
|---|---|---|
| **Feed** | Soubor, kterým e-shop předává seznam produktů jinému systému (srovnávač, marketplace, ERP). Obvykle XML nebo CSV, stahuje se z pevné URL. | `data/vstup/feed_produkty.xml` |
| **XML** | Textový formát se značkami `<NAZEV>hodnota</NAZEV>`. Přísný: jedna chyba (např. neescapovaný znak `&`) a nejde načíst celý soubor. | `<PRICE_VAT>349</PRICE_VAT>` |
| **CSV** | Tabulka jako text, hodnoty oddělené čárkou nebo středníkem. Česká data mívají středník a desetinnou čárku. | `data/vstup/sklad_export.csv` |
| **Kódování (encoding)** | Jak se znaky převádějí na bajty. Dnes standard UTF-8; starší české systémy exportují ve Windows-1250. Špatné kódování = rozsypaný čaj (`KĂˇva`). | CSV ze skladu je ve Windows-1250. |
| **EAN** | Čárový kód produktu, 13 číslic. Poslední číslice je kontrolní, dá se dopočítat ze zbylých dvanácti. | `8594000000017` |
| **Validace** | Kontrola, že data dávají smysl, dřív než s nimi začneme pracovat. | cena není záporná, EAN má správnou kontrolní číslici |
| **Traceback** | Výpis chyby v Pythonu. Čte se **odspodu**: poslední řádek je chyba, nad ní místo, kde vznikla. | lekce 00, cvičení |
| **Test (pytest)** | Kód, který ověřuje jiný kód. Když projde, víš, že věc funguje aspoň v testovaných případech. | `tests/test_smoke.py` |
