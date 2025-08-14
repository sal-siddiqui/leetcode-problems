# https://leetcode.com/problems/missing-number/

# Solution 1 - Brute force
# Time Complexity: O(n^2) —
# Space Complexity: O(1) —
def main(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    return -1


# Solution 2 - Sum formula
# Time Complexity: O(n) — just one pass to sum.
# Space Complexity: O(1) — only a few variables.
# def main(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) / 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum


if __name__ == "__main__":
    args = [3, 0, 1]
    print(main(args))
