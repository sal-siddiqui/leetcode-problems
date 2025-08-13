# https://leetcode.com/problems/squares-of-a-sorted-array/


# def main(nums):
#     return sorted(num**2 for num in nums)

from collections import deque


def main(nums):
    lp, rp = 0, len(nums) - 1
    result = deque()

    while lp <= rp:
        left_val, right_val = abs(nums[lp]), abs(nums[rp])

        if left_val > right_val:
            result.appendleft(left_val**2)
            lp += 1
        else:
            result.appendleft(right_val**2)
            rp -= 1

    return list(result)


if __name__ == "__main__":
    args = [-7, -3, 2, 3, 11]
    print(main(args))
