import sys
import numpy as np

# The input to the program is the path to a file containing a numpy matrix and an integer p.
# python program.py path/to/data.txt p

path_to_matrix = sys.argv[1]
matrix = np.load(path_to_matrix)
np.save('cols', np.mean(matrix, axis=0))
np.save('rows', np.mean(matrix, axis=1))