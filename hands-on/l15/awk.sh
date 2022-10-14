awk '{sm+=($2-48.1905)*($2-48.1905)} END {print sqrt(sm/21)}' plant.dat
awk '{sm+=} END {print sm/21}' plant.dat
