class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i, n in enumerate(s[::-1]):
            #print(i,n)
            res += (ord(n)-ord('A')+1)*(26**i)
        return res
        

print(Solution().titleToNumber("abcd"))
