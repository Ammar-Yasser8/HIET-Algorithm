"""
Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray with the largest sum.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    """
    Find maximum sum of contiguous subarray.
    
    Args:
        nums: List of integers
    
    Returns:
        Maximum sum
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # Example usage
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(nums)
    print(f"Input: {nums}")
    print(f"Maximum subarray sum: {result}")  # 6
