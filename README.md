# ClusterAutomation
Scripts Used For Cluster Automation, Including Forcefields and Scripts for Modifying CIFs (removing charges, translating along axes etc.)


(1) Move the forcefield file to the RASPA forcefields directory.

(2) In the PBS template the HOME directry and project name should be entered.

(3) In the settings.y the 'ABSOLUTE_PATH_TO_RASPA_DIR' must be changed.

(4) Move the cifs to the raspa/structures/cif/ directory, create a list of ones to simulate in the Structures.txt file

(5) Update the simulation templates (in the templates direcotry), and specify which one to use in the settings.py document.

(6) bash Run.sh while in the RASPA_Automation directory
