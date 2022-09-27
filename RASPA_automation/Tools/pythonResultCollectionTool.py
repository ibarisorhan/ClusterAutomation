import sys

document = sys.argv[1]
output_doc = sys.argv[2]

try:
    f = open(document, "r")
    data = f.read()
    f.close()
    
    delimiter  = """Number of molecules:
===================="""
    delimeter2 = """Average Widom Rosenbluth factor:
================================""" 
    delimeter3 = "Average loading absolute [mol/kg framework]"
    delimeter4 = "Average loading absolute [milligram/gram framework] "
    
    result_block = data.split(delimiter)[1].split(delimeter2)[0]
    #  print(len(data.split(delimiter)[1].split(delimeter2)))
    Co2_uptake1 = result_block.split(delimeter3)[1].split(delimeter4)[0]
    # print(Co2_uptake1)
    uptake_intermediate = Co2_uptake1.strip().strip("\n").strip("[-]")
    # print(Co2_uptake1.strip().strip("\n").strip("[-]"))
    uptake_intermediate2 = uptake_intermediate.split("+/-")
    uptake_abs = uptake_intermediate2[0].strip()
    uptake_error = uptake_intermediate2[1].strip()
    # print(uptake_abs, uptake_error)
    Units = document.split("/")[-1].split("_")[-3]
    Temp  = document.split("/")[-1].split("_")[-2]
    Press = document.split("/")[-1].split("_")[-1][:-5]#.strip(".data")
    MOF   = document.split("/")[-1].split(Units)[0][7:]#.strip("output_")
    errors = ""
    print("Made to Warning Check")
    hasError = "No"
    if len(data.split("WARNING"))>1:
        hasError = "Yes"
        warnings = data.split('WARNING')
        for i in warnings[1:]:
            errors += " (x)"
            errors += i.split('\n')[0]

    f = open(output_doc, "a+")
    f.write(f"{document},{MOF},{Units},{Temp},{Press},{uptake_abs},{uptake_error},{hasError}\n")
    f.close()
    
    
except: 
    print(f"ERROR: Unable to read data from document document: {document}")

