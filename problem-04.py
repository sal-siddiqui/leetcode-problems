# https://leetcode.com/problems/two-sum/

# Solution 1 - Brute Force
# Time Complexity: O(n^2) — check all pairs
# Space Complexity: O(1) — no extra data structures
def main(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


# Solution 2 - Hash Map Looking
# Time Complexity: O(n) — single pass through the array
# Space Complexity: O(n) — store seen numbers in a dictionary
# def main(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
#     return None


if __name__ == "__main__":
    args = [3, 2, 4], 6
    print(main(*args))
