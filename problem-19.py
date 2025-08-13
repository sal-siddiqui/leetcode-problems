# https://leetcode.com/problems/maximum-subarray/


# Solution 1 - Brute Force
# def main(nums):
#     n = len(nums)
#     max_sum = float("-inf")

#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += nums[j]
#             max_sum = max(max_sum, current_sum)

#     return max_sum


# Solution 2 - ...
# def main(nums):
#     max_sum = nums[0]
#     current_sum = 0

#     for num in nums:
#         current_sum = max(0, current_sum)
#         current_sum += num
#         max_sum = max(max_sum, current_sum)


# Solution 3 - Dynamic Progrmaming
def main(nums):
    dp = [0] * len(nums)

    for idx, num in enumerate(nums):
        dp[idx] = max(num, dp[idx - 1] + num)


if __name__ == "__main__":
    args = ...
    print(main(*args))
