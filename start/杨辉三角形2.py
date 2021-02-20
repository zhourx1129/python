# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 21:30
# @Author  : Zhou Ruxin
# @Email   : z534418624@gmail.com
# @File    : 杨辉三角形2.py
# @Software: PyCharm
a = [[0 for x in range(2*10-1)] for y in range(2*10-1)] #生成一个二维数组
# a = [0 for x in range(2*10-1)]  生成一个一维数组
for i in range(10):
    for j in range(i+1):
        if j==i or j==0:
            a[i][j]=1
        else:
            a[i][j]=a[i-1][j-1]+a[i-1][j] 

for i in range(10):
    print('  '*(10 - i-1), end='')
    for j in range(i+1):

        print('%2d'%a[i][j],end='  ')
    print()
