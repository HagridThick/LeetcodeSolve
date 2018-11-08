class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up = moves.count('U')        
        down = moves.count('D')
        left = moves.count('L')
        right = moves.count('R')
        if up == down and left == right:
            return True
        else:
            return False