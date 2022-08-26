#!/bin/bash -f
#set i = 190
#ifort avg.f90 -o avg.o
#chmod +x avg.o
#./avg.o  <<!
#set k = 1
#k="`wc -l rad.dat`"
for ((k=100;k<=200;k=k+20))
do 
echo ${k}
if [ $k -ge 120 ]
then
  echo "k is 100"
else 
echo "k is junk"
fi
done
#
#!
#wc -l rad.dat
