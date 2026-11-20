---
name: navazani
description: Rychlé navázání na práci na začátku nové relace v projektu eshop-pohoda-most. Použij, když Vítek řekne „navaž“, „pokračujeme“, „kde jsme skončili“ nebo spustí /navazani. Načte předání, stav a aktuální lekci a navrhne další krok.
---

# Navázání relace

Cíl: za minutu vědět, kde projekt je, a navrhnout další krok. Nečti celý repozitář.

## Postup

1. Přečti (`CLAUDE.md` už máš v kontextu):
   - `docs/HANDOFF.md` (celý),
   - `docs/PROGRESS.md` (Rozpracováno, Čeká na Vítka, Otevřené otázky, Známé problémy),
   - aktuální lekci v `docs/lekce/` jen v části, kde se skončilo.
2. Git: `git status --short`, `git log --oneline -5`, `git fetch` a porovnání s `origin/main`.
3. Spusť `uv run pytest -q` a zapamatuj si výsledek (tohle jediné spouštíš sám).
4. Odpověz Vítkovi česky, do 8 řádků:
   - kde jsme (2–3 body),
   - stav testů,
   - navržený další krok (první bod z „Co udělat dál“),
   - otevřené otázky.
   Pak počkej na pokyn.

## Pravidla

- Když si `HANDOFF.md` a `PROGRESS.md` odporují, platí novější záznam; rozpor zmiň.
