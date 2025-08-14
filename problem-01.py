# https://leetcode.com/problems/contains-duplicate/

# Solution 1 - Use a set
# Time Complexity: O(n) — each lookup/add in a set is O(1) on average.
# Space Complexity: O(n) — worst case we store all elements.
def main(nums):
    return len(set(nums)) != len(nums)


# Solution 2 - Sort first (no extra memory except for sorting)
# Time Complexity: O(n log n) — due to sorting.
# Space Complexity: O(1)
# def main(nums):
#     nums.sort()
#     n = len(nums)

#     for i in range(n - 1):
#         if nums[i] == nums[i + 1]:
#             return True
#     return False


if __name__ == "__main__":
    args = [1, 2, 3, 4]
    print(main(args))
