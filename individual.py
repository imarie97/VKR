from math import (radians, degrees, sqrt, pow)

class Individual():
    def __init__(self, qs, sol):
        # lists
        self.qs = qs
        self.sol = sol

    def getQ(self):
        return self.qs

    def getSol(self):
        return self.sol

    def __str__(self):
        return "Individual (%s, %s)" % (self.qs, self.sol)
