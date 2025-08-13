# https://leetcode.com/problems/spiral-matrix/


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
