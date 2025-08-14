# https://leetcode.com/problems/squares-of-a-sorted-array/

# Solution 1 - Square and sort
# Time Complexity: O(n log n) — sorting dominates
# Space Complexity: O(n) — new array for squared values
# def main(nums):
#     return sorted(num**2 for num in nums)


# Solution 2 - Two-pointer approach
# Time Complexity: O(n) — one pass through the array
# Space Complexity: O(n) — new array for squared values
def main(nums):
    import collections

    n = len(nums)
    lp, rp = 0, n - 1
    result = collections.deque()

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
