"""
Coin Change Problem
Find minimum number of coins needed to make a given amount.
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

def coin_change(coins, amount):
    """
    Find minimum number of coins to make amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
    
    Returns:
        Minimum number of coins or -1 if impossible
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    # Example usage
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    print(f"Minimum coins needed: {result}")  # 3 (5+5+1)
