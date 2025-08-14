# https://leetcode.com/problems/counting-bits/


# Solution 1: Direct Count with bin()
# Idea: For each number from 0 to n, convert to binary and count '1's.
# Time Complexity: O(n log n) — log n to convert and count bits per number
# Space Complexity: O(1) extra — output list only
def main(n):
    result = [0] * (n + 1)
    for i in range(n + 1):
        result[i] = bin(i).count("1")
    return result


if __name__ == "__main__":
    args = 5
    print(main(args))
