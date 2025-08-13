# https://leetcode.com/problems/two-sum/


# def main(lst, target):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] + lst[j] == target:
#                 return [i, j]
#     return [-1, -1]


def main(lst, target):
    hashmap = {}
    for index, item in enumerate(lst):
        difference = target - item
        if difference in hashmap:
            return hashmap[difference], index
        hashmap[item] = index
    return None


if __name__ == "__main__":
    args = [3, 2, 4], 6
    print(main(*args))
