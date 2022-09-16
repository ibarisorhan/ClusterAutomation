#!/bin/bash/


SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR
SimType="$(python3 ./Tools/returnSimType.py)"
Pressure="$(python3 ./Tools/returnPressure.py)"
echo $SimType
mkdir -p ../$SimType
JobCount=1

CifDir="$(python3 ./Tools/returnCifDir.py)"
python3 ./Tools/setQueue.py
queueDoc="$(python3 ./Tools/returnQueueDocument.py)"

while read -r line; do
	cd $SCRIPT_DIR
        cif="${CifDir}/${line}"
	MOFint=${cif#*$CifDir}
	MOF=${MOFint%.*}
	echo $MOF
	mkdir -p ../$SimType/
	cd ../$SimType/
	python3 ${SCRIPT_DIR}/Tools/SetInputFiles.py $cif $JobCount
	task="PBS_${JobCount}.txt"
        JobCount=$((JobCount + 1))
	echo $task
	qsub $task
done < $queueDoc

#python3 ${SCRIPT_DIR}/Tools/SetQsub.py



