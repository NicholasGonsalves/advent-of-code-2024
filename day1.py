from collections import defaultdict
import heapq
from typing import Dict, List


def part1(lines: List[str]) -> int:

    # Build heaps
    lheap: List[int] = []
    rheap: List[int] = []
    for line in lines:
        l, r = line.split("   ", 1)
        heapq.heappush(lheap, int(l))
        heapq.heappush(rheap, int(r))

    # Calculate sum of diffs
    total = 0
    while lheap:
        l_val = heapq.heappop(lheap)
        r_val = heapq.heappop(rheap)
        total += abs(l_val - r_val)

    return total


def part2(lines: List[str]) -> int:

    counts: Dict[int, int] = defaultdict(int)
    left_values = [0] * len(lines)  # Preallocate list

    for i, line in enumerate(lines):
        l, r = line.split("   ", 1)
        counts[int(r)] += 1
        left_values[i] = int(l)

    # Calculate similarity score
    total = 0
    for l_val in left_values:
        total += l_val * counts[l_val]

    return total


if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
