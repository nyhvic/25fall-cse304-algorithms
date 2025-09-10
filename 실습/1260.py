class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m,n = len(grid),len(grid[0])
        ret = [[0]* n for _ in range(m)]
        k %= m*n
        for i in range(m):
            for j in range(n):
                if j+k<n:
                    ret[i][j+k] = grid[i][j]
                else:
                    carry = (j+k) // n
                    mean = (j+k)%n
                    if i+carry < m:
                        ret[i+carry][mean] = grid[i][j]
                    else:
                        ret[i+carry-m][mean] = grid[i][j]

        return ret
