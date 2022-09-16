#!/bin/bash/

CifDir="cifs"



SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR
SimType="$(python3 ./Tools/returnSimType.py)"
echo $SimType

mkdir -p ../$SimType


while read -r line;
do
Pressure=$line
for cif in ../$CifDir/*.cif; do
	cd $SCRIPT_DIR
	MOFint=${cif#*$CifDir}
	MOF=${MOFint%.*}
	echo $MOF
	mkdir -p ../$SimType/$MOF/
	cp $cif ../$SimType/$MOF/
	cd ../$SimType/$MOF/
	python3 ../../RASPA_automation/Tools/simulatePressures.py ../$cif $line
	task="PBS_script_${Pressure}.txt"
	echo $task
	qsub $task
done
done < pressures2simulate.txt
