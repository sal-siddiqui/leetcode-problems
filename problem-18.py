# https://leetcode.com/problems/climbing-stairs/


# Solution 1 - Brute Force
def main(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n - 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    args = 2
    print(main(args))
