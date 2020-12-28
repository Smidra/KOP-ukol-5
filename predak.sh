#!/bin/bash




TYPE="ZKC"
ALG="redux"
INSTANCES=10
bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"


#INSTANCES=15
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=20
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=22
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=25
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=27
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=30
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=32
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=35
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"

#INSTANCES=37
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"
#INSTANCES=40
#bash kopac.sh "./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat" "./calculated_${ALG}/${TYPE}${INSTANCES}" "./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat" "./calculated_${ALG}/${TYPE}_summary"



# Zaloha kopac
#!/bin/bash
# --- New kopac without generator ---
# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
# python main.py ${1}             ${2}                       ${3}                              ${4}                         ${5}                  ${6}

#TYPE="ZKC"
#ALG="redux"
#INSTANCES=10
#
#                 KDE_JE_ZADANI="./data/${TYPE}/${TYPE}${INSTANCES}_inst.dat"
#       KAM_ULOZIT_VYSLEDEK_SOL="./calculated_${ALG}/${TYPE}${INSTANCES}_solution.dat"
#KAM_ULOZIT_VYSLEDEK_COMPLEXITY="./calculated_${ALG}/${TYPE}${INSTANCES}_complexity.dat"
#     KDE_JE_KONTROLNI_VYSLEDEK="./data/${TYPE}/${TYPE}${INSTANCES}_sol.dat"
#            KAM_ULOZIT_SUMMARY="./calculated_${ALG}/${TYPE}_summary"
#                  JAKY_SOLVER="${ALG}"
#
#mkdir -p "./calculated_${ALG}"
#python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
