"""
Linear Search Algorithm
Search for a target value by checking each element sequentially.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Search for target in array using linear search.
    
    Args:
        arr: List of comparable elements
        target: Element to search for
    
    Returns:
        Index of target or -1 if not found
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


if __name__ == "__main__":
    # Example usage
    arr = [5, 2, 9, 1, 7, 6, 3]
    target = 7
    result = linear_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Index: {result}")  # 4
