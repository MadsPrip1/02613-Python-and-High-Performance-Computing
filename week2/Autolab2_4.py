import sys
import numpy as np

path_to_matrix = sys.argv[1]
matrix = np.load(path_to_matrix)
np.save('cols', np.mean(matrix, axis=0))
np.save('rows', np.mean(matrix, axis=1))