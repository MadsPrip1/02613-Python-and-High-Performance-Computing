import os
import blosc
import numpy as np
import sys
from time import perf_counter
import matplotlib.pyplot as plt

def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    #os.sync()

def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
        #os.sync()

def read_numpy(file_name):
    return np.load(f"{file_name}.npy")

def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
        return blosc.unpack_array(b_arr)
    

numbers = [int(n) for n in sys.argv[1:]]
cnames = ['lz4', 'zstd']

write_numpy_arr = np.zeros(shape=(3, len(numbers)))
write_blosc_arr = np.zeros(shape=(3, len(numbers)))
read_numpy_arr  = np.zeros(shape=(3, len(numbers)))
read_blosc_arr  = np.zeros(shape=(3, len(numbers)))

for cname in cnames:
    for i, n in enumerate(numbers):

        zeros = np.zeros(shape=(n,n,n), dtype=np.uint8)
        tiled_array = np.tile(np.arange(256, dtype='uint8'), (n // 256) * n * n, ).reshape(n, n, n) # numpy.tile(A, reps) Construct an array by repeating A the number of times given by reps.
        random = np.random.randint(0, 256, size=(n, n, n), dtype=np.uint8)
        arrays = [zeros, tiled_array, random]
        arrays_name = ['zero', 'tled', 'random']
        for j, arr in enumerate(arrays):

            t_start = perf_counter()
            write_numpy(arr=arr, file_name=f'arrays/{arrays_name[j]}_numpy')
            t_write_numpy = perf_counter() - t_start
            print('Time required for write_numpy is', t_write_numpy)

            t_start = perf_counter()
            write_blosc(arr=arr, file_name=f'arrays/{arrays_name[j]}_{cname}_blosc', cname=cname)
            t_write_blosc = perf_counter() - t_start
            print('Time required for write_blosc is', t_write_blosc)

            t_start = perf_counter()
            read_numpy(file_name=f'arrays/{arrays_name[j]}_numpy')
            t_read_numpy = perf_counter() - t_start
            print('Time required for read_numpy is', t_read_numpy)

            t_start = perf_counter()
            read_blosc(file_name=f'arrays/{arrays_name[j]}_{cname}_blosc')
            t_read_blosc = perf_counter() - t_start
            print('Time required for read_blosc is', t_read_blosc)

            write_numpy_arr[j, i] = t_write_numpy
            write_blosc_arr[j, i] = t_write_blosc
            read_numpy_arr[j, i]  = t_read_numpy
            read_blosc_arr[j, i]  = t_read_blosc

    colors = ['r', 'g', 'b']
    labels = ['zeros', 'tiled_array', 'random']


    fig, ax = plt.subplots(1, 4, figsize=(20, 5))
    for j in range(len(arrays)):
        ax[0].plot(numbers, write_numpy_arr[j, :], label=f'write_numpy_{labels[j]}', color=colors[j])
        ax[1].plot(numbers, write_blosc_arr[j, :], label=f'write_blosc_{labels[j]}', linestyle='--', color=colors[j])
        ax[2].plot(numbers, read_numpy_arr[j, :], label=f'read_numpy_{labels[j]}', color=colors[j])
        ax[3].plot(numbers, read_blosc_arr[j, :], label=f'read_blosc_{labels[j]}', linestyle='--', color=colors[j])


    for i in range(4):
        ax[i].set_xlabel('n')
        ax[i].set_ylabel('Time (s)')
        ax[i].legend()
        ax[i].set_ylim(0, 5)

    ax[0].set_title(f'write_numpy')
    ax[1].set_title(f'write_blosc {cname}')
    ax[2].set_title(f'read_numpy')
    ax[3].set_title(f'read_blosc {cname}')

    plt.tight_layout()
    plt.savefig(f'figures/Compare_compression_methods_{cname}.png')
    plt.show()

