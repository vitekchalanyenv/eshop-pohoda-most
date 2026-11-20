# Plán projektu

Tempo: 5–10 hodin týdně. Každý týden = jedna lekce v `docs/lekce/`.

Každá lekce má čtyři části:
1. **Pojmy:** krátké vysvětlení na příkladu z e-commerce.
2. **Stavba:** specifikace → testy → kód, s Claude Code.
3. **Rozbij to:** záměrná chyba, kterou Vítek najde a opraví sám (AI jen napovídá).
4. **Hotovo, když:** testy projdou a Vítek umí krok vysvětlit vlastními slovy (kontrolní otázky na konci lekce).

| Týden | Lekce | Co vznikne | Co se naučíš |
|---|---|---|---|
| 0 | `00-zaklady` | prostředí, git, první test | uv, git, pytest, čtení tracebacku |
| 1 | `01-feedy` | validátor produktového feedu (XML) a skladového exportu (CSV) | XML, CSV, kódování, validace dat, report chyb |
| 2 | `02-api` | fake e-shop API (FastAPI) + klient stahující objednávky | REST, JSON, HTTP kódy, tokeny, stránkování, retry |
| 3 | `03-webhooky` | příjem objednávek přes webhook | webhooky, podpis HMAC, idempotence, logování |
| 4 | `04-pohoda` | mapování polí a export objednávek do Pohoda XML | mapovací konfigurace, AI návrh mapování + kontrola, XSD validace |
| 5 | `05-sftp` | odeslání na SFTP, plánované běhy, stav v SQLite | SFTP, Docker, plánovač, SQLite |
| 6 | `06-mcp` | MCP server pro dohledání a znovuodeslání objednávek | MCP, nástroje pro agenta, bezpečná oprávnění |
| 7 | `07-portfolio` | anglický README, technické zadání, diagram, video | prezentace práce, psaní zadání pro vývojáře |

**Milník pro přihlášky:** po týdnu 4 je projekt použitelný jako odkaz do přihlášky (Base.com).

Lekce 02+ se píšou až po dokončení předchozí, aby navazovaly na to, co opravdu vzniklo.
