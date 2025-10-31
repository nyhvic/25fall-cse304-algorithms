class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ind = 0
        last = len(nums)-1
        
        if ind == last :
            return True
        while ind<last:
            if nums[ind]==0:
                return False
            if nums[ind]+ind>=last:
                return True
            partition = nums[ind+1:ind+nums[ind]+1]
            pl = partition[0]
            mx = 1
            for i in range(1,len(partition)):
                if pl>=1:
                    pl-=1
                if pl<partition[i]:
                    pl = partition[i]
                    mx = i+1
            if mx == 0:
                return False
            ind+=mx

        return ind >= last