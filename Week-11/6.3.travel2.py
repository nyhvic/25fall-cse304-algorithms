from heapq import heappush, heappop
from typing import List, Tuple
import time

INF = float("inf")

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path: List[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(path)

def pathlength(path: List[int], W: List[List[float]]) -> float:
    # Complete the code here
    i,j = 0,1
    length = 0
    while j<len(path):
        length+=W[path[i]][path[j]]
        i+=1
        j+=1

    return length

def hasOutgoing(v: int, path: List[int]) -> bool:
    return v in path[:len(path)-1]

def hasIncoming(v: int, path: List[int]) -> bool:
    return v in path[1:]

def boundof(v: Node, n: int, W: List[List[float]]) -> float:
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        # Complete the code here
        if hasOutgoing(i,v.path):
            continue
        minimum = INF
        for j in range(1,n+1):
            if i==j:
                continue
            if j==1 and i==v.path[v.level]:
                continue
            if hasIncoming(j,v.path):
                continue
            minimum = min(minimum,W[i][j])
        lower+=minimum

    return lower

def travel2(n: int, W: List[List[float]]) -> Tuple[float, List[int]]:
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, time.time(), v))
    while len(heap) != 0:
        v = heappop(heap)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                # Complete the code here
                if i in v.path:
                    continue  
                u=Node(v.level+1,v.path+[i])
                if u.level == n-2:
                    u.path.append(remainder(u.path,n))
                    u.path.append(1)
                    if pathlength(u.path,W)<minlength:
                        minlength = pathlength(u.path,W)
                        opttour = u.path
                else:
                    u.bound = boundof(u,n,W)
                    if u.bound<minlength:
                        heappush(heap,(u.bound,time.time(),u))

    return minlength, opttour
