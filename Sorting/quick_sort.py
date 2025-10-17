"""
Quick Sort Algorithm
Divide and conquer sorting algorithm using partitioning.
Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n)
"""

def quick_sort(arr):
    """
    Sort array using Quick Sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
