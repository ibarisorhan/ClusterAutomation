# ClusterAutomation
Repo includes scripts used for cluster automation, including forcefields and scripts for modifying CIFs (removing charges, translating along axes etc.)
<br>
<br>
For RASPA simulation automation, use the RASPA_Automation directory in this repo and follow the steps below:
<ol>
<li>Move the forcefield file (in ./Extras/Automation_Script/)to the RASPA forcefields directory.</li>
<li>In the PBS template the HOME directry and project name MUST be entered.</li>
<li>In the settings.y the 'ABSOLUTE_PATH_TO_RASPA_DIR' must be changed.</li>
<li>Move the cifs to the raspa/structures/cif/ directory, create a list of ones to simulate in the ./Queu/Structures.txt file.</li>
<li>Update the simulation templates (in the templates directory), and specify which one to use in the settings.py document.</li>
<li>bash Run.sh while in the RASPA_Automation directory (Optional: From the "Other" folder, the Recursive_Queue_Task.txt task can be moved to the RASPA automation folder and sent to queue. This will recursively call itself to run Run.sh in the time frame in the script! Be sure to change the project title in the document if used)</li>
</ol>



<br>
<br>
The "Other" directory has the scripts for removing charges from cif files (necessary for zeo++ simulations), automation scripts used in Zeo++, shifting mofs such that atoms have squared sums closes to axes, etc. 
<br>


For gathering geomteric features:
<ol>
<li> Install Zeo++</li>
<li> Create a new directory with cif files that will be analysed</li>
<li> If applicable, remove charges from cifs</li>
<li> Copy network binary from zeo++ to the new directory</li>
<li>Change the PBS file's project name</li>
<li> qsub PBS.txt to run</li>
</ol>
