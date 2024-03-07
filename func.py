import numpy as np


def generate_coeff(m_len: int):
    table = [
        [0, 0, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1]]
    return table[m_len - 4]


def generate_m_sequence(coeff: list):
    coeff_len = len(coeff)
    m_len = 2 ** coeff_len - 1
    m = []
    register = np.zeros(coeff_len)
    register[0] = 1
    register[-1] = 1

    for i in range(m_len):
        m.append(register[coeff_len-1])
        result = np.mod(sum(coeff * register), 2)
        register[1:len(register)] = register[0:len(register)-1]
        register[0] = result
    return m