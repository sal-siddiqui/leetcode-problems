# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution 1 - Single pass tracking minimum price
# Time Complexity: O(n) — iterate through the array once
# Space Complexity: O(1) — only a few variables used
def max_profit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# Solution 2 - Using two pointers
# Time Complexity: O(n) — each element visited once
# Space Complexity: O(1) — just two pointers
def main(prices):
    left, right = 0, 1  # buy, sell
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit


if __name__ == "__main__":
    args = [7, 1, 5, 3, 6, 0, 4]
    print(main(args))
