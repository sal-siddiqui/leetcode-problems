# https://leetcode.com/problems/single-number/


# Solution 1 - Brute Force
# def main(nums):
#     from collections import Counter

#     counter = Counter(nums)

#     for key, value in counter.items():
#         if value == 1:
#             return key
#     return -1


# Solution 2 - Bit Manipulation
# XOR of two identical numbers is 0.
# XOR with 0 gives the number itself.
# XOR is commutative
def main(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    args = [4, 1, 2, 1, 2]
    print(main(args))
