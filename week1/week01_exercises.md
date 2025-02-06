# Exercises for Week 1

## 1. Connecting and transferring fles to the HPC

The focus of this exercise is to learn how to connect to the HPC nodes, transfer fles and run code on the HPC, preferably using the terminal.

1. **<span style="color:#990000;">Autolab</span>** Write a Python program that writes "Hello world" to a fle (e.g., called 'content.txt'). It should also print the same text to the screen.

The result can be seen in the ``write_to_context.py``

2. Transfer your Python fle to the HPC using scp, sfp, FileZilla, or other (see guide [File Transfer to/from HPC](https://learn.inside.dtu.dk/d2l/le/lessons/242101/topics/920710)  on Learn).

To transfer my files I use the following code:
``scp path/to/file.py <username>@login.hpc.dtu.dk:path/to/file.py ``

3. Connect to an HPC terminal (see guide [Connecting to an HPC Terminal](https://learn.inside.dtu.dk/d2l/le/lessons/242101/topics/920710) on Learn). If you are not on a DTU network, you may need to use a VPN or set up SSH keys - see the guide. If you used SSH, make sure you called linux sh so you are not on a login node.

``ssh <username>@login.hpc.dtu.dk``

4. Create and/or navigate to your working directory (on the HPC) for this exercise (see guide [Linux Terminal Cheat Sheet](https://learn.inside.dtu.dk/d2l/le/lessons/242101/topics/920711) on Learn).

Use the ``cd`` command

5. Initialize the course conda environment (see guide [Initializing the 02613 Conda Environment](https://learn.inside.dtu.dk/d2l/le/lessons/242101/topics/920713) on Learn).

I use the following command
``source /dtu/projects/02613_2025/conda/conda_init.sh``
``conda activate 02613``

6. Run your Python program.

Use the ``python write_to_content.py``

7. Transfer the generated fle (e.g., content.txt) back to your local computer.

Use the following command on my local pc
``scp <username>@login.hpc.dtu.dk:Documents/02613_PyHPC/compute_from_hpc.py compute_from_hpc.py``

## 2. Job Scripts

For all scripts below, use /bin/sleep 60 (or a longer period, like 100 or 120 seconds) as the com mand to run, and use ‘hpc’ as the queue name (except if stated otherwise).

1. **<span style="color:#990000;">Autolab</span>** Write a simple job script, like the one shown in the lectur and submit it.

It is called ``submit.sh``

- a) Check the status with bstat and/or bjobs. Use 'man bjobs', to get information about the options or check the [online documentation](https://www.ibm.com/docs/en/spectrum-lsf/10.1.0?topic=bjobs-options).

- b) You can add a walltime limit to the script. Can you see that limit in the bstat or the bjobs output?

If I use ``bjobs -l`` there is a  **RUNLIMIT 2.0 min** section

2. **<span style="color:#990000;">Autolab</span>** Write a job script that sends you notifcations when the job starts and ends - see 'man bsub' for the details or check the [online documentation](https://www.ibm.com/docs/en/spectrum-lsf/10.1.0?topic=bsub-options). Take a look at the job summary, i.e. what information can you retrieve from that?

The file for this is called ``submit2.sh``

``-B``
Sends mail to you when the job is dispatched and begins execution.
``-N``
Sends the job report to you by mail when the job finishes.


- a) To test, increase the period in the sleep command to be longer than the wall time limit, and submit the job again. What happens?

I get the following message:
*TERM_RUNLIMIT: job killed after reaching LSF run time limit.Exited with exit code 140.*

3. The default hpc queue has nodes of diferent type, e.g. with diferent CPUs. The CPU type can be requested as a feature in a command script.

It is ``submit3.sh``

- a) **<span style="color:#990000;">Autolab</span>** Use the nodestat command to check which CPU types are available in the hpc queue, and then submit a job script that requests one of the types. See the [Batch Jobs under LSF 10](https://www.hpc.dtu.dk/?page_id=1416) webpage for information on how to do that.

I use ``nodestat -F hpc``


b) Add the necessary commands to your job script, to print the CPU type - and check in the job output that your job did indeed run on a node with the requested feature. Note: there is slight diference in the type request and the type variable: the variable contains a '-', while LSF uses a '_'.

I have added ``lscpu`` to the ``submit3.sh``

The next exercises are a preparation for later weeks, where we want to submit multi-core jobs to the batch system:

4.  **<span style="color:#990000;">Autolab</span>** Write a job script that requests 1 node and 4 cores.

To request 1 node I use ``#BSUB -R "span[hosts=1]"`` since one node is one computer/host

The number of cores is set using ``#BSUB -n 4``

5. **<span style="color:#990000;">Autolab</span>** Write a job script, requesting 1 node and 16 cores. Does it run? If the job doesn't start,use ‘bjobs -p' to check for the reason.

To request 1 node I use ``#BSUB -R "span[hosts=1]"`` since one node is one computer/host
I set the following parameter to 16
``#BSUB -n 16``
yes it will run (I have 48 nodes, can be seen using ``bpeek``)
If the job is just appending we will use ``bjobs -p`` where I get the following message:
*Not enough hosts to meet the job's spanning requirement;*

6. **<span style="color:#990000;">Autolab</span>** Write a job script, requesting 1 node and 64 cores. Does it run? If the job doesn't start,use the bjobs -p command to check for the reason.

To request 1 node I use ``#BSUB -R "span[hosts=1]"`` since one node is one computer/host
I set the following parameter to 64 cores
``#BSUB -n 64``

If i use ``bjobs -p`` then I get the following error
*Not enough hosts to meet the job's spanning requirement;*
Meaning there does not exist any host with 64 cores

Clean up:

7. Check all your submitted jobs with 'bstat' again. If there are any lef, that still are in status 'PEND', please remove them with 'bkill JOBID' (the JOBID is the number in the frst column of the 'bstat'/'bjobs' output).

**Hints:** to get the informations needed, use the 'man' command and take a look at the DTU Computing Center webpages https://www.hpc.dtu.dk/?page_id=2534



