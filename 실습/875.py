class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        minimumk = int(sum(piles)/h)
        while True:
            hour = 0
            