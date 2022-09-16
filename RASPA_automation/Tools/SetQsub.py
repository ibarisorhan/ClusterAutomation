
if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../..")
    import RASPA_automation.Settings as Settings
    fname = '../' + Settings.Structures['ListOfStructures'].strip('.txt') + Settings.Structures['currentSuffix']
    if fname [-4:] != '.txt' and fname.find('.') == -1:
        fname += '.txt'
    f = open(fname, 'r+')
    num = len(f.read().split('\n'))
    f.close()



    output = 'qsub -MAIN_LOOP '
    for i in range(1,num+1):
        output += f'J{i},'

    output = output[:-1]
    output += "-cwd MAIN_LOOP_PBS.txt"
    sys.stdout.write(output)
    sys.exit(0)
