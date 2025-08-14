# Solution 2: Expand Around Peaks
# Idea: Iterate through array, treat each element as a potential peak, expand left and right to find mountain length.
# Time Complexity: O(n) — Each element visited at most twice
# Space Complexity: O(1) — Only storing counters
def main(nums):
    n = len(nums)
    max_len = 0
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            lp = i - 1
            rp = i + 1

            while lp > 0 and nums[lp - 1] < nums[lp]:
                lp -= 1

            while rp < n - 1 and nums[rp + 1] < nums[rp]:
                rp += 1

            max_len = max(max_len, rp - lp + 1)

    return max_len


if __name__ == "__main__":
    args = [-1, 0, 1]
    print(main(args))
