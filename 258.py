class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        m = num % 9
        if m:
            return m
        else:
            return 9