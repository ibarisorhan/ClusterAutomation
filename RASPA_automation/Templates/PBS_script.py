data  = {"file_name" : "PBS_{job_number}.txt",
"text" : """#!/bin/bash
#PBS -P PROJECT_NAME
#PBS -q normal
#PBS -l ncpus=1
#PBS -l mem=16gb
#PBS -l walltime=24:00:00
#PBS -N J_{MOF}
#PBS -o AUTOMATION_SCRIPT.out
#PBS -e AUTOMATION_SCRIPT.err
cd $PBS_O_WORKDIR

RASPA_DIR=\"{RASPA_Directory}\"
$RASPA_DIR/bin/simulate -i simulation_{job_number}.input"""}
