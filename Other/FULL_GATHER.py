#!/usr/bin/env python
# coding: utf-8
# FOR GATHERING META DATA, uncleaned code but is functional
# Go to directory with RASPA results ('.data' files) and run from there!



# ## CONSTANTS AND MODULES

import copy
from os import listdir 

HENRY_DELIMETER = 'Average Henry coefficient'
WIDOM_DELIMETER = 'Average Widom Rosenbluth factor'
SIMULATION_NAME = 'HenryCoefficient'


delimeters2use = [HENRY_DELIMETER]#,WIDOM_DELIMETER]

def remove_spaces(label):
    """Take string; return string where spaces are replaced with underscores '_' """
    out = ""
    for i in label.split():
        out += i
        out += "_"
    out = out[:-1]
    return out


# ## DETAIL GROUPS and DF_DICT

details_to_gather = {
'SimulationDetails' : 
                    ["Number of cycles",
                    "Number of initializing cycles",
                    "Number of equilibration cycles",
                    "Print every",
                    "Timestep",
                    "External temperature",
                    "External Pressure",],

'FrameworkDetails' :
                    ["Framework name",
                    "Degrees of freedom",
                    "Translational Degrees of freedom",
                    "Rotational Degrees of freedom",
                    "Degrees of freedom Framework",
                    "Number of unitcells [a]",
                    "Number of unitcells [b]",
                    "Number of unitcells [c]",
                    "volume of the cell",
                    "Number of framework atoms in the unit cell",
                    "Number of framework atoms",
                    "Framework Mass",
                    "Framework Density",
                    "Framework has net charge",
                    "largest charge ",
                    "smallest charge"],

'ForcefieldDetails': 
                    ["Forcefield",
                    "Minimal distance",
                    "CutOff VDW",
                    "CutOff VDW switching on",
                    "CutOff charge-charge",
                    "CutOff charge-charge switching on",
                    "CutOff charge-bonddipole",
                    "CutOff charge-bondipole switching on",
                    "CutOff bonddipole-bonddipole",
                    "CutOff bonddipole-bondipole switching on",]
        }

ABEXEM_example = {'HenryCoefficient_SimulationDetails SimulationDate': 'Mon Aug 29 18:15:18 2022',
 'HenryCoefficient_SimulationDetails [Warnings]': '0',
 'HenryCoefficient_SimulationDetails Number_of_cycles': '20000',
 'HenryCoefficient_SimulationDetails Number_of_initializing_cycles': '0',
 'HenryCoefficient_SimulationDetails Number_of_equilibration_cycles': '0',
 'HenryCoefficient_SimulationDetails Print_every': '1000',
 'HenryCoefficient_SimulationDetails Timestep': '0.000500',
 'HenryCoefficient_SimulationDetails External_temperature[K]': '298 ',
 'HenryCoefficient_SimulationDetails External_Pressure[Pa]': '0 ',
 'HenryCoefficient_FrameworkDetails SimulationDate': 'Mon Aug 29 18:15:18 2022',
 'HenryCoefficient_FrameworkDetails [Warnings]': '0',
 'HenryCoefficient_FrameworkDetails Framework_name': 'ABEXEM_clean_DDEC',
 'HenryCoefficient_FrameworkDetails Degrees_of_freedom': '0',
 'HenryCoefficient_FrameworkDetails Translational_Degrees_of_freedom': '0',
 'HenryCoefficient_FrameworkDetails Rotational_Degrees_of_freedom': '0',
 'HenryCoefficient_FrameworkDetails Degrees_of_freedom_Framework': '0',
 'HenryCoefficient_FrameworkDetails Number_of_unitcells_[a]': '3',
 'HenryCoefficient_FrameworkDetails Number_of_unitcells_[b]': '3',
 'HenryCoefficient_FrameworkDetails Number_of_unitcells_[c]': '2',
 'HenryCoefficient_FrameworkDetails volume_of_the_cell': '47394.797788827906 (A^3)',
 'HenryCoefficient_FrameworkDetails Number_of_framework_atoms_in_the_unit_cell': '144',
 'HenryCoefficient_FrameworkDetails Number_of_framework_atoms': '2592',
 'HenryCoefficient_FrameworkDetails Framework_Mass[g/mol]': '50256.910476631601 ',
 'HenryCoefficient_FrameworkDetails Framework_Density[kg/m^3]': '1760.816588004671 ',
 'HenryCoefficient_FrameworkDetails Framework_has_net_charge': '0.000000',
 'HenryCoefficient_FrameworkDetails largest_charge': '0.000000',
 'HenryCoefficient_FrameworkDetails smallest_charge': '0.000000',
 'HenryCoefficient_ForcefieldDetails SimulationDate': 'Mon Aug 29 18:15:18 2022',
 'HenryCoefficient_ForcefieldDetails [Warnings]': '0',
 'HenryCoefficient_ForcefieldDetails Forcefield': 'AutomationScript',
 'HenryCoefficient_ForcefieldDetails Minimal_distance': '1',
 'HenryCoefficient_ForcefieldDetails CutOff_VDW': '12.000000 (144.000000)',
 'HenryCoefficient_ForcefieldDetails CutOff_VDW_switching_on': '10.800000 (116.640000)',
 'HenryCoefficient_ForcefieldDetails CutOff_charge-charge': '12.000000 (144.000000)',
 'HenryCoefficient_ForcefieldDetails CutOff_charge-charge_switching_on': '7.800000 (60.840000)',
 'HenryCoefficient_ForcefieldDetails CutOff_charge-bonddipole': '12.000000 (144.000000)',
 'HenryCoefficient_ForcefieldDetails CutOff_charge-bondipole_switching_on': '8.400000 (70.560000)',
 'HenryCoefficient_ForcefieldDetails CutOff_bonddipole-bonddipole': '12.000000 (144.000000)',
 'HenryCoefficient_ForcefieldDetails CutOff_bonddipole-bondipole_switching_on': '9.000000 (81.000000)',
 'HenryCoefficient_RASPA Average_Henry_coefficient[mol/kg/Pa]': '2.30133e-05',
 'HenryCoefficient_RASPA Average_Henry_coefficient_margin': '1.92223e-07'}


