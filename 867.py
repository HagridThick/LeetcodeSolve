class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #print(*A)
        #print(zip(*A))
        return list(zip(*A))

print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
