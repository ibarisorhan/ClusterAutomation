#----------------- TEMPLATE -----------------
data  = {"file_name" : "simulation_{job_number}.input"}

simulation = {"MonteCarlo": """
SimulationType        MonteCarlo
NumberOfCycles        100000
PrintEvery            1000
RestartFile           no

Forcefield                    {ForcefieldName}
Framework                     0
FrameworkName                 {MOF}
UnitCells                     {countABC}
ExternalTemperature           {ExternalTemperature}
ExternalPressure              {ExternalPressure}


NumberOfGrids 2
GridTypes C_co2 O_co2
SpacingVDWGrid 0.1
SpacingCoulombGrid 0.1
UseTabularGrid yes

Component 0 MoleculeName             CO2
            MoleculeDefinition       CO2
            TranslationProbability   0.5
            RegrowProbability        0.5
            RotationProbability      0.5
            ReinsertionProbability   0.5
            SwapProbability          1.0
            CreateNumberOfMolecules  0

""",



"MakeGrid":"""
SimulationType        MakeGrid
RestartFile           no

CutOff                12.5

Forcefield                    {ForcefieldName}
Framework                     0
FrameworkName                 {MOF}
UnitCells                     {countABC}
ExternalTemperature           {ExternalTemperature}
ExternalPressure              {ExternalPressure}
AddAtomNumberCodeToLabel      yes

NumberOfGrids                 2
GridTypes                     C_co2 O_co2
SpacingVDWGrid                0.05
SpacingCoulombGrid            0.05
UseChargesFromCIFFile         yes

"""
}



#----------------- SETUP -----------------
import sys
sys.path.append("../")
sys.path.append('../../')
from RASPA_automation import Settings
sim = Settings.Settings['SimulationType']
data["text"] = simulation[sim]
