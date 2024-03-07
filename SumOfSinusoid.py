import numpy as np


def SumOfSinusoid(N1, N2, j: int):
    if j == 1:
        sosPhi = np.zeros([200, N1])
        for i in range(sosPhi.shape[0]):
            sosPhi[i] = 2 * np.pi * np.random.rand(1, N1)
    else:
        sosPhi = np.zeros([200, N2])
        for i in range(sosPhi.shape[0]):
            sosPhi[i] = 2 * np.pi * np.random.rand(1, N2)

    return sosPhi
