class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        n = len(nums)
        if n==1:
            return [[nums[0]]]
        if n==2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        for i in range(n):
            pl = self.permute(nums[:i]+nums[i+1:])
            for j in range(len(pl)):
                pl[j].append(nums[i])
            ret.extend(pl)
        return ret 