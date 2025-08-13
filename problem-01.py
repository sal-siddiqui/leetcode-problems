# https://leetcode.com/problems/contains-duplicate/


def main(lst):
    return len(set(lst)) != len(lst)


if __name__ == "__main__":
    args = [1, 2, 3, 4]
    print(main(args))
