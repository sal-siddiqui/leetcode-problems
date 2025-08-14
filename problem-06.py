# https://leetcode.com/problems/minimum-time-visiting-all-points/

# Solution 1 - Iterative traversal using max difference
# Time complexity: O(n) — we iterate over all points once
# Space complexity: O(1) — we only use a few variables, no extra data structures
def main(points):
    total_time = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        # You can move diagonally in one second, so the time is max of x and y distance
        total_time += max(abs(y2 - y1), abs(x2 - x1))
    return total_time


if __name__ == "__main__":
    args = [[1, 1], [3, 4], [-1, 0]]
    print(main(args))
