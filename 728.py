class Solution:
    def divide(self,num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        L1 = list(range(left,right+1))
        L2 = [x for x in L1 if self.divide(x)]
        return L2