from vector import Vector
import numpy as np
from math import (sin, cos, radians)

from gauss import GEPP

a_par = 0.4
b_par = 0.4
c_par = 0.4
eps = 0.1
kmax = 10
zeroApproximation = Vector(0.0, 0.0, 0.0, radians(0), radians(0), radians(0))
q = []


def f1(v):
    return q[0] - (v.x + b_par * (cos(v.gamma) * sin(v.beta) * sin(v.alpha) - sin(v.gamma) * cos(v.alpha)) -
                   c_par * (sin(v.gamma) * sin(v.alpha) + cos(v.gamma) * cos(v.alpha) * sin(v.beta)))

def f2(v):
    return q[1] - (v.x - b_par * (cos(v.gamma) * sin(v.beta) * sin(v.alpha) - sin(v.gamma) * cos(v.alpha)) +
                   c_par * (sin(v.gamma) * sin(v.alpha) + cos(v.gamma) * cos(v.alpha) * sin(v.beta)))

def f3(v):
    return q[2] - (v.y + a_par * (sin(v.gamma) * cos(v.beta))
                       - c_par * (sin(v.gamma) * cos(v.alpha) * sin(v.beta) - cos(v.gamma) * sin(v.alpha)))

def f4(v):
    return q[3] - (v.y - a_par * (sin(v.gamma) * cos(v.beta))
                       + c_par * (sin(v.gamma) * cos(v.alpha) * sin(v.beta) - cos(v.gamma) * sin(v.alpha)))

def f5(v):
    return q[4] - (v.z + a_par * (-sin(v.beta)) - b_par * (cos(v.beta) * sin(v.alpha)))


def f6(v):
    return q[5] - (v.z - a_par * (-sin(v.beta)) + b_par * (cos(v.beta) * sin(v.alpha)))


def f1_x(v):
    return -1

def f1_y(v):
    return 0

def f1_z(v):
    return 0

def f1_alpha(v):
    return -b_par * (cos(v.gamma) * sin(v.beta) * cos(v.alpha) + sin(v.gamma) * sin(v.alpha)) \
           + c_par * (sin(v.gamma) * cos(v.alpha) - cos(v.gamma) * sin(v.alpha) * sin(v.beta))

def f1_beta(v):
    return -b_par * (cos(v.gamma) * cos(v.beta) * sin(v.alpha)) \
           + c_par * cos(v.gamma) * cos(v.alpha) * cos(v.beta)

def f1_gamma(v):
    return b_par * (sin(v.gamma) * sin(v.beta) * sin(v.alpha) + cos(v.gamma) * cos(v.alpha)) \
           + c_par * (cos(v.gamma) * sin(v.alpha) - sin(v.gamma) * cos(v.alpha) * sin(v.beta))


def f2_x(v):
    return -1

def f2_y(v):
    return 0

def f2_z(v):
    return 0

def f2_alpha(v):
    return b_par * (cos(v.gamma) * sin(v.beta) * cos(v.alpha) + sin(v.gamma) * sin(v.alpha)) \
           - c_par * (sin(v.gamma) * cos(v.alpha) - cos(v.gamma) * sin(v.alpha) * sin(v.beta))

def f2_beta(v):
    return b_par * (cos(v.gamma) * cos(v.beta) * sin(v.alpha)) \
           -c_par * (cos(v.gamma) * cos(v.alpha) * cos(v.beta))

def f2_gamma(v):
    return -b_par * (sin(v.gamma) * sin(v.beta) * sin(v.alpha) + cos(v.gamma) * cos(v.alpha)) \
           -c_par * (cos(v.gamma) * sin(v.alpha) - sin(v.gamma) * cos(v.alpha) * sin(v.beta))

def f3_x(v):
    return 0

def f3_y(v):
    return -1

def f3_z(v):
    return 0

def f3_alpha(v):
    return -c_par * (cos(v.gamma) * cos(v.alpha) + sin(v.gamma) * sin(v.alpha) * sin(v.beta))

