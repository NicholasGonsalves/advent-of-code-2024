from typing import List, Set, Tuple


def in_bounds(i: int, j: int, grid: List[List[str]]) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def find_locations_for_freq(freq: str, grid: List[List[str]]) -> Set[Tuple[int, int]]:
    locations: Set[Tuple[int, int]] = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == freq:
                locations.add((i, j))
    return locations


def find_antinodes(locations: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    antinodes: Set[Tuple[int, int]] = set()
    for (ai, bi) in locations:
        for (aj, bj) in locations:
            # if ai == bi and aj == bj:
            #     continue
            diff = (ai - aj, bi - bj)
            antinodes.add((ai + diff[0], bi + diff[1]))
            antinodes.add((ai - diff[0], bi - diff[1]))
    return antinodes


def part1(grid: List[List[str]]) -> int:
    freqs = set(v for row in grid for v in row if v != ".")
    antinodes = set(
        point 
        for freq in freqs 
        for point in find_antinodes(list(find_locations_for_freq(freq, grid)))
        if in_bounds(point[0], point[1], grid)
        and grid[point[0]][point[1]] != freq
    )
    return len(antinodes)


def part2(lines: List[List[str]]) -> int:
    return 0


if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        grid = [list(line) for line in f.read().split("\n")]

    print(part1(grid))
    print(part2(grid))
