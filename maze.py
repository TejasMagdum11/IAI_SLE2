"""
BFS and DFS Maze Pathfinding
------------------------------
Combined single-file version of maze.py, bfs.py, dfs.py, and main.py.
"""

from collections import deque
from time import perf_counter


# ----------------------------
# maze.py
# ----------------------------

def get_neighbors(maze, cell):
    """Return valid 4-directional open-cell neighbors."""
    rows, cols = len(maze), len(maze[0])
    r, c = cell
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
            yield (nr, nc)


def create_sample_maze():
    """Create a small sample maze. 0 = open, 1 = wall."""
    return [
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]


# ----------------------------
# bfs.py
# ----------------------------

def bfs(maze, start, goal):
    """Breadth-First Search. Returns path, path length, and nodes expanded."""
    queue = deque([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    if goal not in parent:
        return [], 0, nodes_expanded

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, len(path) - 1, nodes_expanded


# ----------------------------
# dfs.py
# ----------------------------

def dfs(maze, start, goal, depth_limit=200):
    """Depth-Limited DFS. Returns path, path length, and nodes expanded."""
    visited = set()
    nodes_expanded = 0

    def search(current, path, depth):
        nonlocal nodes_expanded
        nodes_expanded += 1

        if current == goal:
            return path

        if depth >= depth_limit:
            return None

        visited.add(current)

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                result = search(neighbor, path + [neighbor], depth + 1)
                if result is not None:
                    return result

        return None

    result = search(start, [start], 0)

    if result is None:
        return [], 0, nodes_expanded

    return result, len(result) - 1, nodes_expanded


# ----------------------------
# main.py
# ----------------------------

def display_result(name, result):
    path, length, nodes = result
    print(f"\n{name}")
    print("-" * 30)
    print("Path:", path)
    print("Path length:", length)
    print("Nodes expanded:", nodes)


def main():
    maze = create_sample_maze()
    start = (0, 0)
    goal = (7, 7)

    start_time = perf_counter()
    bfs_result = bfs(maze, start, goal)
    bfs_time = (perf_counter() - start_time) * 1000

    start_time = perf_counter()
    dfs_result = dfs(maze, start, goal, depth_limit=200)
    dfs_time = (perf_counter() - start_time) * 1000

    print("BFS vs DFS Maze Pathfinding")
    print("=" * 40)

    display_result("BFS", bfs_result)
    print(f"Execution time: {bfs_time:.4f} ms")

    display_result("DFS (depth limit = 200)", dfs_result)
    print(f"Execution time: {dfs_time:.4f} ms")


if __name__ == "__main__":
    main()
