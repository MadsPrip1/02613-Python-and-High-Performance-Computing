#!/bin/bash

### -- set the job Name -- 
#BSUB -J python_performance

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 5

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=10GB]"

### -- select the machine to be XeonGold6226R --
#BSUB -R "select[model==XeonGold6226R]"

### -- ask for number of cores (default: 1) -- 
#BSUB -n 1

### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o bash_output/python_performance%J.out
#BSUB -e bash_output/python_performance%J.err

### -- Need to activate the python environment --
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

### -- run in the job --
### -m cProfile will run the program
### -s cumulative will sort by cumulative time (Cumulative is including time spent in sub-functions).
python -m cProfile -s cumulative python_performance.py /dtu/projects/02613_2025/data/locations/locations_100.csv



