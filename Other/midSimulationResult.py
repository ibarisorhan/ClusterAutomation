import sys

document = sys.argv[1]
output_doc = sys.argv[2]

def gatherAds(text):
    delimeter0 = "Current cycle: "
    delimeter1 = " out of "
    delimeter2 = "----------------------------------------------------------------------------------------------------------------------------------------------------\n"
    delimeter3 = "absolute adsorption: "
    delimeter4 = " [mol/uc],"
    delimeter5 = " [mol/kg],"
    delimeter6 = "(avg."
    t      = text.split(delimeter0)[-1]
    cycle  = t.split('\n')[0]
    out_of = cycle.split(delimeter1)[1].strip()
    cycle  = cycle.split(delimeter1)[0].strip()
    ads    = t.split(delimeter2)[1]
    ads    = ads.split(delimeter3)[1]
    ads    = ads.split(delimeter4)[1]
    ads    = ads.split(delimeter5)[0]
    ads    = ads.split(delimeter6)[0].strip()
    return cycle,out_of,ads


try:
    f = open(document, "r")
    data = f.read()
    f.close()

    cycle, out_of, ads = gatherAds(data)
    Units = document.split("/")[-1].split("_")[-3]
    Temp  = document.split("/")[-1].split("_")[-2]
    Press = document.split("/")[-1].split("_")[-1][:-5]
    MOF   = document.split("/")[-1].split(Units)[0][7:]


    f = open(output_doc, "a+")
    f.write(f"{document},{MOF},{Units},{Temp},{Press},{ads},{cycle},{out_of}\n")
    f.close()


except:
    print(f"ERROR: Unable to read data from document document: {document}")
