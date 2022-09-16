from math import cos, sin, sqrt, pi
def multiply_unit_cell(cif_address, cutoff):
    """
    Source:https://github.com/aiidateam/aiida-tutorials/blob/master/docs/pages/2019_molsim_school_Amsterdam/screening/screening.rst
    """
    from math import cos, sin, sqrt, pi
    deg2rad=pi/180.
    f= open(cif_address, 'r')
    data = f.read()
    f.close()
    a_len, b_len, c_len  = '_cell_length_a', '_cell_length_b', '_cell_length_c'
    aa, ab, ac = '_cell_angle_alpha', '_cell_angle_alpha', '_cell_angle_alpha'
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
    unit_tuple = tuple(int(i) for i in ui2)
    unit_string = f"{unit_tuple[0]} {unit_tuple[1]} {unit_tuple[2]}"
    return unit_string


if __name__ == '__main__':
    import sys
    cif_address = sys.argv[1]
    vdw = float(sys.argv[2])
    
    import sys
    sys.stdout.write(multiply_unit_cell(cif_address, vdw))
    sys.exit(0)
