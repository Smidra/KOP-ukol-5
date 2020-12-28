#!/bin/bash

# --- New kopac ---
# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
# python main.py ${1}             ${2}                       ${3}                              ${4}                         ${5}                  ${6}

# Setup of python
TYPE="GEN"
ALG="redux"

# Setup of generator
THINGS=20 # total number of things
INSTANCES=300    # generate this much of knapsack instances
MAX_WEIGHT=1000  # Maxmimum weight of a thing
MAX_COST=1000    # Maxmimum cost of a thing
#PERMUTATIONS=10

# Optional
CAPACITY_TO_SUM_WEIGHT=0.8  # -m Ratio of capacity to sum weight. Default [0.8]. Can be interval.
HEAVY_THINGS="bal"  # -w More *heavy*, *light* or *bal*anced things [bal]
CORELATION="uni"    # -c Weight-cost correlation *uni*, *corr*, *strong* [uni]
GRANULARITY="0.1"     # -k Granularity. -w must be set. [1]
mkdir -p "./data/GEN/"

# Generator paths
GENERATING_NAME="${THINGS}-${INSTANCES}_(w${MAX_WEIGHT}c${MAX_COST})[m${CAPACITY_TO_SUM_WEIGHT}w${HEAVY_THINGS}c${CORELATION}k${GRANULARITY}]"
GENERATING_PATH="./data/${TYPE}/${GENERATING_NAME}"

# Prepare arguments for python script
mkdir -p "./calculated_${ALG}"
                 KDE_JE_ZADANI="${GENERATING_PATH}_inst.dat"
       KAM_ULOZIT_VYSLEDEK_SOL="./calculated_${ALG}/${GENERATING_NAME}_solution.dat"
KAM_ULOZIT_VYSLEDEK_COMPLEXITY="./calculated_${ALG}/${GENERATING_NAME}_complexity.dat"
     KDE_JE_KONTROLNI_VYSLEDEK="${GENERATING_PATH}_sol.dat"
            KAM_ULOZIT_SUMMARY="./calculated_${ALG}/${GENERATING_NAME}_summary"
                  JAKY_SOLVER="${ALG}"


# Generate instances with generator -- do it only once
# echo ./hen/kg2 -n "$THINGS" -N "$INSTANCES" -W "$MAX_WEIGHT" -C "$MAX_COST" -m "$CAPACITY_TO_SUM_WEIGHT" -w "$HEAVY_THINGS" -c "$CORELATION" -k "$GRANULARITY"
if [ ! -f "${GENERATING_PATH}_sol.dat" ]; then
  ./gen/kg2 -n "$THINGS" -N "$INSTANCES" -W "$MAX_WEIGHT" -C "$MAX_COST" -m "$CAPACITY_TO_SUM_WEIGHT" -w "$HEAVY_THINGS" -c "$CORELATION" -k "$GRANULARITY" > "${GENERATING_PATH}_inst.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 5  > "${GENERATING_PATH}_permut5.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 10 > "${GENERATING_PATH}_permut10.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 15 > "${GENERATING_PATH}_permut15.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 20 > "${GENERATING_PATH}_permut20.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 25 > "${GENERATING_PATH}_permut25.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 50 > "${GENERATING_PATH}_permut50.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 100 > "${GENERATING_PATH}_permut100.dat"
  cat "${GENERATING_PATH}_inst.dat" | ./gen/kg_perm -d 1000 -N 200 > "${GENERATING_PATH}_permut200.dat"
fi

# Is there a solution file? If not, create it.
if [ ! -f "${GENERATING_PATH}_sol.dat" ]; then
  echo "${GENERATING_PATH}_sol.dat does not exist!"
  # The solution file does not exist, create it.
  python main.py "${GENERATING_PATH}_inst.dat" "${GENERATING_PATH}_sol.dat" "/dev/null" "/dev/null" "/dev/null" "bab"
  echo "${GENERATING_PATH}_sol.dat created!"
fi

# Start python script
python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}

## No permutace
#python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} ${KDE_JE_KONTROLNI_VYSLEDEK} ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 5 permutace
#python main.py "${GENERATING_PATH}_permut5.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut5.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 10 permutace
#python main.py "${GENERATING_PATH}_permut10.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut10.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 15 permutace
#python main.py "${GENERATING_PATH}_permut15.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut15.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 20 permutace
#python main.py "${GENERATING_PATH}_permut20.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut20.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 25 permutace
#python main.py "${GENERATING_PATH}_permut25.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut25.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 50 permutace
#python main.py "${GENERATING_PATH}_permut50.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut50.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 100 permutace
#python main.py "${GENERATING_PATH}_permut100.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut100.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}
## 200 permutace
#python main.py "${GENERATING_PATH}_permut200.dat" ${KAM_ULOZIT_VYSLEDEK_SOL} ${KAM_ULOZIT_VYSLEDEK_COMPLEXITY} "${GENERATING_PATH}_permut200.dat" ${KAM_ULOZIT_SUMMARY} ${JAKY_SOLVER}


echo "========================================="
echo "Solved with ${JAKY_SOLVER}."
echo "N= $THINGS"
echo "Generated instances: ${GENERATING_NAME}"