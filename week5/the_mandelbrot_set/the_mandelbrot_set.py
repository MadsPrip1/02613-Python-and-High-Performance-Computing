import multiprocessing
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def generate_mandelbrot_set(points, num_processes):
    pool = multiprocessing.Pool(num_processes)
    # pool.map splits data into chunks and runs it statically by default.
    escape_times = np.array(pool.map(mandelbrot_escape_time, points))
    return escape_times

def  generate_mandelbrot_set_chunks(points, num_processes):
    chunk_size = 1000
    pool = multiprocessing.Pool(num_processes)
    escape_time = np.array(pool.map(mandelbrot_escape_time, points, chunksize=chunk_size)) # define the chunck size
    return escape_time

def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = 4

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Compute set

    #mandelbrot_set = generate_mandelbrot_set(points, num_proc)
    mandelbrot_set = generate_mandelbrot_set_chunks(points, num_proc)
    # Save set as image
    mandelbrot_set = mandelbrot_set.reshape((height, width))
    plot_mandelbrot(mandelbrot_set)