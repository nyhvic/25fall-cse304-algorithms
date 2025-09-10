from typing import List

def arrsum(n: int, S: List[int]) -> int:
    # Complete the code here
    ret=0
    for i in range(n):
        ret+=S[i]
    return ret

