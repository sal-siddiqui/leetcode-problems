# https://leetcode.com/problems/minimum-absolute-difference/

# Solution 1: Brute Force Pair Comparison
# Idea: Compare all possible pairs (i, j), track the minimum absolute difference,
#       and collect all pairs with that difference.
# Time Complexity: O(n^2) — check every pair
# Space Complexity: O(n) — store pairs in result list
def main(arr):
    n = len(arr)
    min_diff = float("inf")
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff
                result = [[min(arr[i], arr[j]), max(arr[i], arr[j])]]
            elif diff == min_diff:
                result.append([min(arr[i], arr[j]), max(arr[i], arr[j])])
    return sorted(result)


# Solution 2 - Sliding Window
# Idea: Sorting arr ensures the minimum difference is between consecutive elements. Check adjacent pairs, track the smallest difference, and collect results.
# Time Complexity: O(n log n) — sorting dominates
# Space Complexity: O(1) extra — aside from result list
# def main(arr):
#     arr.sort()
#     min_diff = float("inf")
#     pairs = []

#     # Find minimum difference
#     for i in range(1, len(arr)):
#         diff = arr[i] - arr[i - 1]
#         min_diff = min(min_diff, diff)

#     # Collect pairs with min_diff
#     for i in range(1, len(arr)):
#         if arr[i] - arr[i - 1] == min_diff:
#             pairs.append([arr[i - 1], arr[i]])

#     return pairs


if __name__ == "__main__":
    args = [3, 8, -10, 23, 19, -4, -14, 27]
    print(main(args))
