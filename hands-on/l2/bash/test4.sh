nanometer=$1
layers_real= $(($nanometer / 0.45))
layers=${layers%.*}
angstrom=$((${nanometer} * 5))
waterbox=$((${angstrom} + 20))
pdbs=$(($layers * 6))
echo "length" $nanometer,"z" $waterbox,"layers" $layers,"no. of units" $pdbs
