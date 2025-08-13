# https://leetcode.com/problems/counting-bits/


# Solution 1 - ...
def main(n):
    result = [0] * (n + 1)

    for index, item in enumerate(range(n + 1)):
        result[index] = bin(item).count("1")

    return result


if __name__ == "__main__":
    args = 5
    print(main(args))
