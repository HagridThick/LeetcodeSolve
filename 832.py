class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = 1 - A[i][j]
            A[i] = A[i][::-1]
        return A

so = Solution()
print(so.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))