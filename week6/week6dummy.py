import ctypes
import multiprocessing as mp
import numpy as np
import sys

from time import perf_counter as time
from PIL import Image

def dummy_data():
    arr = np.arange(10) # 0 to 9
    arr = arr.astype('float32')
    arr = arr[:, None, None, None] # (10, 1, 1, 1)
    np.save('dummydata.npy', arr)

def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_

def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')

def reduce_step(args):
    b, e, s, elemshape = args # b is the current location, e is the end location for the chunk, s is the step size and elemshape is the element shape
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    
    #My code
    arr[b] = np.sum(arr[b:e:s])
    return arr[b]
   
 
if __name__ == '__main__':
    n_processes = 1
    chunk = 2
    # Create shared array
    # data = np.load(sys.argv[1])
    dummy_data()
    data = np.load('dummydata.npy')
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    # pool.map(reduce_step, [(i, i + chunk, 1, elemshape) for i in range(0, len(arr), chunk)], chunksize=1)
    arr = pool.map(reduce_step, [(i, i + chunk, 1, elemshape) for i in range(0, len(arr), chunk)], chunksize=1)     # Need to make the parameters we have to a list because pool.map expect an iterable object
    print(np.array(arr))

    # Write output
    print(time() - t)
    final_image = arr[0]

    # final_image /= len(arr) # For mean
    #Image.fromarray((255 * final_image.astype(float)).astype('uint8')).save('result.png')