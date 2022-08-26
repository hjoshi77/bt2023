#!/bin/bash  -f 
for ((i=1;i<=5;i=i+1))
do 
echo ${i}
l=$(($i - 5))
k=`echo $i * 0.5 | bc -l`
k1=kya
tim_step=`expr $i * 1000000`
echo ${tim_step}
echo ${l}
echo ${k}
ln1=$((i * 5))
ln2=$((i * 50))    
echo $ln1
echo $k1
done
