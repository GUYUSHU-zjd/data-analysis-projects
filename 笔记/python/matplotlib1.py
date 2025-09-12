import numpy as np
import matplotlib.pyplot as plt

# Figure对象（包含一个或多个子图（Axes）的顶层容器。）
fig = plt.figure(facecolor='c')
# Axes（图形中的一个绘图区域，可以包含多个绘图元素（如线条、文本、标签等）。）
ax = fig.add_subplot(111) # 在画板的第1行第1列的第一个位置生成一个Axes对象来准备作画

ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')
plt.show() # 每次调用plt.show()方法后，会将所有绘图元素释放出来，所以对元素的修改应该在该方法之前

# 折线图
x=[1,2,3,4,5]
y=[2,1,3,5,4]
plt.plot(x,y,color='#A7D676',linestyle='--',marker='*',markerfacecolor='b',markersize=15)
plt.show() 

#点密集后，折线图会变得光滑
x=np.linspace(0,2*np.pi,200) # 使用linspace 函数生成从 0 到 2π 的 200 个等间隔点。
y=np.sin(x)
fig=plt.figure()
plt.plot(x,y,linestyle='-',color='c')
plt.title('Line Plot',fontsize=18) # 添加标题，字体大小设置为 18。
plt.xlabel('x',loc='right')
plt.ylabel('y',loc='top',rotation=0) # 设置 y 轴标签为 'y'，loc='top' 表示将标签放置在 y 轴的上方，rotation=0 表示不旋转标签，使其水平显示。
plt.grid(axis='y',linestyle='--',color='k',alpha=0.5) # 只显示y轴网格线

plt.show()