import sys
import os 
from os import listdir

sys.path.append("../")
sys.path.append('../../')
import RASPA_automation.Settings as Settings


template = {"file_name" : "BATCH_{batch_number}.txt",
"text" : """#!/bin/bash
#PBS -P {PROJECT_NAME}
#PBS -q normal
#PBS -l ncpus=48
#PBS -l mem=16gb
#PBS -l walltime=24:00:00
#PBS -N RASPA_BATCH_{batch_number}
#PBS -o BATCH.out
#PBS -e BATCH.err
cd $PBS_O_WORKDIR
"""}


def create_batch_pbs(template, batch_number):
    """
    Take template (dict) and batch_number (int)
    Return file name after writing initial PBS task
    """
    name = template['file_name'].format(batch_number = batch_number)
    with open(name, 'w+') as task:
        task.write(template['text'].format(batch_number = batch_number, PROJECT_NAME = Settings.PROJECT_NAME))
    return name



def get_final_2lines(pbs_doc):
    f=open(pbs_doc,'r')
    data=f.read()
    f.close()
    
    lines = [i for i in data.split('\n') if i.strip() != ""]
    return lines[-2:]



def add_to_batch(batch,pbs):
    last2 = get_final_2lines(pbs)
    new_line = '\n' + last2[0]
    new_line += '\n' + last2[1] + ' &\n'
    with open(batch,'a') as file:
        file.write(new_line)
    return None

def add_line(doc,line):
    with open(doc,'a') as f:
        f.write('\n')
        f.write(line)
        f.write('\n')
    return None

if __name__ == "__main__":
    directory = './'
    PBS_scripts = [directory + i for i in listdir(directory) if i[:3] == "PBS"]
    batch_number = 0
    while len(PBS_scripts)>0:
        name = create_batch_pbs(template, batch_number)
        batch_number += 1
        for i in PBS_scripts[:48]:
            add_to_batch(name, i)
            os.remove(i)
        add_line(name,'wait')

        PBS_scripts = [directory + i for i in listdir(directory) if i[:3] == "PBS"]
