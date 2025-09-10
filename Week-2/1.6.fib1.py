# name: 노영호
# student id: 2024105451
def fib1(n: int) -> int:
    # Complete the code here
    if n<=1:
        return n
    return fib1(n-1)+fib1(n-2)