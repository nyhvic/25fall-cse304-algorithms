from typing import List

class Heap:
    def __init__(self, n: int, S: List[int]) -> None:
        # Complete the code here
        self.n = n
        self.S = S

def siftdown(H: Heap, i: int) -> None:
    # Complete the code here
    parent = i
    siftkey = H.S[i]
    while 2*parent <= H.n:
        if 2*parent < H.n and H.S[2*parent] < H.S[2*parent + 1]:
            largerchild = 2*parent+1
        else:
            largerchild = 2*parent
        if siftkey < H.S[largerchild]:
            H.S[parent] = H.S[largerchild]
            parent = largerchild
        else:
            break
    H.S[parent] = siftkey


def root(H: Heap) -> int:
    # Complete the code here
    keyout = H.S[1]
    H.S[1] = H.S[H.n]
    H.n -= 1
    siftdown(H,1)
    return keyout

def removekeys(n: int, H: Heap, S: List[int]) -> None:
    # Complete the code here
    i = n
    while i >=1:
        S[i] = root(H)
        i-=1

def makeheap(n: int, H: Heap) -> None:
    # Complete the code here
    i = n//2 
    while i>=1:
        siftdown(H,i)
        i-=1

def heapsort(n: int, H: Heap, S: List[int]) -> None:
    # Complete the code here
    makeheap(n,H)
    removekeys(n,H,S)
