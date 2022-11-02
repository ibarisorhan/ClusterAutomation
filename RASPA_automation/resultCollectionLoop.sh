#!/bin/bash
current=$(pwd)
sim_type=$(python3 ./Tools/returnSimType.py)
doc_name="${sim_type}_output.csv"
python3 Tools/setOutputHeader.py ../${doc_name}
cd ../MonteCarlo

for mof_dir in */; do
cd $current
cd ../$sim_type/Output/System_0
#cd ./$mof_dir/Output/System_0

for result in *.data; do
echo "$(pwd)"
echo $result
python3 ${current}/Tools/pythonResultCollectionTool.py $result ../../../${doc_name}
done
cd ${current}/../$sim_type
done
