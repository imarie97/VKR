import numpy as np
from matplotlib import gridspec

from individual import Individual
from vector import Vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

def vizualize(v, name):

    population = [Individual.getSol(x[0]) for x in v]
    print(len(population))
    #
    # print(Vector.as_list(population[0]))

    xcod = [Vector.as_list(x)[0] for x in population]
    ycod = [Vector.as_list(x)[1] for x in population]
    zcod = [Vector.as_list(x)[2] for x in population]

    fig = plt.figure(name, figsize=[10, 7])
    fig.subplots_adjust(hspace=.4)
    gs = gridspec.GridSpec(2, 2,
                           width_ratios=[7, 2],
                           height_ratios=[500, 1]
                           )

    ax = plt.subplot(gs[0], projection='3d')
    # ax = fig.add_subplot(121, projection='3d')

    # ax = plt.axes(projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    pnt3d = ax.scatter3D(xcod, ycod, zcod, c = zcod)
    plt.colorbar(pnt3d)
    cbaxes = fig.add_axes([0.07, 0.3, 0.01, 0.4])
    cb = plt.colorbar(pnt3d, cax=cbaxes)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")

    ax1 = plt.subplot(333)
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.scatter(xcod, ycod)
    ax1.set_xlabel("x axis")
    ax1.set_ylabel("y axis")

    ax2 = plt.subplot(336)
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.scatter(xcod, zcod)
    ax2.set_xlabel("x axis")
    ax2.set_ylabel("z axis")

    ax3 = plt.subplot(339)
    ax3.set_xlim(-1, 1)
    ax3.set_ylim(-1, 1)
    ax3.scatter(ycod, zcod)
    ax3.set_xlabel("y axis")
    ax3.set_ylabel("z axis")

    plt.show()


if __name__=='__main__':
    vizualize([])