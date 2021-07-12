# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。


# 题解：利用二分查找寻找那个数，如果找到返回数的下标
# 如果没有找到，那么返回最后找到的下标
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if (nums[mid]== target):
                return mid
            if (nums[mid]>target):
                right = mid-1
            else:
                left = mid+1
        return left

nums = [1,3,5,6]
target = int(input('输入要查询的数字'))
solution = Solution() 
print(solution.searchInsert(nums,target)) 