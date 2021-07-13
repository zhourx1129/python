# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。


class Solution:
    def sortedSquares(self, nums):
        newArr = []
        height = len(nums)
        for i in range(height):
            newArr.append(nums[i]**2)
        newArr.sort()
        return newArr
        

nums = [-5,-3,-2,-1]
solution = Solution()
print(solution.sortedSquares(nums))
