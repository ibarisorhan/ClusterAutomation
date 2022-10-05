from os import listdir
import sys

sys.path.append("../")
sys.path.append('../../')

import RASPA_automation.Settings as Settings


doc   = Settings.Structures['ListOfStructures']
count = Settings.Structures['NumberOfJobs']

current  = "./" + doc.strip('.txt') + Settings.Structures['currentSuffix']
complete = "./" + doc.strip('.txt') + Settings.Structures['compeletedSuffix']


f  = open(current,  'r+')
f2 = open(complete, 'a+')
f2.write('\n')
f2.write(f.read())
f2.close()
f.close()

f = open(doc, 'r+')
queue = [i for i in f.read().split('\n') if i != '']
f.close()


count_in_queue = min(len(queue), count)

f = open(current, 'w+')

for i in range(count_in_queue):
	f.write(f'{queue [i]}\n')
f.close()


f = open(doc, 'w+')
for i in range(count_in_queue,len(queue)):
	f.write(f'{queue [i]}\n')
f.close()
