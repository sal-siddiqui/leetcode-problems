# https://leetcode.com/problems/minimum-size-subarray-sum/

# Solution 1 - Brute Force
def main(nums, target):
    n = len(nums)
    min_len = float("inf")

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total >= target:
                min_len = min(min_len, j - i + 1)
                break

    return 0 if min_len == float("inf") else min_len


# Solution 2 - Sliding Window
# def main(nums, target):
#     n = len(nums)
#     lp = 0
#     total = 0
#     min_len = float("inf")

#     for rp in range(n):
#         total += nums[rp]
#         while total >= target:
#             min_len = min(min_len, rp - lp + 1)
#             total -= nums[lp]
#             lp += 1

#     return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    args = [2, 3, 1, 2, 4, 3], 7
    print(main(*args))