outputs_collection = {i:[] for i in ABEXEM_example.keys()}


# ## FUNCTIONS


def get_simulation_attribute(delimeter, data, simtype=SIMULATION_NAME, feature_name = "", label=""):
    #For the blocks of output data where error margins are included
    #Typically the blocks have the header of their name followed by a line of '='
    
    line = data.split(delimeter)[2].split('\n')[0]
    units = ""
    if len(line.split('[')) == 2:
        units = line.split('[')[1].split(']')[0]
    
    average_result = line.split('+/-')[0].strip(': ')
    margin = line.split('+/-')[1].split('[')[0].strip()
    
    if label == "":
        label = f'{remove_spaces(simtype)}_{feature_name} {delimeter}'
    output = {f'{label}[{units}]':average_result,f'{label}_margin':margin,}
    
    return output


def add_data_to_record(record_in={},data="",delimeter_1="",delimeter_2= "\n",label="",simulation_name=SIMULATION_NAME):
    """
    Take
    record_in: dictionary, and rest of args: string(s)
    
    Return 
    record_out: dictionary with new data saved to record_out 
    
    """
    #simulationName is a string; eg HenryCoefficient, MonteCarlo, etc.
    record_out  = record_in
    if label=="":
                label = simulation_name + " " +remove_spaces(delimeter_1)
    if delimeter_1 != "" and len(data.split(delimeter_1)) >1:
        try:
            
            val = data.split(delimeter_1)[1]

            if len(val.split(delimeter_2)[0]) == 1:
                print(f"Error Gathering \"{delimeter_1}\"").strip()
                return record
            else:
                val = val.split(delimeter_2)[0].strip(": ")
                if len(val.split('[')) > 1:
                    unit = val.split('[')[1].split(']')[0]
                    val = val.split('[')[0]
                    label += f'[{unit}]'
                record_out[label] = val
     
        except:
            record_out[label] = ""
            print(f"Error Gathering \"{delimeter_1}\"").strip()
    
    else:
        print(f"Error Gathering \"{delimeter_1}\"").strip()
    
    return record_out

