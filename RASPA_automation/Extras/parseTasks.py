f = open('tasks.txt','r')
data = f.read()
f.close()

print(len(data.split('.gadi-pbs'))) #ASSUMES THIS SPECIFIC CLUSTER + NAMING CONVENTION IS USED
