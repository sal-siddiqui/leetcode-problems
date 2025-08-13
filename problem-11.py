# https://leetcode.com/problems/3sum/


def main(nums):
    triplets = []

    nums.sort()

    for index, item in enumerate(nums):
        # Early stop if the first number is positive
        if item > 0:
            break

        # Skip duplicate first numbers
        if index > 0 and item == nums[index - 1]:
            continue

        lp, rp = index + 1, len(nums) - 1

        while lp < rp:
            total = item + nums[lp] + nums[rp]

            if total > 0:
                rp -= 1
            elif total < 0:
                lp += 1
            else:
                triplets.append([item, nums[lp], nums[rp]])

                # Skip duplicates on the left
                while lp < rp and nums[lp] == nums[lp + 1]:
                    lp += 1
                # Skip duplicates on the right
                while lp < rp and nums[rp] == nums[rp - 1]:
                    rp -= 1

                # Move both pointers after recording a triplet
                lp += 1
                rp -= 1

    return triplets


if __name__ == "__main__":
    args = [-1, 0, 1, 2, -1, -4]
    print(main(args))
