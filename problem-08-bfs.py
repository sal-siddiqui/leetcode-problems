# https://leetcode.com/problems/number-of-islands/

##  BFS Template
# from collections import deque

# def bfs(<starting-node>):
#     queue = deque([<starting-node>])
#     visited.add(<starting-node>)

#     def neighbors(node):
#         # return list of neighbors

#     def is_valid(neighbor):
#         # return True if neighbor is a valid neighbor in context of problem

#     while queue:
#         node = queue.popleft()
#         # process node if needed

#         for neighbor in neighbors(node):
#             if neighbor not in visited and is_valid(neighbor):
#                 visited.add(neighbor)
#                 queue.append(neighbor)


from collections import deque


def main(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def neighbors(r, c):
        return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    def is_valid(neighbor):
        row, col = neighbor

        if row < 0 or row >= rows:
            return False
        if col < 0 or col >= cols:
            return False
        if grid[row][col] != "1":  # noqa: SIM103
            return False

        return True

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()

            for neighbor in neighbors(row, col):
                if neighbor not in visited and is_valid(neighbor):
                    visited.add(neighbor)
                    queue.append(neighbor)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


if __name__ == "__main__":
    args = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(main(args))
