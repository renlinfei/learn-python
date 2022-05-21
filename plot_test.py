from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')

# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x, np.sin(x))
# plt.show()

# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
plt.figure(1, dpi=50)
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))
# plt.show()

# 直方图
# data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6]
# plt.hist(data)
# plt.show()

# 散点图
# x = np.arange(1, 10)
# y = x
# plt.scatter(x, y, c='r', marker='o') # c='r'表示散点颜色为红色 marker表示指定散点形状为圆形
# plt.show()

# iris = pd.read_csv('./iris_training.csv')
# print(iris.head())
# # 绘制散点图
# iris.plot(kind='scatter', x='120', y='4')
# plt.show()


# iris = pd.read_csv('./iris_training.csv')
# # 设置样式
# sb.set(style='white', color_codes=True)
# # 设置绘制格式为散点图
# sb.jointplot(x='120', y='4', data=iris, size=5)
# # dispplot绘制曲线
# sb.distplot(iris['120'])
# plt.show()

# FaceGrid一般绘制函数
# hue彩色显示分类0/1/2
# plt.scatter绘制散点图
# add_legend（）显示分类的描述信息
iris = pd.read_csv('./iris_training.csv')
sb.set(style='white', color_codes=True)
sb.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, "120", "4").add_legend()

plt.show()

