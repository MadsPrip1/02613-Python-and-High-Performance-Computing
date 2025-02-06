#!/bin/bash

### -- set the job Name -- 
#BSUB -J sleeper

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 2

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=512MB]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60

