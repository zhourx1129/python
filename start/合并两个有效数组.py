# -*- coding: UTF-8 -*-
'''
@File    ：合并两个有效数组.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/7/17 13:06 
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            nums1[m] = i
            m+=1
        nums1.sort()
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
result = solution.merge(nums1,m,nums2,n)
print(result)