class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)