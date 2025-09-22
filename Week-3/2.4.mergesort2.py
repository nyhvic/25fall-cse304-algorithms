from typing import List

def merge2(low: int, mid: int, high: int, S: List[int]) -> None:
    U = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    # Complete the code here
    while (i<=mid and j<=high):
        if S[i]<S[j]:
            U[k]=S[i]
            i+=1
        else:
            U[k]=S[j]
            j+=1
        k+=1
    if(i>mid):
        while j<=high:
            U[k]=S[j]
            j+=1
            k+=1
    else:
        while i<=mid:
            U[k]=S[i]
            i+=1
            k+=1
    i,j,k=low,mid+1,0
    while i<=mid:
        S[i]=U[k]
        i+=1
        k+=1
    while j<=high:
        S[j]=U[k]
        j+=1
        k+=1


def mergesort2(low: int, high: int, S: List[int]) -> None:
    if low < high:
        mid = (low + high) // 2
        mergesort2(low, mid, S)
        mergesort2(mid + 1, high, S)
        merge2(low, mid, high, S)