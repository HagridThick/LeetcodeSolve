class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = s.split(' ')
        s3 = ""
        for i in s2:
            s3 = s3 + i[::-1] +" "
        return s3[:-1]

print(Solution().reverseWords("Let's take LeetCode contest"))