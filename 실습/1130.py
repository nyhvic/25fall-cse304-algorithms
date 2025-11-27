class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.DP=[[-1 for _ in range(len(arr))] for _ in range(len(arr))]


        