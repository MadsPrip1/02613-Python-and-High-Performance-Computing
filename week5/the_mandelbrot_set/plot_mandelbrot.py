

#real	0m4.021s
#user	0m11.314s
#sys	    0m0.195s
#
#real	0m4.017s
#user	0m11.294s
#sys	    0m0.172s
#
#real	0m4.080s
#user	0m11.756s
#sys	    0m0.181s
#
#real	0m4.310s
#user	0m12.159s
#sys	    0m0.188s
#
#real	0m4.169s
#user	0m11.172s
#sys	    0m0.177s
#
#real	0m4.154s
#user	0m11.242s
#sys	    0m0.187s
#
#real	0m4.215s
#user	0m11.535s
#sys	    0m0.191s
#
#real	0m4.164s
#user	0m11.634s
#sys	    0m0.190s
#
#real	0m4.031s
#user	0m11.288s
#sys	    0m0.180s
#
#real	0m4.060s
#user	0m11.464s
#sys	    0m0.184s


if __name__ == '__main__':

    import numpy as np
    from matplotlib import pyplot as plt
    # real, user, sys
    data_names = ['real', 'user', 'sys']
    time_all_points = np.array([[4.021, 11.314, 0.195], [4.017, 11.294, 0.172], [4.080, 11.756, 0.181], [4.310, 12.159, 0.188], [4.169, 11.172, 0.177], [4.154, 11.242, 0.187], [4.215, 11.535, 0.191], [4.164, 11.634, 0.190], [4.031, 11.288, 0.180], [4.060, 11.464, 0.184]])
    
    test_names = ['time all points']
    test_data = [time_all_points]

    x = range(time_all_points.shape[0])

    fig, ax = plt.subplots(1,3,figsize=(15,5))
    for i, (test_d, test_name) in enumerate(zip(test_data, test_names)):
        for j, data_name in enumerate(data_names):
            ax[j].plot(x, test_d[:,j])
            ax[j].set_title(test_name)
            ax[j].legend(data_name)

    plt.savefig('times_mandelbrot.png')