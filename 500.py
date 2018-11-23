class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """
        L1 = ['Q','W','E','R','T','Y','U','I','O','P']
        L2 = ['A','S','D','F','G','H','J','K','L']
        L3 = ['Z','X','C','V','B','N','M']
        L1 = L1 + [i.lower() for i in L1]
        L2 = L2 + [i.lower() for i in L2]
        L3 = L3 + [i.lower() for i in L3]
        """
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        out = []

        for i in words:
            for line in keyboard:
                lword = i.lower()
                if set(lword).issubset(set(line)):
                    out.append(i)

        return out



