# https://leetcode.com/problems/minimum-size-subarray-sum/

# Solution 1: Brute Force Prefix Sum
# Idea: For each starting index, try extending the subarray until the sum >= target, track the minimal length found.
# Time Complexity: O(n^2) — nested loops for subarray sums
# Space Complexity: O(1) — only variables for sum and min length
def main(nums, target):
    n = len(nums)
    min_len = float("inf")
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum >= target:
                min_len = min(min_len, j - i + 1)
                break
    return 0 if min_len == float("inf") else min_len


# Solution 2: Sliding Window (Two Pointers)
# Idea: Expand right pointer to increase sum, move left pointer to shrink window while keeping sum >= target. Track smallest valid window length.
# Time Complexity: O(n) — each element visited at most twice
# Space Complexity: O(1) — constant extra space
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
