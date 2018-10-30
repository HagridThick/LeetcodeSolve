class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str 宝石类型
        :type S: str 拥有的石头
        :rtype: int  返回有多少石头是宝石,字母区分大小写
        """

        number = 0
        for i in J:
            number+=S.count(i)
        return number

J = "aA"
S = "aAAbbbb"
solu = Solution()
print(solu.numJewelsInStones(J,S))