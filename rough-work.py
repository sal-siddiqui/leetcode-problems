def main(nums):
    n = len(nums)
    max_total = float("-inf")

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            max_total = max(max_total, total)
    return max_total


if __name__ == "__main__":
    args = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(main(args))
