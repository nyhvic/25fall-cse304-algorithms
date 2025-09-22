from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here
    while (i<h and j<m):
        if(U[i]<V[j]):
            S[k]=U[i]
            i+=1
        else:
            S[k]=V[j]
            j+=1
        k+=1
    if i>=h:
        while j<m:
            S[k]=V[j]
            j+=1
            k+=1
    else:
        while i<h:
            S[k]=U[i]
            i+=1
            k+=1

    

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    if n > 1:
        # Complete the code here
        U=S[0:h]
        V=S[h:n] # m=짝수 n-h = h    홀수 m=n-h = h + 1
        mergesort(h,U)
        mergesort(m,V)  
        merge(h,m,U,V,S)