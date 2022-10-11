#The Settings Here Should Be Checked Before Simulations Are Run!

ABSOLUTE_PATH_TO_RASPA_DIR = '$HOME'
PROJECT_NAME = '' 
Sim = 'MonteCarlo'


Settings = {
	'SimulationType': Sim, #Must be ./Templates/simulation_input.py 
        'Cutoff':12.5,
	'ForcefieldName' : "AutomationScript",
	'ExternalTemperature' : 298,
	'ExternalPressure' :  40,

}

PBS_Settings = {
	'RASPA_Directory' : f'{ABSOLUTE_PATH_TO_RASPA_DIR}/RASPA/simulations/'
}

Structures = {
	'Directory' : f'{ABSOLUTE_PATH_TO_RASPA_DIR}/RASPA/simulations/share/raspa/structures/cif/',
	'NumberOfJobs' : 500, #number of jobs to run simultaneously
	'ListOfStructures': './Queue/Structures.txt', #document of structures to be simulated
	'currentSuffix': '_current.txt',
	'compeletedSuffix': '_complete.txt'
}
