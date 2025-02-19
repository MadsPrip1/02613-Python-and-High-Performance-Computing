import os
import blosc
import numpy as np
import sys
from time import perf_counter

def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()

def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
        os.sync()

def read_numpy(file_name):
    return np.load(f"{file_name}.npy")

def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
        return blosc.unpack_array(b_arr)
    
n = int(sys.argv[1])

zeros = np.zeros(shape=(n,n,n)).astype('unit8')

t_start = perf_counter()
write_numpy(zeros, 'arrays/write_numpy')
print('Time required for write_numpy is', perf_counter() - t_start)

t_start = perf_counter()
write_blosc(zeros, 'arrays/write_blosc')
print('Time required for write_blosc is', perf_counter() - t_start)

t_start = perf_counter()
read_numpy(zeros, 'arrays/read_numpy')
print('Time required for read_numpy is', perf_counter() - t_start)

t_start = perf_counter()
read_blosc(zeros, 'arrays/read_blosc')
print('Time required for read_blosc is', perf_counter() - t_start)