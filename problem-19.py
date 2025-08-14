# https://leetcode.com/problems/maximum-subarray/


# Solution 1: Brute Force Subarray Sum
# Idea: For each starting index, sum all subarrays starting there, track the maximum sum.
# Time Complexity: O(n^2) — two nested loops for subarrays
# Space Complexity: O(1) — only variables for sum and max
def main(nums):
    n = len(nums)
    max_sum = float("-inf")
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


# Solution 2: Kadane's Algorithm
# Idea: Iterate once, tracking the best sum ending at current index
#       and the best sum overall. If current sum drops below 0, reset to current element.
# Time Complexity: O(n) — single pass
# Space Complexity: O(1) — constant extra variables
# def main(nums):
#     curr_sum = max_sum = nums[0]
#     for num in nums[1:]:
#         curr_sum = max(num, curr_sum + num)
#         max_sum = max(max_sum, curr_sum)
#     return max_sum


if __name__ == "__main__":
    args = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(main(*args))
