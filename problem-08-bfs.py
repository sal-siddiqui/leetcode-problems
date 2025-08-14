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


# Solution 1 - BFS with visited set
# Time Complexity: O(m * n) — each cell is visited at most once
# Space Complexity: O(m * n) — for the visited set and BFS queue
def main(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def neighbors(node):
        r, c = node
        return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    def is_valid(node):
        r, c = node

        if r < 0 or r >= rows:
            return False
        if c < 0 or c >= cols:
            return False
        if grid[r][c] != "1":  # noqa: SIM103
            return False

        return True

    def bfs(node):
        queue = deque([node])
        visited.add(node)

        while queue:
            node = queue.popleft()

            for neighbor in neighbors(node):
                if neighbor not in visited and is_valid(neighbor):
                    visited.add(neighbor)
                    queue.append(neighbor)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs((r, c))

    return islands


if __name__ == "__main__":
    args = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "1", "1"],
    ]
    print(main(args))
