class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ret=0
        for i in range(2**n):
            subset = []
            for j in range(n):
                if i>>j & 1:
                    subset.append(nums[j])
            pl=0
            for elem in subset:
                pl^=elem
            ret+=pl
        return ret