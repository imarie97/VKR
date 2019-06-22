import numpy as np
import time
from matplotlib import gridspec

from individual import Individual
from vector import Vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

def vizualize(v, level, name, start):

    population = [Individual.getSol(x[0]) for x in v]
    print(len(population))

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
    ax.set_xlim3d(-level, level)
    ax.set_ylim3d(-level, level)
    ax.set_zlim3d(-level, level)
    pnt3d = ax.scatter3D(xcod, ycod, zcod, c = zcod)
    plt.colorbar(pnt3d)
    cbaxes = fig.add_axes([0.07, 0.3, 0.01, 0.4])
    cb = plt.colorbar(pnt3d, cax=cbaxes)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")

    ax1 = plt.subplot(333)
    ax1.set_xlim(-level, level)
    ax1.set_ylim(-level, level)
    ax1.scatter(xcod, ycod)

    t = [round(min(xcod), 3), round(max(xcod), 3)]
    plt.xticks(t, t)

    t = [round(min(ycod), 3), round(max(ycod), 3)]
    plt.yticks(t, t)

    ax1.set_xlabel("x axis")
    ax1.set_ylabel("y axis")

    ax2 = plt.subplot(336)
    ax2.set_xlim(-level, level)
    ax2.set_ylim(-level, level)
    ax2.scatter(xcod, zcod)

    t = [round(min(xcod), 3), round(max(xcod), 3)]
    plt.xticks(t, t)
    t = [round(min(zcod), 3), round(max(zcod), 3)]
    plt.yticks(t, t)

    ax2.set_xlabel("x axis")
    ax2.set_ylabel("z axis")

    ax3 = plt.subplot(339)
    ax3.set_xlim(-level, level)
    ax3.set_ylim(-level, level)
    ax3.scatter(ycod, zcod)

    t = [round(min(ycod), 3), round(max(ycod), 3)]
    plt.xticks(t, t)
    t = [round(min(zcod), 3), round(max(zcod), 3)]
    plt.yticks(t, t)

    ax3.set_xlabel("y axis")
    ax3.set_ylabel("z axis")
    plt.show()
