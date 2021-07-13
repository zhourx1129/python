# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

from hashlib import new


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        

nums = [1,2,3,4,5,6,7]
k = int(input('请输入k\n'))
solution=Solution()
solution.rotate(nums,k)
print(nums)