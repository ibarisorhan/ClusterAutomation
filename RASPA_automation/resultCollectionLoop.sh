#!/bin/bash
current=$(pwd)
python3 Tools/setHeader.py ../$1
cd ../MonteCarlo

for mof_dir in */; do
cd $current
cd ../MonteCarlo/Output/System_0
#cd ./$mof_dir/Output/System_0

for result in *.data; do
echo "$(pwd)"
echo $result
python3 ${current}/Tools/pythonResultCollectionTool.py $result ../../../$1
done
cd ${current}/../MonteCarlo
done

