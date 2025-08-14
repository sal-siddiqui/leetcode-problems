class NumArray:
    def __init__(self, nums):
        self.nums = nums

        self._prefix_sums = [0]
        for num in self.nums:
            self._prefix_sums.append(self._prefix_sums[-1] + num)

    def sum_range(self, left, right):
        return self._prefix_sums[right + 1] - self._prefix_sums[left]


if __name__ == "__main__":
    temp = NumArray([-2, 0, 3, -5, 2, -1])
    print(temp)
