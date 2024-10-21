#midSiumulationResultCollectionTool.py
import sys

document = sys.argv[1]
output_doc = sys.argv[2]


try:
    cycle_del1="Current cycle:"
    cycle_del2="out of"




    del1="""Loadings per component:
----------------------------------------------------------------------------------------------------------------------------------------------------"""
    del2=") [mol/kg]"
    del3="(avg."

    f = open(document, "r")
    data = f.read()
    f.close()
    
    uptake_error = "n/a"
    # print(uptake_abs, uptake_error)
    Units = document.split("/")[-1].split("_")[-3]
    Temp  = document.split("/")[-1].split("_")[-2]
    Press = document.split("/")[-1].split("_")[-1][:-5]#.strip(".data")
    MOF   = document.split("/")[-1].split(Units)[0][7:]#.strip("output_")
    errors = ""
    cycle = data.split(cycle_del1)[-1].split(cycle_del2)[0].strip()
    uptake_abs = data.split(del1)[-1].split(del2)[0].split(del3)[-1].strip()
    hasError = "No"
    if len(data.split("WARNING"))>1:
        hasError = "Yes"
        warnings = data.split('WARNING')
        for i in warnings[1:]:
            errors += " (x)"
            errors += i.split('\n')[0]
    #print(f"{document},{MOF},{Units},{Temp},{Press},{uptake_abs},{uptake_error},{hasError},NO\n")
    f = open(output_doc, "a+")
    f.write(f"{document},{MOF},{Units},{Temp},{Press},{uptake_abs},{uptake_error},{hasError},NO\n") #simulation complete
    f.close()
    
    
except: 
    print(f"ERROR: Unable to read data from document document: {document}")
