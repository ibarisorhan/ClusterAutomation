# ClusterAutomation
Repo includes scripts used for cluster automation, including forcefields and scripts for modifying CIFs (removing charges, translating along axes etc.)


For RASPA simulation automation, use the RASPA_Automation direcoty in this repo and follow the steps below:

(1) Move the forcefield file (in ./Extras/Automation_Script/)to the RASPA forcefields directory.

(2) In the PBS template the HOME directry and project name should be entered.

(3) In the settings.y the 'ABSOLUTE_PATH_TO_RASPA_DIR' must be changed.

(4) Move the cifs to the raspa/structures/cif/ directory, create a list of ones to simulate in the Structures.txt file

(5) Update the simulation templates (in the templates direcotry), and specify which one to use in the settings.py document.

(6) bash Run.sh while in the RASPA_Automation directory



The "Other" directory has the scripts for removing charges from cif files (necessary for zeo++ simulations), automation scripts used in Zeo++, shifting mofs such that atoms have squared sums closes to axes, etc. 
