# https://leetcode.com/problems/spiral-matrix/

# Solution 1 - Using matrix rotation
# Time Complexity: O(m * n) — each element is visited exactly once
# Space Complexity: O(m * n) — because zip creates a new rotated matrix at each step
def main(matrix):
    def rotate():
        return list(zip(*matrix))[::-1]

    result = []
    while matrix:
        result.extend(matrix.pop(0))
        matrix = rotate()
    return result


if __name__ == "__main__":
    args = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(main(args))
