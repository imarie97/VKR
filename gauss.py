import numpy as np
from vector import Vector

class GEPP():
    """
    input: A -- n x n матрица
           b -- n x 1 столбец
    output: x -- решение Ax=b
    """
    def __init__(self, A, b, doPricing=True):
        #super(GEPP, self).__init__()

        self.A = A
        self.b = b
        self.doPricing = doPricing

        self.n = None                   # n -- размер A
        self.x = None

        self._validate_input()          # валидация input'a
        self._elimination()             # method that conducts elimination
        self._backsub()                 # method that conducts back-substitution

    def _validate_input(self):
        self.n = len(self.A)
        if self.b.size != self.n:
            raise ValueError("Invalid argument: incompatible sizes between" +
                             "A & b.", self.b.size, self.n)

    def _elimination(self):

        for k in range(self.n - 1):
            if self.doPricing:
                # Pivot
                maxindex = abs(self.A[k:, k]).argmax() + k
                if self.A[maxindex, k] == 0:
                    raise ValueError("Matrix is singular.")
                # Swap
                if maxindex != k:
                    self.A[[k, maxindex]] = self.A[[maxindex, k]]
                    self.b[[k, maxindex]] = self.b[[maxindex, k]]
            else:
                if self.A[k, k] == 0:
                    raise ValueError("Pivot element is zero. Try setting doPricing to True.")
            # Eliminate
            for row in range(k + 1, self.n):
                multiplier = self.A[row, k] / self.A[k, k]
                self.A[row, k:] = self.A[row, k:] - multiplier * self.A[k, k:]
                self.b[row] = self.b[row] - multiplier * self.b[k]

    def _backsub(self):

        self.x = np.zeros(self.n)
        for k in range(self.n - 1, -1, -1):
            self.x[k] = (self.b[k] - np.dot(self.A[k, k + 1:], self.x[k + 1:])) / self.A[k, k]

    def get_res(self):
        res = Vector(self.x[0], self.x[1], self.x[2], self.x[3], self.x[4], self.x[5])
        return res

def main():
    A = np.array([[1., -1., 1., -1.],
                  [1., 0., 0., 0.],
                  [1., 1., 1., 1.],
                  [1., 2., 4., 8.]])
    b = np.array([[14.],
                  [4.],
                  [2.],
                  [2.]])

    GaussElimPiv = GEPP(np.copy(A), np.copy(b), doPricing=False)
    print(GaussElimPiv.x)
    print(GaussElimPiv.A)
    print(GaussElimPiv.b)
    GaussElimPiv = GEPP(A, b)
    print(GaussElimPiv.x)

if __name__ == "__main__":
    main()