#!/bin/bash 
k=0
for ((j=1;j<=4;j=j+1))                                                                                                                 
do
m=0
n="`ls pdb_files/${j}_*|wc -l`"
#="`wc -l rad.dat`" 
for ((l=1;l<=n;l=l+1))
do 
k=$((k+1))
m=$((m+1))
echo $k
echo $m
done
done
