#!/bin/bash

#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model==XeonE5_2660v3]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
#BSUB -B

lscpu
sleep 60

