import sys
import numpy as np

number_of_strings = sys.argv[1:]
number_np_array = np.array([float(x) for x in number_of_strings])
print(np.linalg.norm(number_np_array))