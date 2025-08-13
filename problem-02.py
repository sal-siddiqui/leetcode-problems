# https://leetcode.com/problems/missing-number/


# def main(lst):
#     for i in range(len(lst)):
#         if i not in lst:
#             return i
#     return -1


def main(lst):
    return sum(range(len(lst) + 1)) - sum(lst)


if __name__ == "__main__":
    args = [3, 0, 1]
    print(main(args))
