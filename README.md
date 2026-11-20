# eshop-pohoda-most

Integrační most mezi e-shopem a účetním systémem **Pohoda**, postavený v Pythonu s pomocí AI agentů.

Simuluje práci implementátora e-commerce systémů: načte a zkontroluje produktový feed, přijímá objednávky
přes API a webhooky, namapuje pole e-shopu na Pohodu, vyexportuje objednávky do Pohoda XML, pošle je na SFTP
a přes MCP server umožní AI agentovi dohledat, proč se objednávka nepropsala.

> Projekt je rozpracovaný. Stav je v [`docs/PROGRESS.md`](docs/PROGRESS.md), plán v [`docs/PLAN.md`](docs/PLAN.md).
> Anglický README vznikne v týdnu 7.

## Jak to spustit

Potřebuješ [uv](https://docs.astral.sh/uv/) (stará se o Python i knihovny).

```powershell
uv sync           # nainstaluje Python a závislosti
uv run pytest     # spustí testy
```

## Struktura

```
src/most/        kód mostu
tests/           automatické testy
data/vstup/      vstupní data od „klienta“ (se záměrnými chybami, neopravovat ručně)
data/vystup/     výstupy programu (nejsou v gitu)
docs/            plán, postup, lekce, specifikace, slovníček
cviceni/         malá cvičení k lekcím
```
