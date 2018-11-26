class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        #一开始没看懂题目，参考别人代码
        return sum(list(a) != sorted(a) for a in zip(*A))
