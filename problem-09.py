# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def main(lst):
    left, right = 0, 1
    max_profit = 0

    while right != len(lst):
        if lst[left] < lst[right]:
            profit = lst[right] - lst[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit


if __name__ == "__main__":
    args = [7, 1, 5, 3, 6, 0, 4]
    print(main(args))
