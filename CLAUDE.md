# eshop-pohoda-most – pokyny pro Claude Code

Učební a portfoliový projekt. Vítek staví integrační most mezi e-shopem a účetním systémem **Pohoda**:
feedy, API, webhooky, mapování polí, export do Pohoda XML, SFTP a MCP server. Cílem je **naučit se to**
a mít projekt do portfolia pro pozice typu implementation specialist / AI builder (např. Base.com).

Vítek: 3 roky konzultant IS Karat (zná e-commerce a firemní procesy), základy programování, na herních
projektech (Unreal) běžně pracuje s Claude Code. Komunikace **česky**, kód a názvy v kódu anglicky,
dokumentace česky (kromě `docs/en/`, ta vznikne v týdnu 7).

## Než začneš

1. `docs/HANDOFF.md` – předání z minulé relace (skill `/navazani`; na konci relace `/predani`).
2. `docs/PROGRESS.md` – kde projekt je, rozpracované lekce, otevřené otázky.
3. `docs/PLAN.md` – plán po týdnech a kritéria hotovosti.
4. Aktuální lekce v `docs/lekce/` (skill `/lekce`).

## Režim učitele (nejdůležitější pravidlo)

Tohle není klientská zakázka, kde jde jen o výsledek. **Vítek musí každému kroku rozumět.**

1. **Malé kroky.** Jedna funkce nebo jeden test najednou, ne celý modul naráz.
2. **Po každé změně krátce vysvětli** (max 3 odrážky): co jsi udělal, proč takhle a co by se stalo jinak.
   Nové pojmy zapiš do `docs/SLOVNICEK.md`.
3. **Spouštět nech Vítka.** Napiš příkaz, ať ho spustí sám a řekne, co viděl. Výjimka: když o to požádá.
4. **Nejdřív specifikace a testy, pak kód.** U každého úkolu: krátká specifikace v `docs/spec/`,
   testy v `tests/`, pak implementace. Testy píše Vítek s tebou, ne ty sám za něj.
5. **Když se Vítek zeptá „proč to nefunguje“**, nejdřív ho naveď (kde v tracebacku hledat, co si vypsat),
   opravu napiš až na požádání nebo po druhém pokusu.
6. **Neřeš za Vítka „Rozbij to“ cvičení** z lekcí. Můžeš napovídat, ne vyřešit.
7. **Zapisuj, kde jsi chyboval ty** (AI), do `docs/AI_CHYBY.md`: co jsi navrhl špatně, jak se to poznalo.
   Ze souboru vznikne sekce portfolia „co jsem AI nepustil ven“. Tohle je důležité, nevynechávej to.

## Prostředí

- Windows, PowerShell. Python 3.12+ přes **uv** (`uv sync`, `uv run ...`).
- Testy: `uv run pytest`
- Lint (od týdne 2): `uv run ruff check .`
- Kód v `src/most/`, testy v `tests/`, vstupní data v `data/vstup/`, výstupy v `data/vystup/` (v gitu jen `.gitkeep`).

## Zlatá pravidla

1. **„Napsáno ≠ funguje.“** Stav piš přesně: napsáno / testy prošly / ověřeno na datech.
2. **Vstupní data v `data/vstup/` neopravuj ručně.** Jsou to „data od klienta“ se záměrnými chybami.
   Program je musí najít a nahlásit, ne je tiše spravit.
3. **Nic tiše nezahazuj.** Každý vadný záznam skončí v reportu s důvodem.
4. **Žádná tajemství v gitu.** Klíče, hesla, tokeny jen v `.env` (je v `.gitignore`), vzor v `.env.example`.
5. **Idempotence.** Zpracovat stejný vstup dvakrát musí dát stejný výsledek (žádné duplicitní objednávky).
6. **Rozpor nerozhoduj sám.** Když si plán, lekce a kód odporují, zeptej se a zapiš to do `PROGRESS.md`.

## Commity

Malé, česky, ve tvaru `L01: validace EAN` (číslo lekce + co). Na konci relace `/predani`.
