# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


# def main(lst):
#     result = []
#     for i in range(len(lst)):
#         count = 0
#         current_value = lst[i]
#         for j in range(len(lst)):
#             if lst[j] < current_value:
#                 count += 1
#         result.append(count)
#     return result


def main(lst):
    sorted_lst = sorted(lst)
    position_map = {}

    for index, item in enumerate(sorted_lst):
        if item not in position_map:
            position_map[item] = index

    return [position_map[item] for item in lst]


if __name__ == "__main__":
    args = [6, 5, 4, 8]
    print(main(args))
