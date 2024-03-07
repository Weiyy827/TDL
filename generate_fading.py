import numpy as np

from SumOfSinusoid import SumOfSinusoid


def rayleigh(fd, fs, n, i, nslot):
    N1 = 20
    N2 = 21
    phi_1 = SumOfSinusoid(N1, N2, 1)[2 + 2 * i]
    phi_2 = SumOfSinusoid(N1, N2, 2)[i + 1]

    wd = 2 * np.pi * fd

    t = np.arange(nslot * n / fs, ((nslot + 1) * n) / fs, 1 / fs)
    t = t[0:n]

    I = 0
    Q = 0

    for i in range(N1):
        I += np.sqrt(2 / N1) * np.cos(wd * np.cos(np.pi * (i - 0.5) / 2 / N1) * t + phi_1[i])

    for i in range(N2):
        Q += np.sqrt(2 / N2) * np.cos(wd * np.sin(np.pi * (i - 0.5) / 2 / N2) * t + phi_2[i])

    r = (I + 1j * Q) / np.sqrt(2)

    return r


def rician(fd, fs, n, kfactor, nslot):
    N1 = 20
    N2 = 21
    phi_1 = SumOfSinusoid(N1, N2, 1)[2]
    phi_2 = SumOfSinusoid(N1, N2, 2)[1]

    wd = 2 * np.pi * fd

    t = np.arange(nslot * n / fs, ((nslot + 1) * n) / fs, 1 / fs)
    t = t[0:n]

    K = 10 ^ (np.array(kfactor) / 10)

    f_ratio = 0
    f_los = fd * f_ratio

    I = 0
    Q = 0

    for i in range(N1):
        I += np.sqrt(2 / N1) * np.cos(wd * np.cos(np.pi * (i - 0.5) / 2 / N1) * t + phi_1[i])

    for i in range(N2):
        Q += np.sqrt(2 / N2) * np.cos(wd * np.sin(np.pi * (i - 0.5) / 2 / N2) * t + phi_2[i])

    r = (I + 1j * Q) / np.sqrt(2)
    r = 1/np.sqrt(K)*r+np.exp(1j*2*np.pi*f_los*t)

    return r
