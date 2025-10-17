"""
Merge Sort Algorithm
Divide and conquer sorting algorithm using merging.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge_sort(arr):
    """
    Sort array using Merge Sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")
