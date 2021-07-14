# -*- coding: UTF-8 -*-
'''
@File    ：移动0.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/7/14 15:11 
'''
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        while (r < len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

nums = [0,1,0,3,12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)