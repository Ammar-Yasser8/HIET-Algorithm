"""
Binary Search Algorithm
Search for a target value in a sorted array.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
    
    Returns:
        Index of target or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    # Example usage
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Index: {result}")  # 3
