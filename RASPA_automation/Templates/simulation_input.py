#----------------- TEMPLATE -----------------
data  = {"file_name" : "simulation_{job_number}.input"}

simulation = {
"MonteCarlo" : """

SimulationType                MonteCarlo
NumberOfCycles                10000
NumberOfInitializationCycles  2500
PrintEvery                    5000
RestartFile                   no

Forcefield                    {ForcefieldName}
UseChargesFromCIFFile         yes

Framework 0
FrameworkName {MOF}
UnitCells {countABC}
ExternalTemperature {ExternalTemperature}
ExternalPressure {ExternalPressure}

Component 0 MoleculeName             CO2
            MoleculeDefinition       CO2
            FugacityCoefficient      1.0
            TranslationProbability   0.5
            RotationProbability      0.5
            ReinsertionProbability   0.5
            SwapProbability          1.0
            CreateNumberOfMolecules  0


""",
            
            
"Henry298K": """
SimulationType                MonteCarlo
NumberOfCycles                20000
NumberOfInitializationCycles  0
PrintEvery                    1000
PrintPropertiesEvery          1000

Forcefield                    AutomationScript

Framework 0
FrameworkName {MOF}
RemoveAtomNumberCodeFromLabel no
UnitCells {countABC}
ExternalTemperature 298

Component 0 MoleculeName             CO2
            MoleculeDefinition       CO2
            IdealGasRosenbluthWeight 1
            WidomProbability         1.0
            CreateNumberOfMolecules  0

"""
}



#----------------- SETUP -----------------
import sys
sys.path.append("../")
sys.path.append('../../')
from RASPA_automation import Settings
sim = Settings.Settings['SimulationType']
data["text"] = simulation[sim]
