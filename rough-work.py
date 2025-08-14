def main(nums):
    mapping = {}
    sorted_nums = sorted(nums)

    for i, num in enumerate(sorted_nums):
        if num not in mapping:
            mapping[num] = i

    return [mapping[num] for num in nums]


if __name__ == "__main__":
    args = [6, 5, 4, 8]
    print(main(args))
