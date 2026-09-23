# IAI_SLE2
# BFS and DFS Maze Pathfinding

## Project Overview

This project implements and compares two search techniques used in Artificial Intelligence:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)

Both algorithms solve a grid-based maze using 4-directional movement.

## Files

- `bfs.py` - BFS implementation.
- `dfs.py` - Depth-limited DFS implementation.
- `maze.py` - Maze and neighbor-generation functions.
- `main.py` - Runs both algorithms and displays results.
- `CONTRIBUTIONLOG.md` - AI and student contribution record.

## Maze Representation

- `0` = open cell
- `1` = wall
- Start = `(0, 0)`
- Goal = `(7, 7)`

## BFS

BFS explores nodes level by level using a queue.

### Main property

BFS finds the shortest path in an unweighted grid when a path exists.

## DFS

DFS explores one direction as deeply as possible before backtracking.

This project uses a depth limit of 200.

### Main property

DFS can find a path without guaranteeing that the path is the shortest.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python main.py
```

The program displays:

- Path found
- Path length
- Nodes expanded
- Execution time

## Complexity

For a general search problem:

- BFS: O(b^d) time and O(b^d) space
- DFS: O(b^m) time and O(m) space

where:
- `b` = branching factor
- `d` = depth of the shallowest solution
- `m` = depth limit/search depth

## Project Purpose

The purpose is to understand how BFS and DFS behave differently when solving a maze and to compare their execution behavior and solution quality.
