#----------------- TEMPLATE -----------------
data  = {"file_name" : "simulation_{job_number}.input"}

simulation = {"MonteCarlo": """
SimulationType                MonteCarlo


NumberOfCycles                50000
NumberOfInitializationCycles  0
PrintEvery                    1000
PrintPropertiesEvery          1000

Forcefield                   {ForcefieldName}
Framework 0
            FrameworkName                  {MOF}
            RemoveAtomNumberCodeFromLabel  yes
            UnitCells                      {countABC}

ExternalTemperature           {ExternalPressure}

Component 0 MoleculeName             CO2
            MoleculeDefinition        CO2
            WidomProbability          1.0
            CreateNumberOfMolecules   0
        """,



"MakeGrid":"""
SimulationType        MakeGrid
NumberOfCycles        50000
PrintEvery            1000
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
SpacingVDWGrid                0.1
SpacingCoulombGrid            0.1
UseChargesFromCIFFile         yes

""",

"NVT":"""
SimulationType MonteCarlo
NumberOfCycles 25000
NumberOfInitializationCycles 5000
NumberOfEquilibrationCycles 10000
PrintEvery 5000
RestartFile no
Forcefield {ForcefieldName}
ExternalTemperature {ExternalTemperature}
ExternalPressure 0


Framework 0
FrameworkName {MOF}
RemoveAtomNumberCodeFromLabel no
UnitCells {countABC}


Component 0 MoleculeName CO2
MoleculeDefinition CO2
RotationProbability 0.5
TranslationProbability 0.5
ReinsertionProbability 0.5
CreateNumberOfMolecules 1

"""
}



#----------------- SETUP -----------------
import sys
sys.path.append("../")
sys.path.append('../../')
from RASPA_automation import Settings
sim = Settings.Settings['SimulationType']
data["text"] = simulation[sim]
