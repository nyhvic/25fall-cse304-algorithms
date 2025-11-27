from heapq import heappush,heappop

class Node():
    def __init__(self,path,visited,last,m):
        self.path=path
        self.visited=visited
        self.last=last  
        self.m=m
        

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        lenmin=n**2
        v=Node([],set({}),-1,0)
        queue = []
        heappush(queue,(-len(v.path),id(v),v))
        while len(queue)!=0:
            v=heappop(queue)[2]
            if len(v.visited)==n and len(v.path)<lenmin:
                lenmin = len(v.path)
                continue
            elif len(v.path)>lenmin:
                continue
            for i in range(n):
                if v.last!=i and (v.last==-1 or v.last in graph[i]):
                    s=v.visited.copy()
                    s.add(i)
                    m = 1 if i in v.path else 0
                    u=Node(v.path+[i],s,i,v.m+m)
                    heappush(queue,(-len(u.path),id(u),u))
        return lenmin-1
    



s= Solution()
print(s.shortestPathLength([[1,5],[0,3],[3,5],[1,2,5],[7],[0,7,6,2,3],[5],[5,4,8],[7]]))