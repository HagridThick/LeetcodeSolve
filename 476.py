class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Complement = bin(num)[2::]
        #newnum = [ not x for x in Complement]
        
        return ((num ^ 2 ** (len(bin(num))-2) - 1))
        #    num 与 2 异或 
        #    101 与 010 --  111(7)
        #    7 **  5-2   - 1
    
Solution().findComplement(5)
