import pandas as pd
import numpy as np

# Series数据结构
# Series：一维的带索引数据结构(单列)
# 第一列为索引，第二列为Series数据
sdata = pd.Series(np.arange(1,4), index=list('abc'))
print(sdata)
# index查看下标(索引/标签)，values查看下标的值()
print(sdata.index)
print(sdata.values)
# iloc and loc的使用
# iloc是原下标，也就是默认值，计算机的记忆
# loc是修改过的下标，我们把他叫作标签，标签是由我们自主给的，计算机并不会自己产生
print(sdata.iloc[0])
# 使用标签[a,b,c]
print(sdata['b'])
# 使用loc方式，只能使用标签
print(sdata.loc['c'])

# 创建对象
s1 = pd.Series({"小李":90,"小王":85}) #前键后值
print(s1)
# 使用loc修改数据
s1.loc["小李"]=100
print("小李的成绩：",s1.loc["小李"])

# 数据相加、相减、相乘、相除
# 标签会自动对应
s2 = pd.Series([1,2,3,4,5],index=[1,2,3,4,5])
s3 = pd.Series([2,3,1,6,4],index=[2,1,3,5,6])
print(s2+s3) # 使用这种相加，没有对应标签的情况下会错误，显示NAN
print(s2.add(s3,fill_value=0)) # s2.add（s3，fill_value = “如果出现没有值的情况，以0代替”）
# 同理
print(s2.sub(s3,fill_value=0))
print(s2.mul(s3,fill_value=1)) # 需注意的是，乘除不要设为0
print(s2.div(s3,fill_value=1))

# 求最大值、最小值、求和值、平均值
print(s2.max())
print(s2.min())
print(s2.sum())
print(s2.mean())

# DataFrame创建二维数组
# 一维数据
data = pd.DataFrame(data=np.arange(1,5))
print(data)
# 多维数据 data为4X4
data = np.arange(16).reshape(4,4)
data = pd.DataFrame(data=data)
print(data)
# 设置index与columns
data = np.arange(16).reshape(4,4)
df = pd.DataFrame(data=data, index=list('abcd'), columns=['c1','c2','c3','c4'])
print(df)
# 
s_id = pd.Series(["01","02","03","04"],index=["小明","小李","小红","小王"])
s_class = pd.Series(["一班","二班","三班","一班"],index=["小明","小李","小红","小王"])
s_grade = pd.Series([92,89,95,87],index=["小明","小李","小红","小王"])
df = pd.DataFrame({"学号":s_id,"班级":s_class,"成绩":s_grade})
print(df)


# 查看行
print(df.index)
# 查看列
print(df.columns)
# 查看数据
print(df.values)
# 数据倒置(行列转换)
print(df.T)

# 切片
# 标签切片
print(df.loc["小明":"小红"])
# 下标切片
print(df.iloc[0:3])
# 行列切片
print(df.loc["小明":"小红","学号":"班级"])
# 行列切片(下标)
print(df.iloc[0:2,0:2])

