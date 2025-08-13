# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


def main(lst):
    set_ = set(lst)
    res = []
    for i in range(1, len(lst) + 1):
        if i not in set_:
            res.append(i)
    return res


if __name__ == "__main__":
    args = [1, 1]
    print(main(args))
