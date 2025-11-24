from heapq import heappush, heappop
from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0
    def __lt__(self, other):
        return self.bound < other.bound

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        result = u.profit
        j = u.level+1
        totweight = u.weight
        while j<=n and totweight+w[j]<=W:
            result+=p[j]
            totweight+=w[j]
            j+=1
        if j<=n:
            result+= (W-totweight) * p[j]/w[j]
        return result

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    count +=1
    while len(heap) != 0:
        # Complete the code here
        v=heappop(heap)[1]
        if v.bound>maxprofit:
            u = Node(v.level+1,v.weight+w[v.level+1],v.profit+p[v.level+1])
            u.bound = boundof(u,n,W,w,p)
            if u.weight<=W and u.profit>maxprofit:
                maxprofit=u.profit
            if u.bound>maxprofit:
                heappush(heap,(-u.bound,u))
            uu = Node(v.level+1,v.weight,v.profit)
            uu.bound=boundof(uu,n,W,w,p)
            if uu.bound>maxprofit:
                heappush(heap,(-uu.bound,uu))

    return maxprofit
