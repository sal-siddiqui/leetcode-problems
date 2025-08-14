# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Solution 1 - Brute Force
# Time Complexity: O(n^2) — compare each element with all others
# Space Complexity: O(n) — store the result array
# def main(nums):
#     result = []
#     for i in range(len(nums)):
#         count = 0
#         for j in range(len(nums)):
#             if j != i and nums[j] < nums[i]:
#                 count += 1
#         result.append(count)
#     return result

# Solution 2 - Sorting with Counting
# Time Complexity: O(n log n) — sort the array
# Space Complexity: O(n) — store indices and results
def main(nums):
    sorted_nums = sorted(nums)
    mapping = {}

    for i, num in enumerate(sorted_nums):
        if num not in mapping:
            mapping[num] = i

    return [mapping[item] for item in nums]


if __name__ == "__main__":
    args = [6, 5, 4, 8]
    print(main(args))
