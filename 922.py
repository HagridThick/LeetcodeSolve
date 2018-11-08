class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [x for x in A if x%2 != 0]
        even = [x for x in A if x%2 == 0]
        rarray = []
        is_odd = False
        
        while(odd or even):
            if is_odd:
                rarray.append(odd.pop())
            else:
                rarray.append(even.pop())
            is_odd = not is_odd
        return rarray
