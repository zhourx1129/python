class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([st[::-1] for st in s.split(" ")])


solution = Solution()
s = "Let's take LeetCode contest"
s= solution.reverseWords(s)
print(s)