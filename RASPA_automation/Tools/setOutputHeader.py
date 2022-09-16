from sys

header = "MOF,UNIT,TEMP,PRESSURE,UPTAKE,MARGIN,WARNINGS,NOTES\n"
output = sys.argv[1]

f= open(output, 'w+')
f.write(header)
f.close()

