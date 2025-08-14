# https://leetcode.com/problems/contains-duplicate-ii/

# Solution 1: Brute Force Check
# Idea: Compare every pair of indices (i, j) and check if values match and distance <= k.
# Time Complexity: O(n^2) — nested loop comparison
# Space Complexity: O(1) — no extra storage
def main(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
                return True
    return False


# Solution 2: Hashmap for Last Seen Index
# Idea: Store the last seen index of each number in a dictionary. When a duplicate is found, check if the index difference <= k.
# Time Complexity: O(n) — each lookup and update is O(1)
# Space Complexity: O(n) — dictionary stores last index for each unique number
# def main(nums, k):
#     last_seen = {}
#     for i, num in enumerate(nums):
#         if num in last_seen and i - last_seen[num] <= k:
#             return True
#         last_seen[num] = i
#     return False


# Solution 2: Sliding Window with Set
# Idea: Use a set to store up to k previous numbers; if a duplicate is found, return True.
# Remove numbers that slide out of the k-window.
# Time Complexity: O(n) — each element added/removed at most once
# Space Complexity: O(min(n, k)) — set stores at most k elements
# def main(nums, k):
#     seen = set()
#     for i, num in enumerate(nums):
#         if num in seen:
#             return True
#         seen.add(num)
#         if len(seen) > k:
#             seen.remove(nums[i - k])
#     return False


if __name__ == "__main__":
    args = [1, 2, 3, 1, 2, 3], 2
    print(main(*args))
