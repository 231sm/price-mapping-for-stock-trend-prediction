# encoding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 导入数据
f = open('DJIA_table.csv')
df = pd.read_csv(f)               # 读入股票数据
data_open = df.iloc[:,1:2].values     # 取第3-10列
data_high = df.iloc[:,2:3].values
data_low = df.iloc[:,3:4].values
data_close = df.iloc[:,4:5].values
data_vol = df.iloc[:,5:6].values
data_adjclose = df.iloc[:,6:7].values

# 检测
# print(np.append(data_open,data_close, axis=1))
# print(type(data_close))

# 超参的设置
really_dec = -0.01
really_inc = 0.02
rick_val = 1
real_val = 0.5

# 数据处理，看是否增长
data_inc = (data_close - data_open)/data_open
data_daily = []
for i in data_inc:
	if i > really_inc:
		data_daily.append(1*real_val)
	elif i < really_dec:
		data_daily.append(0*real_val)
	else:
		data_daily.append(-1*real_val)

data_daily = np.array(data_daily).reshape(1989,1)
# print(data_daily.shape)

# 数据处理，看是否有明显的风险
data_risk = (data_high - data_low)/data_low
# print(data_risk.shape)

# 数据处理，看是否利于投资
data_future = ((data_vol - data_vol.min())/(data_vol.max() - data_vol.min()))*((data_adjclose - data_adjclose.min())/(data_adjclose.max() - data_adjclose.min()))
# print(data_future.shape)

data = np.concatenate((data_daily,data_risk,data_future,data_adjclose),axis=1)
# print(data)




