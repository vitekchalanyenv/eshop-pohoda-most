# Lekce 00 – Základy: prostředí, git, testy, traceback

**Čas:** 1–3 hodiny · **Výsledek:** funkční prostředí, první commit a umíš číst chybový výpis.

Tahle lekce je krátká a skoro bez kódu. Bez ní by ale každá další stála dvakrát víc času.

---

## 1. Pojmy

**uv** je správce Pythonu a knihoven. Místo „nainstaluj Python, vytvoř virtuální prostředí,
nainstaluj balíčky“ napíšeš `uv sync` a hotovo. Seznam knihoven je v `pyproject.toml`, přesné verze
v `uv.lock`. Díky tomu bude projekt na tvém i cizím počítači fungovat stejně.

**Virtuální prostředí** (`.venv/`) je složka, kam se knihovny instalují jen pro tenhle projekt.
Nepleteš si tak verze mezi projekty. Do gitu nepatří (proto je v `.gitignore`).

**pytest** spouští testy. Test je funkce začínající `test_`, která pomocí `assert` ověří, že
něco platí. Když `assert` neplatí, test spadne a pytest ti ukáže proč.

**Traceback** je výpis chyby. **Čte se odspodu:**
- poslední řádek = **co** se stalo (typ chyby a zpráva),
- řádky nad ním = **kde** to vzniklo (soubor, číslo řádku, kód), od nejhlubšího volání nahoru.

Z IS Karat to znáš: chybová hláška při importu, ze které musíš poznat, jestli je vadný soubor,
nastavení, nebo program. Tady je to stejné, jen detailnější.

---

## 2. Stavba

### 2.1 Instalace uv (jednorázově)

V PowerShellu:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Zavři a znovu otevři terminál a ověř: `uv --version`.

### 2.2 Stažení projektu a první spuštění

```powershell
git clone https://github.com/vitekchalanyenv/eshop-pohoda-most.git
cd eshop-pohoda-most
uv sync
uv run pytest
```

Měly by projít **2 testy**. Otevři `tests/test_smoke.py` a přečti si je. Rozumíš, co ověřují?

### 2.3 Vyzkoušej si, jak vypadá spadlý test

1. V `tests/test_smoke.py` změň `"0.1.0"` na `"0.2.0"`.
2. Spusť `uv run pytest` a prohlédni si výpis. Najdi řádek, kde pytest ukazuje obě hodnoty.
3. Vrať změnu zpět a ověř, že testy zase projdou.

### 2.4 Git: první vlastní commit

Do `docs/PROGRESS.md` připiš pod „Hotovo“ řádek, že máš funkční prostředí. Pak:

```powershell
git status          # co se změnilo
git diff            # jak přesně
git add docs/PROGRESS.md
git commit -m "L00: funkční prostředí"
git push
```

Tohle je základní smyčka, kterou budeš dělat pořád: **změna → status → diff → add → commit → push.**
Claude Code ji umí za tebe, ale musíš vědět, co dělá, abys poznal, když udělá něco jiného.

---

## 3. Rozbij to: traceback

Soubor `cviceni/00_traceback.py` má spočítat cenu bez DPH pro tři produkty. Obsahuje **dvě chyby**.

**Pravidla:** neopravuj naslepo a nedávej to hned AI. Postup:

1. Spusť: `uv run python cviceni/00_traceback.py`
2. Přečti traceback **odspodu**. Napiš si (klidně do poznámky):
   - jaký je typ chyby,
   - na kterém řádku vznikla,
   - jakou hodnotu program čekal a co dostal.
3. Oprav **první** chybu. Spusť znovu. Objeví se druhá.
4. U druhé chyby se zamysli: je chyba v programu, nebo v datech? A co by bylo správné řešení,
   kdyby takových dat byly tisíce a přišly od klienta?
5. Teprve teď se můžeš zeptat Claude Code, jestli tvoje oprava dává smysl.

> Druhá chyba je ochutnávka lekce 01. Česká data jsou plná takových „drobností“.

---

## 4. Hotovo, když

- [ ] `uv run pytest` projde,
- [ ] máš na GitHubu vlastní commit `L00: …`,
- [ ] obě chyby v cvičení máš opravené a skript vypíše tři ceny,
- [ ] umíš odpovědět na kontrolní otázky.

### Kontrolní otázky

1. Proč `.venv/` nepatří do gitu, ale `uv.lock` ano?
2. Na kterém řádku tracebacku najdeš, **co** se pokazilo, a na kterém, **kde**?
3. Co je rozdíl mezi `git commit` a `git push`?
4. Ve cvičení byla jedna chyba v kódu a jedna „v datech“. Jak bys tu druhou řešil, kdyby data posílal
   klient každý den a nemohl jsi je ručně opravovat?

Odpovědi řekni Claude Code přes `/lekce` („zkoušej mě“), nebo je napiš lektorovi do chatu.
