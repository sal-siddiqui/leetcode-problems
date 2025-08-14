# https://leetcode.com/problems/longest-mountain-in-array/


def main(arr):
    n = len(arr)
    max_len = 0

    for i in range(1, n - 1):
        # Check if arr[i] is a peak
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            left = i
            right = i

            # Expand left while strictly decreasing
            while left > 0 and arr[left] > arr[left - 1]:
                left -= 1

            # Expand right while strictly decreasing
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    args = [-1, 2]
    print(main(args))
