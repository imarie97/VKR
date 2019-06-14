from math import (radians, degrees, sqrt, pow)
class Vector():
    def __init__(self, x=0, y=0, z=0, alpha=0, beta=0, gamma=0):
        self.x, self.y, self.z, self.alpha, self.beta, self.gamma = x, y, z, alpha, beta, gamma

    # переопределяем '+'
    def __add__(self, V):
        added = Vector(self.x + V.x, self.y + V.y, self.z + V.z, self.alpha + V.alpha, self.beta + V.beta, self.gamma +V.gamma)
        return added

    # переопределяем '-' для координат
    def __sub__(self, V):
        subed = Vector(self.x - V.x, self.y - V.y, self.z - V.z)
        return subed

    # переопределяем '**' для координат (возведение в квадрат)
    def __pow__(self, p):
        p = pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)
        return p

    def __truediv__(self, d):
        return Vector(self.x / d, self.y / d, self.z / d, 0,0,0)

    # overload []
    def __getitem__(self, index):
        data = [self.x, self.y, self.z, self.alpha, self.beta, self.gamma]
        return data[index]

    def constraints_satisfy(self, limit):
        degs = to_degrees(self)
        l1 = limit[0]
        l2 = limit[1]
        l3 = limit[2]
        alpha = limit[3]
        beta = limit[4]
        gamma = limit[5]
        if (-l1 < self.x < l1) & (-l2 < self.y < l2) & (-l3 < self.z < l3) & \
                (-alpha <= degs[0] <= alpha) & (-beta <= degs[1] <= beta) & (-gamma <= degs[2]<= gamma):
            return True
        else:
            return False

    # overload set []
    def __setitem__(self, key, item):
        if (key == 0):
            self.x = item
        elif (key == 1):
            self.y = item
        elif (key == 2):
            self.z = item
        elif (key == 3):
            self.alpha = item
        elif (key == 4):
            self.beta = item
        elif (key == 5):
            self.gamma = item

    def __str__(self):
        degs = to_degrees(self)
        return "Vector (%s, %s, %s, %s, %s, %s)" % (self.x, self.y, self.z, degs[0], degs[1], degs[2])

    def as_list(self):
        degs = to_degrees(self)
        return [self.x, self.y, self.z, degs[0], degs[1], degs[2]]


def to_degrees(v):
    a = degrees(v.alpha) % 360
    b = degrees(v.beta) % 360
    g = degrees(v.gamma) % 360
    if a > 180:
        a = - (360.0 - a)
    if b > 180:
        b = - (360.0 - b)
    if g > 180:
        g = - (360.0 - g)
    return [a, b, g]