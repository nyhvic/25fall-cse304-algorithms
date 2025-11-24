from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
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

def knapsack2(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    queue = [] # Initialize Queue
    v = Node(0, 0, 0)
    bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    count+=1
    while len(queue) != 0:
        # Complete the code here
        v = queue[0]
        queue.pop(0)
        u=Node(v.level+1,v.weight+w[v.level+1],v.profit+p[v.level+1])
        if u.weight<=W and u.profit>maxprofit:
            maxprofit = u.profit
        if boundof(u,n,W,w,p)>maxprofit:
            queue.append(u)
        uu=Node(v.level+1,v.weight,v.profit)
        if boundof(uu,n,W,w,p)>maxprofit:
            queue.append(uu)



    return maxprofit