def add_simulation_run_date(record_in={},data="",simulation_name = SIMULATION_NAME):
    record_out = record_in
    try:
        val  = data.split('\nSimulation started')[0].split("\n")[-1]
        label = f'{simulation_name} SimulationDate'
        record_out[label]= val
    except:
        print("Error Gathering Simulation Date/Time Information!")
    
    return record_out


def get_number_of_warnings(record_in={},data="",simulation_name = SIMULATION_NAME):
    delimeter_1 ="Simulation finished,"
    delimeter_2 = "warnings"
    label = f"{simulation_name} [Warnings]"
    record_out = add_data_to_record(record_in,data,delimeter_1,delimeter_2,label,simulation_name)
    return record_out
    
    
def get_details(record_in={},data="",delimeters = [],simulation_name = ""):
    record_out = record_in
    try:
        record_out = add_simulation_run_date(record_out,data,simulation_name)
        record_out = get_number_of_warnings(record_out,data,simulation_name)


        for delimeter in delimeters:
            #add_data_to_record(record_in={},data="",delimeter_1="",delimeter_2= "\n",label="",simulation_name="")
            record_out =  add_data_to_record(record_out,data,delimeter,"\n","",simulation_name)
    except:
        print('Error Gathering Simulation Details')
    return record_out


def gather_details_by_group(data="", details_to_gather = {}, simulation_name=SIMULATION_NAME):
    record = {}
    for group in details_to_gather.keys():
        record = get_details(record,data,details_to_gather[group],f"{simulation_name}_{group}")
        
    return record


# ## Simulation-Specific Data Gathering Functions


def get_simulation_attribute(delimeter, data, simtype=SIMULATION_NAME, label=""):
    #For the blocks of output data where error margins are included
    #Typically the blocks have the header of their name followed by a line of '='
    feature_name = "RASPA"
    units = '' 
    if label == "":
        label = f'{remove_spaces(simtype)}_{remove_spaces(feature_name)} {remove_spaces(delimeter)}'
    
    
    try:

        line = data.split(delimeter)[2].split('\n')[0]
        if len(line.split('[')) == 2:
            units = line.split('[')[1].split(']')[0]

        average_result = line.split('+/-')[0].strip(': ')
        margin = line.split('+/-')[1].split('[')[0].strip()

        if label == "":
            label = f'{remove_spaces(simtype)}_{remove_spaces(feature_name)} {remove_spaces(delimeter)}'
        output = {f'{label}[{units}]':average_result,f'{label}_margin':margin,}
    
    except:
        output = {f'{label}[{units}]':'',f'{label}_margin':'',}
    return output




def gather_full(data,simtype=SIMULATION_NAME, result_delimeters = delimeters2use):
    output  = gather_details_by_group(data,details_to_gather,simtype)
    for delimeter in result_delimeters:
        attribute_dict = get_simulation_attribute(delimeter,data)
        for key in attribute_dict.keys():
            output[key] = attribute_dict[key]
    return output
    



def save_record_to_dfdict(current,df_dict_in):
    df_dict = copy.deepcopy(df_dict_in)
    for key in df_dict.keys():
        if key not in current.keys():
            df_dict[key].append('')
        else:
            df_dict[key].append(current[key])
    return df_dict



def get_result_and_combine(data,full=outputs_collection,simtype=SIMULATION_NAME, result_delimeters = delimeters2use):
    current = gather_full(data,simtype, result_delimeters)
    full  = save_record_to_dfdict(current,full)
    return full


# ## Writing to CSV


def write_to_csv(dfdict,doc = f'../{SIMULATION_NAME}_output.csv'):
    key_order = list(dfdict.keys())
    f = open(doc,'w+')
    
    for key in key_order:
        f.write(key)
        f.write(',')
    f.write('\n')
    for index in range(len(dfdict[key_order[0]])):
        for key in key_order:
            val = dfdict[key][index]
            f.write(val)
            f.write(',')
        f.write('\n')


# # RUN


loc = './'
data_files = [i for i in listdir(loc) if i[-5:]=='.data']
for file in data_files:
    print(file)

    full_file_address = f'{loc}/{file}'
    f = open(full_file_address,'r')
    data = f.read()
    f.close()
    
    outputs_collection = get_result_and_combine(data,outputs_collection)


write_to_csv(outputs_collection)




