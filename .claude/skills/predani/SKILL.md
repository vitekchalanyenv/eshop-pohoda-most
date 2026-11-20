---
name: predani
description: Předání práce na konci relace v projektu eshop-pohoda-most. Použij, když Vítek řekne „předání“, „končíme“, „zapiš a pushni“ nebo spustí /predani. Aktualizuje PROGRESS, HANDOFF a AI_CHYBY, spustí testy, commitne a pushne.
---

# Předání relace

Cíl: další relace (i úplně nová, bez historie konverzace) naváže během minuty. Česky, stručně, jen fakta.

## Postup

1. `git status --short` a `git log --oneline -10`: co se změnilo, co není commitnuté.
2. `uv run pytest -q` (a od lekce 02 i `uv run ruff check .`). Výsledek zapiš přesně.
3. Aktualizuj `docs/PROGRESS.md`: Hotovo (s datem), Rozpracováno, Čeká na Vítka, Otevřené otázky, Známé problémy.
   U lekce rozliš: napsáno / testy prošly / ověřeno na datech / Vítek zodpověděl kontrolní otázky.
4. Projdi relaci: chybovala někde AI (špatný návrh, chybný kód, halucinace o knihovně)?
   Doplň řádek do `docs/AI_CHYBY.md`. Když ne, nic nevymýšlej.
5. Nové pojmy z relace doplň do `docs/SLOVNICEK.md`.
6. Přepiš celý `docs/HANDOFF.md`: datum, Kde jsme (3–6 odrážek), Co udělat dál (očíslovaně),
   Otevřené otázky pro Vítka, Jak pracovat.
7. `git add -A`, commit `Předání: <krátké shrnutí>` s přípisem z pokynů systému, `git push`. Ověř čistý `git status`.
8. Odpověz Vítkovi 3–5 řádky: co je uloženo (hash), další krok, co od něj bude potřeba.

## Pravidla

- Nevymýšlej stav: co neproběhlo, napiš jako neověřené.
- Neměň kód, jen dokumentaci a commit.
