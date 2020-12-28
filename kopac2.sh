#!/bin/bash

# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}

                 KDE_JE_ZADANI="./data/NK/NK_test_inst.dat"
       KAM_ULOZIT_VYSLEDEK_SOL="./calculated/NK_solution.dat"
KAM_ULOZIT_VYSLEDEK_COMPLEXITY="./calculated/NK_complexity.dat"
     KDE_JE_KONTROLNI_VYSLEDEK="./data/NK/NK_test_sol.dat"
            KAM_ULOZIT_SUMMARY="./calculated/NK_test_summary"
                  JAKY_SOLVER="sim"

python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}