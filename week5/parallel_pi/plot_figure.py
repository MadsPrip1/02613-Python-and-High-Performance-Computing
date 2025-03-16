# # 1
# real	0m0.783s
# user	0m0.771s
# sys	    0m0.005s

# real	0m0.169s
# user	0m0.718s
# sys	    0m0.046s

# real	0m48.894s
# user	1m9.278s
# sys	    0m24.223s

# # 2
# real	0m0.763s
# user	0m0.751s
# sys 	0m0.003s

# real	0m0.183s
# user	0m0.719s
# sys	    0m0.042s

# real	0m49.768s
# user	1m9.601s
# sys	    0m24.572s

# # 3
# real	0m0.762s
# user	0m0.747s
# sys 	0m0.003s

# real	0m0.172s
# user	0m0.713s
# sys	    0m0.043s

# real	0m56.734s
# user	1m22.776s
# sys	    0m27.364s

# # 4
# real	0m0.809s
# user	0m0.791s
# sys 	0m0.005s

# real	0m0.167s
# user	0m0.726s
# sys	    0m0.037s

# real	0m49.646s
# user	1m9.852s
# sys	    0m24.372s

# # 5
# real	0m0.762s
# user	0m0.745s
# sys	    0m0.005s

# real	0m0.172s
# user	0m0.704s
# sys	    0m0.050s

# real	0m49.029s
# user	1m9.245s
# sys	    0m24.092s

# # 6
# real	0m0.766s
# user	0m0.753s
# sys 	0m0.005s

# real	0m0.165s
# user	0m0.709s
# sys	    0m0.043s

# real	0m53.308s
# user	1m18.045s
# sys	    0m26.799s

# # 7
# real	0m0.765s
# user	0m0.745s
# sys 	0m0.008s

# real	0m0.173s
# user	0m0.709s
# sys	    0m0.045s

# real	0m55.124s
# user	1m18.366s
# sys	    0m26.956s

# # 8
# real	0m0.773s
# user	0m0.761s
# sys	    0m0.004s

# real	0m0.166s
# user	0m0.728s
# sys	    0m0.036s

# real	0m55.467s
# user	1m19.181s
# sys	    0m27.342s

# # 9
# real	0m0.790s
# user	0m0.771s
# sys	    0m0.008s

# real	0m0.171s
# user	0m0.713s
# sys	    0m0.041s

# real	0m51.351s
# user	1m16.045s
# sys	    0m26.600s

# # 10
# real	0m0.802s
# user	0m0.787s
# sys 	0m0.008s

# real	0m0.166s
# user	0m0.724s
# sys	    0m0.041s

# real	0m50.140s
# user	1m10.202s
# sys	    0m24.399s



if __name__ == '__main__':

    import numpy as np
    from matplotlib import pyplot as plt
    # real, user, sys
    data_names = ['real', 'user', 'sys']
    time_serial = np.array([[0.783, 0.771, 0.005], [0.763, 0.751, 0.003], [0.762, 0.747, 0.003], [0.809, 0.791, 0.005], [0.762, 0.745, 0.005], [0.766, 0.753, 0.005], [0.765, 0.745, 0.008], [0.773, 0.761, 0.004], [0.790, 0.771, 0.008], [0.802, 0.787, 0.008]])
    time_chunked = np.array([[0.169, 0.718, 0.046], [0.183, 0.719, 0.042], [0.172, 0.713, 0.043], [0.167, 0.726, 0.037], [0.172, 0.704, 0.050], [0.165, 0.709, 0.043], [0.173, 0.709, 0.045], [0.166, 0.728, 0.036], [0.171, 0.713, 0.041], [0.166, 0.724, 0.041]])
    time_parallel = np.array([[48.894, 60+9.278, 24.223], [49.768, 60+9.601, 24.572], [56.734, 60+22.776, 27.364], [49.646, 60+9.852, 24.372], [49.029, 60+9.245, 24.092], [53.308, 60+18.045, 26.799], [55.124, 60+18.366, 26.956], [55.467, 60+19.181, 27.342], [51.351, 60+16.045, 26.600], [50.140, 60+10.202, 24.399]])
    
    test_names = ['serial', 'chunked', 'parallel']
    test_data = [time_serial, time_chunked, time_parallel]
    x = range(time_serial.shape[0])

    fig, ax = plt.subplots(3,3,figsize=(15,15))
    for i, (test_d, test_name) in enumerate(zip(test_data, test_names)):
        for j, data_name in enumerate(data_names):
            ax[i,j].plot(x, test_d[:,j])
            ax[i,j].set_title(test_name)
            ax[i,j].legend(data_name)

    plt.savefig('plot.png')
