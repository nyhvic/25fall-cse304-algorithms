from typing import List

# Global variable type declarations
n: int
W: float
w: List[float]
p: List[float]
maxprofit: float
bestset: List[bool]
include: List[bool]

def promising(i: int, weight: float, profit: float) -> bool:
    global n, W, w, p, maxprofit
    # Complete the code here
    if(weight >= W):
        return False

    bound = profit
    totweight = weight
    j=i+1
    while j<=n and totweight+w[j] <=W:
        totweight+=w[j]
        bound+=p[j]
        j+=1
    if j<=n:
        bound+=(W-totweight)*p[j]/w[j]

    return bound > maxprofit

def knapsack(i: int, weight: float, profit: float) -> None:
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        # Complete the code here
        maxprofit=profit
        bestset = include
    if promising(i, weight, profit):
        # Complete the code here
        include[i+1]=1
        knapsack(i+1,weight+w[i+1],profit+p[i+1])
        include[i+1]=0
        knapsack(i+1,weight,profit)