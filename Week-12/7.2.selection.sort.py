from typing import List

def selectionsort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(n-1):
        smaleast = i
        for j in range(i+1,n):
            if S[smaleast]>S[j]:
                smaleast=j
        S[i],S[smaleast]=S[smaleast],S[i]
