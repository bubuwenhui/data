import numpy as np
# matrix = np.array([
# 	[2, 4, 8,16],
# 	[12, 9, 13,15],
# 	[12, 13, 7,16],
# 	[12, 13, 14,16],
# 	])
# for i in range(1,len(matrix)-1):
# 	for j in range(1,len(matrix[0])-1):
# 		if matrix[i][j]<matrix[i-1][j] and matrix[i][j]<matrix[i+1][j] and matrix[i][j]<matrix[i][j-1] and matrix[i][j]<matrix[i][j+1] \
# 				and matrix[i][j]<matrix[i-1][j-1] and matrix[i][j]<matrix[i-1][j+1] and matrix[i][j]<matrix[i+1][j-1] and matrix[i][j]<matrix[i+1][j+1]:
# 				print(matrix[i][j])
# y=(1,2,4,8,16)
# import numpy as np
# #二阶导数
# def hessian(x):
#     x_grad = np.gradient(x) 
#     hessian = np.empty((x.ndim, x.ndim) + x.shape, dtype=x.dtype) 
#     for k, grad_k in enumerate(x_grad):
#         # iterate over dimensions
#         # apply gradient again to every component of the first derivative.
#         tmp_grad = np.gradient(grad_k) 
#         for l, grad_kl in enumerate(tmp_grad):
#             hessian[k, l, :, :] = grad_kl
#     return hessian

# # x = np.random.randn(100, 100, 100)
# print(hessian(matrix))
# import numpy as np

# data = np.array([
# 	[2, 3, 4, 5],
# 	[4, 9, 16,25],
# 	])
# first_derivative = np.gradient(data)
# print(first_derivative)
# # second_derivative = ??? <--- there be kudos (:
# x= np.array([2, 3, 4, 5])
# y= np.array([4, 9, 16,25])
# ax = df.plot(x='X', y='y')
# df = df.assign(derivative=df.diff().eval('y/X'))
# df.plot(x='X', y='derivative', ax=ax)
# -*- coding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/5/18 21:09
@Author  : Dontla
@Email   : sxana@qq.com
@Software: PyCharm
"""
# from sympy import symbols, diff

# x, y = symbols('x y', real=True)

# print(diff(x ** 2 + y ** 3, y).subs({x: 3, y: 1}))  # 3

# from sympy import * #微分模块包

# x, y = symbols('x y', real=True)  #定义符号变量
# f = x ** 2 + y ** 3   #定义一个函数
# diff(f(x, y), x)#
# # print(diff(x ** 2 + y ** 3, y))  # 3*y**2
# print(diff(f, x).subs({x: 3, y: 1}))  # 3

# import matplotlib.pyplot as plt
# import numpy as np
# import math
# import sympy
 
# # if __name__ == '__main__':
# #     nderivativeplot()
# plt.figure(figsize=(5, 8))
# ax = plt.gca()  # 坐标轴的移动
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 绘图中文
# plt.rcParams['axes.unicode_minus'] = False  # 绘图负号
# x = np.linspace(-10,10, 200)
# y = np.power(x,3)+3*np.power(x,2)-24*x-20
# yd = 3*np.power(x,2)+6*x-24
# ydd=6*x+6
# label = '函数f(x)=x^3+3x^2-24x-20的曲线'
# plt.plot(x, y, label=label)
# label = "导数f'(x)=3x^2+6x-24的曲线"
# plt.plot(x, yd, label=label)
# label = "导数f''(x)=6x+6的曲线"
# plt.plot(x, ydd, label=label)


# # 设置图片的右边框和上边框为不显示
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')

# # 挪动x，y轴的位置，也就是图片下边框和左边框的位置
# # data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
# ax.spines['bottom'].set_position(('data', 0))
# # # axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置
# ax.spines['left'].set_position(('axes', 0.5))
# # ax.spines['left'].set_position(('data', 0))
# plt.title("函数、一阶导数、二阶导数")
# plt.legend(loc='upper right')
# plt.show()
import numpy as np
c=np.random.randint(0,20,(3,5))
# c=[ 7, 15 ,5, 9]
print(c)
d=np.gradient(c)
print(d)

# array([  7. ,  -6. ,  -4. ,   7.5,  -5.5,  -2. ,   4.5,   2.5,   2.5,
#         -1.5,  -2.5,  -5.5,   2. ,   0. , -11. ])
# >>> d=np.random.randint(0,20,(3,5))
# >>> np.gradient(d)
# [array([[  0. ,  14. ,  -3. ,   0. ,   1. ],
#        [ -7.5,   1. ,  -0.5,  -6. ,  -5.5],
#        [-15. , -12. ,   2. , -12. , -12. ]]), array([[-13. ,  -3. ,   6.5,   2.5,  -1. ],
#        [  1. ,  -4.5,  -0.5,   4.5,   0. ],
#        [  4. ,   4. ,  -0.5,  -2.5,   0. ]])]
