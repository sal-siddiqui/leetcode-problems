# https://leetcode.com/problems/range-sum-query-immutable/

# Solution 1 - Brute Force sum on each query
# Idea: Just store the array and compute sum by looping through elements for each query.
# Time Complexity: O(n) per query
# Space Complexity: O(1) extra
# class NumArray:
#     def __init__(self, nums):
#         self.nums = nums

#     def sum_range(self, left, right):
#         return sum(self.nums[left : right + 1])


# Solution 2 - Prefix Sum for O(1) queries
# Idea: Precompute prefix sums so we can get range sum in constant time.
# Time Complexity: O(n) preprocessing, O(1) per query
# Space Complexity: O(n) extra
class NumArray:
    def __init__(self, nums):
        self._prefix = [0]
        for num in nums:
            self._prefix.append(self._prefix[-1] + num)

    def sum_range(self, left, right):
        return self._prefix[right + 1] - self._prefix[left]
