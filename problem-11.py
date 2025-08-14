# https://leetcode.com/problems/3sum/

# Solution 1: Brute Force with Set
# Idea: Check all triplets using three nested loops, add to a set to avoid duplicates.
# Time Complexity: O(n^3) — Three nested loops over nums
# Space Complexity: O(k) — For storing unique triplets in a set (k = number of results)
# def main(nums):
#     result = set()
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
#     return [list(item) for item in result]

# Solution 2: Two Pointers after Sorting
# Idea: Sort the array, fix one number, then use two pointers to find pairs that sum to -fixed number, skipping duplicates.
# Time Complexity: O(n^2) — Sorting O(n log n) + two-pointer search for each element
# Space Complexity: O(1) — Ignoring output list
def main(nums):
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        lp, rp = i + 1, len(nums) - 1

        while lp < rp:
            total = num + nums[lp] + nums[rp]

            if total > 0:
                rp -= 1
            elif total < 0:
                lp += 1
            else:
                result.append([num, nums[lp], nums[rp]])
                lp += 1
                rp -= 1

                while nums[lp] == nums[lp - 1] and lp < rp:
                    lp += 1
                while nums[rp] == nums[rp + 1] and lp < rp:
                    rp -= 1

    return result


if __name__ == "__main__":
    args = [-1, 0, 1, 2, -1, -4]
    print(main(args))
