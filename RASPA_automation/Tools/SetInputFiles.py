import sys
sys.path.append("../")
sys.path.append('../../')

from RASPA_automation.Templates import PBS_script
from RASPA_automation.Templates import simulation_input

import RASPA_automation.Settings as Settings

templates = [
    PBS_script,
    simulation_input
]


def FormatAndWriteTemplate(template, job_number  ):
    filename = template.data['file_name'].format(job_number = job_number, MOF = MOF)
    f= open(filename, 'w+')
       
    text = template.data['text'].format(
    VDWCutoff = Settings.Settings['Cutoff'],
    SimulationType = Settings.Settings['SimulationType'],
    ForcefieldName = Settings.Settings['ForcefieldName'],
    ExternalTemperature = Settings.Settings['ExternalTemperature'],
    ExternalPressure = Settings.Settings['ExternalPressure'],
    RASPA_Directory = Settings.PBS_Settings['RASPA_Directory'],
    MOF= MOF,
    countABC=countABC,
    job_number = job_number)
    
    f.write(text)
    f.close()
    
    return None

def multiply_unit_cell(cif_address, cutoff):
    """
    Source:https://github.com/aiidateam/aiida-tutorials/blob/master/docs/pages/2019_molsim_school_Amsterdam/screening/screening.rst
    """
    try:
        from math import cos, sin, sqrt, pi
        deg2rad=pi/180.
        f= open(cif_address, 'r')
        data = f.read()
        f.close()
        a_len, b_len, c_len  = '_cell_length_a', '_cell_length_b', '_cell_length_c'
        aa, ab, ac = '_cell_angle_alpha', '_cell_angle_beta', '_cell_angle_gamma'
        lines = data.split('\n')
        a,b,c =0,0,0
        alpha ,beta, gamma = 0,0,0

        for l in lines:
            if l[:len(a_len)] == a_len:
                a =float( l.strip(a_len).strip())
            if l[:len(b_len)] == b_len:
                b = float(l.strip(b_len).strip())
            if l[:len(c_len)] == c_len:
                c =float( l.strip(c_len).strip())
            if l[:len(aa)] == aa:
                alpha = float(l.strip(aa).strip())*deg2rad
            if l[:len(ab)] == ab:
                beta = float(l.strip(ab).strip())*deg2rad
            if l[:len(ac)] == ac:
                gamma = float(l.strip(ac).strip())*deg2rad

        v = sqrt(1-cos(alpha)**2-cos(beta)**2-cos(gamma)**2+2*cos(alpha)*cos(beta)*cos(gamma))
        cell=[[0,0,0] for i in range(3)]
        cell[0] = [a, 0, 0]
        cell[1] = [b*cos(gamma), b*sin(gamma),0]
        cell[2] = [c*cos(beta), c*(cos(alpha)-cos(beta)*cos(gamma))/(sin(gamma)),c*v/sin(gamma)]
        diag = [cell[i][i] for i in range(3)]
        unit_intermediate = [cutoff/i*2. for i in diag]
        ui2 = []
        for i in unit_intermediate:
            if i%1 != 0:
                ui2.append((i//1) +1)
            else:
                ui2.append(i)
        unit_tuple = tuple(int(i+1) for i in ui2)
        unit_string = f"{unit_tuple[0]} {unit_tuple[1]} {unit_tuple[2]}"
    except:
        unit_string = "9 9 9"
    return unit_string



if __name__ == '__main__':
    import sys
    cif_address = sys.argv[1]
    job_number  = sys.argv[2]
    vdw = Settings.Settings['Cutoff']
    MOF = cif_address.split('/')[-1][:-4]
    countABC = multiply_unit_cell(cif_address, vdw)
    for template in templates:
        FormatAndWriteTemplate(template,job_number)
