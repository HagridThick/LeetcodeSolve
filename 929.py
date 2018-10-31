class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unrepeat = set()
        for email in emails:
            spl = email.split('@')
            pre = spl[0].split('+')
            unrepeat.add(pre[0].replace('.','') + spl[1])
        return len(unrepeat)