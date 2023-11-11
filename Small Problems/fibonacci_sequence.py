"""
    The Fibonacci squenece is a sequence of numbers such that any number, except for the first
    and second, is the sum of the previous two:
    
        0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    So to get the value in the 'n' position of the Fibonacci sequence we use the formula:

        fib(n) = fib(n - 1) + fib(n - 2)
"""

# Naïve recursive approach
def fibonacci_naive(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_naive(n - 2) + fibonacci_naive(n - 1)


# Basic Memoization approach
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}
def fibonacci_memoization(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]


# Automatic Memoization using decorators
from functools import lru_cache

@lru_cache(maxsize=None) # maxsize indicates how many of the most recent calls of the function should be cached
def fibonacci_automated_memo(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_automated_memo(n - 2) + fibonacci_automated_memo(n - 1)


# Iterative approach

def fibonacci_iterative(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1

    for _ in range(1, n): # This runs at most n - 1 times, faster than memoization
        last, next = next, last + next
    
    return next


# Generator 
from typing import Generator

def fibonacci_generator(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last +  next
        yield next

if __name__ == '__main__':
    print(fibonacci_naive(5))
    print(fibonacci_naive(10))
    
    print(fibonacci_memoization(50))
    print(fibonacci_memoization(100))
    
    print(fibonacci_memoization(50))
    print(fibonacci_memoization(100))
    
    print(fibonacci_iterative(50))
    print(fibonacci_iterative(100))
    
    for i in fibonacci_generator(50):
        print(i)

    print(fibonacci_generator(100))