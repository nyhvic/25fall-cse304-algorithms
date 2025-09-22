class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]
        for s in strs:
            pp=""
            length = len(s) if len(prefix)>len(s) else len(prefix)
            for j in range(length):
                if s[j]==prefix[j]:
                    pp+=s[j]
                else:
                    break
            prefix=pp
        return prefix

                