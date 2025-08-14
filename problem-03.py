# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Solution 1 - Brute force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def main(nums):
    result = []
    for num in range(1, len(nums) + 1):
        if num not in nums:
            result.append(num)
    return result


# Solution 1 - Use a set
# Time Complexity: O(n)
# Space Complexity: O(n)
# def main(nums):
#     nums_set = set(nums)
#     result = []
#     for num in range(1, len(nums) + 1):
#         if num not in nums_set:
#             result.append(num)
#     return result


if __name__ == "__main__":
    args = [4, 3, 2, 7, 8, 2, 3, 1]
    print(main(args))
