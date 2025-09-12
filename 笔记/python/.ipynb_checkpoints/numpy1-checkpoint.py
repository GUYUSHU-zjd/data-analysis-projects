import numpy as np
#数组的创建：
# 一维数组
data_1 = np.array([1,2,3,4])
print(data_1)
data_1 = np.arange(1,10,2)
print(data_1)

# 二维数组
data_2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
print(data_2)

# 全0数组
#shape代表形状，比如我这里创建的就是2行三列的2维数组
data_3 = np.zeros(shape=(2,3))
print(data_3)

# 全1数组
data_4 = np.ones(shape=(2,3))
print(data_4)

# 全空数组
data_5 = np.empty(shape=(2,3))
print(data_5)

# 有连续序列的数组 arange
data_6 = np.arange(10,16,2) # 10-16的数据，步长为2
print(data_6)

# 有连续间隔的数组 linspace 
# 创建线段型数据
data_7= np.linspace(1,10,10) # 开始端1，结束端10，且分割成10个数据，生成线段
print(data_7)

# 随机数组
data_8 = np.random.rand(3,4) # 3行4列的随机数组
print(data_8)
data_8=np.random.randint(2,5,size=(3,4)) # 3行4列,每个元素值在2~5之间的随机数组
print(data_8)

# 改变数组形状
data1=[1,2,3,4,5]
data2=[1,2,3,4,5]
data=np.array([data1,data2])
print("改之前的数组形状为:")
print(data.shape)
data=data.reshape((5,2))
print("改之后的数组形状为:")
print(data.shape)

# 数组转置
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_array = np.array(data)
print("没有转置数组之前数组为：")
print(data)
print("转置数组之后数组为：")
print(data_array.T)

# 数组的查看：
# 数组维度 ndim
print(data_1.ndim)
# 数组形状shape
print(data_1.shape)
# 数组中元素个数
print(data_1.size)
# 数组的数据类型 dtype
print(data_1.dtype)

#数组的运算：
# 数组相加
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)
# 数组相乘
result=array1*array2
print(result)

# 数据统计：