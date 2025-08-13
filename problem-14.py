# https://leetcode.com/problems/minimum-absolute-difference/

# Solution 1 - Brute Force
def main(arr):
    arr.sort()
    min_diff = float("inf")
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[j] - arr[i]
            if diff > min_diff:
                break
            if diff < min_diff:
                min_diff = diff
                pairs = [[arr[i], arr[j]]]
            elif diff == min_diff:
                pairs.append([arr[i], arr[j]])

    return pairs


# Solution 2 - Sliding Window
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