def f3_beta(v):
    return a_par * (sin(v.gamma) * sin(v.beta)) + c_par * (sin(v.gamma) * cos(v.alpha) * cos(v.beta))

def f3_gamma(v):
    return -a_par * (cos(v.gamma) * cos(v.beta)) \
           + c_par * (sin(v.gamma) * sin(v.alpha) + cos(v.gamma) * cos(v.alpha) * sin(v.beta))

def f4_x(v):
    return 0

def f4_y(v):
    return -1

def f4_z(v):
    return 0

def f4_alpha(v):
    return c_par * (sin(v.gamma) * sin(v.alpha) * sin(v.beta) + cos(v.gamma) * cos(v.alpha))

def f4_beta(v):
    return -a_par * (sin(v.gamma) * sin(v.beta)) - c_par * (sin(v.gamma) * cos(v.alpha) * cos(v.beta))

def f4_gamma(v):
    return a_par * (cos(v.gamma) * cos(v.beta)) \
           - c_par * (cos(v.gamma) * cos(v.alpha) * sin(v.beta) + sin(v.gamma) * sin(v.alpha))


def f5_x(v):
    return 0

def f5_y(v):
    return 0

def f5_z(v):
    return -1

def f5_alpha(v):
    return b_par * (cos(v.alpha) * cos(v.beta))

def f5_beta(v):
    return a_par * (cos(v.beta)) - b_par * (sin(v.beta) * sin(v.alpha))

def f5_gamma(v):
    return 0


def f6_x(v):
    return 0

def f6_y(v):
    return 0

def f6_z(v):
    return -1

def f6_alpha(v):
    return -b_par * (cos(v.alpha) * cos(v.beta))

def f6_beta(v):
    return -a_par * cos(v.beta) + b_par * (sin(v.alpha) * sin(v.beta))

def f6_gamma(v):
    return 0


def row1(v):
    return np.array([f1_x(v), f1_y(v), f1_z(v), f1_alpha(v), f1_beta(v), f1_gamma(v)])

def row2(v):
    return np.array([f2_x(v), f2_y(v), f2_z(v), f2_alpha(v), f2_beta(v), f2_gamma(v)])

def row3(v):
    return np.array([f3_x(v), f3_y(v), f3_z(v), f3_alpha(v), f3_beta(v), f3_gamma(v)])

def row4(v):
    return np.array([f4_x(v), f4_y(v), f4_z(v), f4_alpha(v), f4_beta(v), f4_gamma(v)])

def row5(v):
    return np.array([f5_x(v), f5_y(v), f5_z(v), f5_alpha(v), f5_beta(v), f5_gamma(v)])

def row6(v):
    return np.array([f6_x(v), f6_y(v), f6_z(v), f6_alpha(v), f6_beta(v), f6_gamma(v)])

def b(v):
    return np.array([[-f1(v)], [-f2(v)] ,[-f3(v)] ,[-f4(v)] ,[-f5(v)] ,[-f6(v)]])


def jacobi(v):
    matrix = np.zeros(shape=(6,6))

    matrix[0] = row1(v)
    matrix[1] = row2(v)
    matrix[2] = row3(v)
    matrix[3] = row4(v)
    matrix[4] = row5(v)
    matrix[5] = row6(v)

    return matrix


def newton(q0, a_p, b_p, c_p):
    global q, a_par, b_par, c_par
    q, a_par, b_par, c_par = q0, a_p, b_p, c_p
    oldvec = zeroApproximation
    for k in range(0, kmax):
        a = jacobi(oldvec)
        b1 = b(oldvec)

        GaussElimPiv = GEPP(a, b1)
        deltavec = GaussElimPiv.get_res()

        newvec = oldvec + deltavec

        if max_delta(newvec, oldvec) < eps:
            return newvec
        else: oldvec = newvec

    return oldvec

def max_delta(newvec, oldvec):
    maxdelta = 0.0

    for i in range(0, 6):
        curdelta = abs(newvec[i] - oldvec[i])
        if curdelta > maxdelta:
            maxdelta = curdelta

    return maxdelta