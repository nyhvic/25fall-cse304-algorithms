from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low
    # Complete the code here
    for i in range(low+1,high+1):
        if S[i]<pivotitem:
            j+=1
            S[i],S[j] = S[j],S[i]
    pivotpoint = j
    S[low],S[pivotpoint] = S[pivotpoint],S[low]
    return pivotpoint

def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        # Complete the code here
        pivotpoint = partition(low,high,S)
        quicksort(low,pivotpoint,S)
        quicksort(pivotpoint+1,high,S)