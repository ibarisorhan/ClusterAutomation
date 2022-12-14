import sys

try:
    inpt = sys.argv[1]
    delimeter = """loop_
  _atom_site_label
  _atom_site_occupancy
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_thermal_displace_type
  _atom_site_B_iso_or_equiv
  _atom_site_type_symbol
  _atom_site_charge"""
    del2 = """loop_
  _atom_site_label
  _atom_site_occupancy
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_thermal_displace_type
  _atom_site_B_iso_or_equiv
  _atom_site_type_symbol"""
    f = open(inpt,'r')
    data = f.read()
    f.close()
    #print(len(data.split(delimeter)))
    if len(data.split(delimeter)) != 2:
        print(inpt)
    else:
        ndata = data.split(delimeter)[0] + del2 + '\n'
        for line in data.split(delimeter)[1].split('\n'):
            if line.strip() != "":
                for col in line.split()[:-1]:
                    ndata += col
                    ndata += "  "
                ndata += "\n"
               
        f = open(inpt,'w')
        f.write(ndata)
        f.close()
   
except:
    print('ERROR')
