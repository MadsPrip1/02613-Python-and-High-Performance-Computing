import sys
import numpy as np

number_of_strings = sys.argv[1:]
matrix = np.diag([float(x) for x in number_of_strings])
np.save('matrix', matrix)