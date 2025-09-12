import pandas as pd
import numpy as np

# 缺失数据处理
s1 = [1,2,3,4,5]
s2 = [2,3,None,1,None]
s3 = [7, 6.9,7.5,None,1]
s4 = [4, 6.9,3.3,7.2,4]

data = pd.DataFrame({'s1':s1,'s2':s2,'s3':s3,'s4':s4})
print(data)

# 判断方法
sdata = pd.isnull(data) # 缺省值对应的值为True，返回值为Boolean的Series或者DataFrame对象
print(sdata)
sdata = pd.notnull(data) # 缺省值对应的值为False，返回值为Boolean的Series或者DataFrame对象
print(sdata)

# 判断是否有缺失值
# pd.notnull,若包含缺省值，缺省值对应值为False
# np.all：若对象中包含假，返回False， 否则返回真
# 返回False， 说明包含缺省值
sdata = np.all(pd.notnull(data))
print(sdata)

# isnull：缺省值对应值为True
# any:对象中包含真，返回True
sdata = np.any(pd.isnull(data))
print(sdata)
# 返回False,说明不含缺省值

# 过滤数据
# 布尔索引方法 
# 获取boolean索引
sdata = np.all(data.notnull(), axis=1) # axis 在布尔索引和 dropna 方法中有不同的含义

# 获取无空值的数据
print(data[sdata])

sdata_columns = np.all(data.notnull(), axis=0)  # axis=0 表示按列操作
print("按行布尔索引筛选后的数据：\n",sdata_columns)

# 使用布尔索引按列筛选数据
filtered_data = data.loc[:, sdata_columns]  # 使用 loc 选择列
print("按列布尔索引筛选后的数据：")
print(filtered_data)




# 删除包含缺省值的行
print(data.dropna())
# 删除包含缺省值列
print(data.dropna(axis=1)) # axis参数：0或'index'：按行操作，1或'columns'：按列操作

# 填充数据
# 固定值0
print(data.fillna(0))
# 使用前一行数据填充
print(data.fillna(method='ffill'))
# 使用后一行数据填充
print(data.fillna(method='bfill'))
# 插入均值
print(data.fillna(data.mean()))