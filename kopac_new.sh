#!/bin/bash

# --- New kopac ---
# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDKY}     ${KDE_JE_KONTROLNI_VYSLEDEK}
# python main.py ${1}             ${2}                       ${4}
#                SLOŽKA           SLOŽKA                     SOUBOR

ALG="sim"

# Prepare arguments for python script
mkdir -p "./calculated_${ALG}"
                 KDE_JE_ZADANI="./data/wuf20-78-M1"
           KAM_ULOZIT_VYSLEDKY="./calculated_${ALG}/"
     KDE_JE_KONTROLNI_VYSLEDEK="./data/wuf20-78-M-opt.dat"

# Start python script
python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDKY} ${KDE_JE_KONTROLNI_VYSLEDEK}

echo "========================================="
echo "Solved with ${ALG}."