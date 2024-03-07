import func
from channel import channel_TDL
from modulation import bpskmod

# 参数设置

elevation = 50  # 用户仰角
sr = 500e6  # 采样率
m_len = 14  # M序列长度
ds = 10e-7  # 时延扩展
fd = 100  # 多普勒扩展

# 生成m序列
coeff = func.generate_coeff(m_len)
m_sequence = func.generate_m_sequence(coeff)

nslot = 2  # 每次时隙所对应的数据起始位置时间
c = 3e8  # 光速，单位m/s
d = 600  # 距离，单位km

# bpsk调制
x = bpskmod(m_sequence)

# 过TDL信道

y = channel_TDL(x, fd, sr, 'NTN-TDL-A', ds, nslot, elevation)
