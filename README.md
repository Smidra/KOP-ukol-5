KOP - Úkol 5
============
## TODO pro úkol 5
- ~~GitHub repo~~
- ~~Pochop o co jde v zadání~~
- ~~Pochop zápis instancí~~ 
- Navrhni stavový prostor a operace 
- Navrhni pro to třídu stav ideálně fungující s tvojí implementací simulovaného ochlazování 
- Uprav načítání ze souboru instancí 
- Uprav skriptování 
- Změř a vyzkoušej heuristiku 
- Napiš report s grafy

## Zadání pro úkol 5
**Algoritmus a implementace (5 pt.)**
  - Byly použity techniky (algoritmy, datové struktury) adekvátní problému?
  - Byly použity pokročilé techniky? (např. adaptační mechanismy)
  - Jsou některé postupy originálním přínosem autora?

**Nasazení heuristiky (13 pt.)** 
- Jakou metodou autor hledal nastavení parametrů?
- Jak byly plánovány experimenty a jaké byly jejich otázky?
- Jestliže byl proveden faktorový návrh (což příliš nedoporučujeme), jak kompletní byl (změna vždy jen jednoho parametru nestačí)?
- Na jak velkých instancích je heuristika schopna pracovat?
- Jestliže práce heuristiky není uspokojivá, jak systematické byly snahy autora zjednat nápravu?

**Experimentální vyhodnocení heuristiky (10 pt.)**
- Jak dalece jsou závěry vyhodnocení doloženy experimentálně?
- Je interpretace experimentů přesvědčivá?
- Pokud je algoritmus randomizovaný, byla tato skutečnost vzata v úvahu při plánování experimentů?
- Je možno z experimentů usoudit na iterativní sílu heuristiky?
- Byly nestandardní postupy experimentálně porovnány se standardními?
- Jsou výsledky experimentů srozumitelně prezentovány (grafy, tabulky, statistické metody)?


## Kopáč - Bash skript
Bash skript který pustí Python se vstupním souborem a zkontroluje pomocí programu diff jestli hotové řešení bylo korektní.

## Python skript
Rozdělený do pěti sbouborů.
 - main.py (hlavní spouštění)
 - classes.py (definice užitých tříd)
 - 8*implementace řešení

Jako vstup bere 
- soubor instancí
- jméno výstupního souboru pro konstruované řešení
- jméno výstupního souboru pro uložení spočítaných složitostí
