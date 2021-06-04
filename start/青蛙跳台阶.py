# -*- coding: UTF-8 -*-
'''
@Project ：国家化妆品的selenium爬取.py 
@File    ：青蛙跳台阶.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/6/4 12:53 
'''
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 1 2 3 5 8
#题解:  f(n) = f(n-1)+f(n-2)
class Solution:
    def jumpFloor(self, number):
        ls = [1,2]
        if number <= 2:
            return ls[number-1]
        for i in range(2,number):
            ls.append(ls[i-1]+ls[i-2])
        return ls[number-1]

number = int(input('请输入台阶数'))
jumpfloor = Solution()
print(jumpfloor.jumpFloor(number))
