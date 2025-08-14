# https://leetcode.com/problems/single-number/


# Solution 1: Brute Force Using Count
# Idea: For each number, count how many times it appears; return the one with count == 1.
# Time Complexity: O(n^2) — counting for each element
# Space Complexity: O(1) — no extra data structures
def main(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num


# Solution 2: Bitwise XOR
# Idea: XOR of two identical numbers is 0, and XOR with 0 is the number itself. XOR-ing all elements cancels duplicates, leaving the unique number.
# Time Complexity: O(n) — single pass through array
# Space Complexity: O(1) — only one variable to store result
# def main(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result


if __name__ == "__main__":
    args = [4, 1, 2, 1, 2]
    print(main(args))
