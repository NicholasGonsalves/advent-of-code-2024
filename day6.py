from typing import Dict, List, Set, Tuple
from collections import defaultdict

from typing import List

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def in_bounds(i: int, j: int, grid: List[List[int]]) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def find_start(grid: List[str]) -> Tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i, j
    raise ValueError("Failed to find start!")


def calculated_visited_set(
    i: int, j: int, grid: List[List[str]]
) -> Set[Tuple[int, int]]:
    dir = 0
    visited = set()
    while True:
        visited.add((i, j))
        newi, newj = i + DIRS[dir][0], j + DIRS[dir][1]
        if not in_bounds(newi, newj, grid):
            break
        if grid[newi][newj] == "#" or grid[newi][newj] == "O":
            dir = (dir + 1) % 4
            newi, newj = i + DIRS[dir][0], j + DIRS[dir][1]
            if not in_bounds(newi, newj, grid):
                break
        i, j = newi, newj
    return visited


def part1() -> int:
    with open("day6.txt", "r") as f:
        grid = [list(l) for l in f.read().split("\n")]
    start_i, start_j = find_start(grid)
    return len(calculated_visited_set(start_i, start_j, grid))


def walk_check_cycle(i: int, j: int, grid: List[List[str]]) -> bool:
    dir = 0
    visited = set()
    while (i, j, dir) not in visited:
        visited.add((i, j, dir))
        newi, newj = i + DIRS[dir][0], j + DIRS[dir][1]
        if not in_bounds(newi, newj, grid):
            return False
        if grid[newi][newj] == "#" or grid[newi][newj] == "O":
            dir = (dir + 1) % 4
            newi, newj = i + DIRS[dir][0], j + DIRS[dir][1]
            if not in_bounds(newi, newj, grid):
                return False
        i, j = newi, newj
    return True


def part2() -> int:
    with open("day6.txt", "r") as f:
        grid = [list(l) for l in f.read().split("\n")]
    start_i, start_j = find_start(grid)
    visited_set = calculated_visited_set(start_i, start_j, grid)
    visited_set.remove((start_i, start_j))
    # brute force - consider each and check if it causes a loop
    total = 0
    for check_i, check_j in visited_set:
        grid[check_i][check_j] = "O"
        # if walk_check_cycle(start_i, start_j, grid):
        #     for row in grid:
        #         print("".join(row))
        #     print("-----------------")
        total += walk_check_cycle(start_i, start_j, grid)
        grid[check_i][check_j] = "."
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
