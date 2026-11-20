---
name: lekce
description: Vedení lekce v projektu eshop-pohoda-most. Použij, když Vítek spustí /lekce, řekne „jedem lekci“, „další krok lekce“ nebo „zkoušej mě“. Provede ho aktuální lekcí z docs/lekce/ v režimu učitele.
---

# Vedení lekce

## Postup

1. Zjisti aktuální lekci z `docs/PROGRESS.md` (Rozpracováno) a otevři ji v `docs/lekce/`.
2. Zjisti, kde se v lekci skončilo (PROGRESS, HANDOFF, git log, existující soubory v `docs/spec/`, `tests/`, `src/most/`).
3. Veď Vítka podle částí lekce:
   - **Pojmy:** vysvětli vlastními slovy na příkladu z projektu, ne kopií lekce. Zeptej se, jestli to sedí,
     a nech ho to říct po svém.
   - **Stavba:** po malých krocích, specifikace → testy → kód. Po každém kroku ať Vítek sám spustí testy.
   - **Rozbij to:** jen zadání a nápovědy na požádání. Nikdy neprozraď řešení dopředu.
   - **Kontrolní otázky:** pokládej po jedné, počkej na odpověď, oprav nebo doplň. Neprozrazuj odpovědi předem.
4. Lekce je hotová, až když platí všechny body „Hotovo, když“. Pak zapiš do `PROGRESS.md` a navrhni `/predani`.

## Pravidla

- Drž se pravidel „Režim učitele“ z `CLAUDE.md`.
- Když lekce předpokládá něco, co v repu neplatí (jiný název souboru, jiná verze knihovny), řekni to,
  navrhni úpravu a zapiš rozpor do `PROGRESS.md`.
- V lekci 01 nečti a neuváděj seznam záměrných chyb v datech. Vítek je má najít programem.
  Kontrolu výsledku dělá s lektorem mimo repo.
