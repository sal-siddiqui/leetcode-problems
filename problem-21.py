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


# Solution 2: Prefix Sum Precomputation
# Idea: Precompute prefix sums so that range sum can be calculated in O(1): sumRange(l, r) = prefix[r+1] - prefix[l]
# Time Complexity: O(n) for init, O(1) per query
# Space Complexity: O(n) — store prefix sum array
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
