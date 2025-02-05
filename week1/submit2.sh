#!/bin/bash

#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
#BSUB -B
#BSUB -N

sleep 180

