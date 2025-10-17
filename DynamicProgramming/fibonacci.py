"""
Fibonacci Sequence using Dynamic Programming
Calculate nth Fibonacci number efficiently.
Time Complexity: O(n)
Space Complexity: O(n) for memoization, O(1) for iterative
"""

def fibonacci_memoization(n, memo=None):
    """
    Calculate nth Fibonacci number using memoization.
    
    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary for memoization
    
    Returns:
        nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """
    Calculate nth Fibonacci number using iteration.
    
    Args:
        n: Position in Fibonacci sequence
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


if __name__ == "__main__":
    # Example usage
    n = 10
    print(f"Fibonacci({n}) using memoization: {fibonacci_memoization(n)}")
    print(f"Fibonacci({n}) using iteration: {fibonacci_iterative(n)}")
