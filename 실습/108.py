class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid = (len(nums)-1)//2
        t=TreeNode(nums[mid])
        t.left=self.sortedArrayToBST(nums[:mid])
        t.right=self.sortedArrayToBST(nums[mid+1:])
        return t