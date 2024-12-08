from typing import List

DIRS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [-1, 1],
    [1, -1],
    [-1, -1],
    [1, 1],
]


def in_bounds(i: int, j: int, grid: List[List[int]]) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def search(grid: List[List[int]], word: str) -> int:

    def search_helper(i: int, j: int, pos: int, _i: int, _j: int) -> int:
        if word[pos] != grid[i][j]:
            return 0
        if pos == len(word) - 1:
            return 1
        return (
            search_helper(i + _i, j + _j, pos + 1, _i, _j)
            if in_bounds(i + _i, j + _j, grid)
            else 0
        )

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for _i, _j in DIRS:
                total += search_helper(i, j, 0, _i, _j)

    return total


def part1(word: str):
    with open("day4.txt", "r") as f:
        lines = f.read().splitlines()
    return search(lines, word)


def part2(): ...


if __name__ == "__main__":
    print(part1("XMAS"))
    print(part2())
