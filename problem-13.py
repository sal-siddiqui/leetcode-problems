# https://leetcode.com/problems/contains-duplicate-ii/

# Solution 1 - Brute Force
def main(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


# Solution 2 - Hashmap
# def main(nums, k):
#     hash_map = {}
#     for index, item in enumerate(nums):
#         if item in hash_map and abs(index - hash_map[item]) <= k:
#             return True
#         hash_map[item] = index
#     return False


# Solution 3 - Sliding Window
# def main(nums, k):
#     window = set()
#     for i, num in enumerate(nums):
#         if num in window:
#             return True
#         window.add(num)
#         if len(window) > k:
#             window.remove(nums[i - k])
#     return False


if __name__ == "__main__":
    args = [1, 2, 3, 1, 2, 3], 2
    print(main(*args))
