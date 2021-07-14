# -*- coding: UTF-8 -*-
'''
@File    ：两数之和 II - 输入有序数组.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/7/14 15:52 
'''
# 给定一个已按照 升序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while (left < right):
            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            elif (numbers[left] + numbers[right] > target):
                right -= 1
            else:
                left += 1

numbers = [0,0,3,4]
target = int(input('请输入target'))
solution =  Solution()
print(solution.twoSum(numbers,target))