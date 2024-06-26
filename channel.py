import numpy as np
from scipy import signal
from generate_fading import rayleigh, rician


def channel_TDL(x: list, fd, fs, channel_model: str, ds, nslot, elevation):
    b = 0.047  # 多径功率
    d = 1.41  # 阴影标准差
    u = 0.91  # 阴影均值

    # pdp配置
    pdp = []

    # 每个仰角下的时延，功率和K因子
    pdp_elevation = {
        'NTN-TDL-A': [[0, 1.0811, 2.8416],
                      [0, -4.675, -6.482],
                      [0, 0, 0]],
        'NTN-TDL-B': [[0, 0.7249, 0.7410, 5.7392],
                      [0, -1.973, -4.332, -11.914],
                      [0, 0, 0, 0]],
        'NTN-TDL-C': [[0, 14.8124],
                      [0, -23.373],
                      [0, 10.224]],
        'NTN-TDL-D': [[0, 0.5596, 7.3340],
                      [0, -9.887, -16.771],
                      [0, 0, 11.707]]}

    for i in range(18):
        pdp.append(pdp_elevation)

    # 选择信道类型
    delay = np.array(pdp[int(elevation / 5 - 1)][channel_model][0])
    power = np.array(pdp[int(elevation / 5 - 1)][channel_model][1])
    kfactor = np.array(pdp[int(elevation / 5 - 1)][channel_model][2])

    delay = np.floor(ds * delay * fs)
    power = 10 ** (power / 10)

    # 计算衰落
    fading = np.zeros([len(delay), len(x)], dtype=complex)
    if channel_model == 'NTN-TDL-A' or 'NTN-TDL-B':
        for i in range(len(delay)):
            fading[i] = rayleigh(fd, fs, len(x), i, nslot)
    elif channel_model == 'NTN-TDL-C' or 'NTN-TDL-D':
        fading[1] = rician(fd, fs, len(x), kfactor, nslot)
        for i in range(2, len(delay)):
            fading[i] = rayleigh(fd, fs, len(x), i, nslot)

    # 过信道滤波器
    filterOut = np.zeros([len(delay), len(x)], dtype=complex)
    for i in range(len(delay)):
        filter_coeff = np.append(np.zeros(int(delay[i])), 1)
        filterOut[i] = signal.lfilter(filter_coeff, 1, x)
        filterOut[i] = filterOut[i] * fading[i]

    y = np.sum(filterOut, 0)
    return None
