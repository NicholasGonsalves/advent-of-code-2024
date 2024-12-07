from collections import defaultdict
import heapq


def part1():
    # Read file
    with open("day1.txt","r") as f:
        lines = f.readlines()
    
    # Build heaps
    lheap, rheap = [], []
    for line in lines:
        l, r = line.split("   ", 1)
        heapq.heappush(lheap, int(l))
        heapq.heappush(rheap, int(r))

    # Calculate sum of diffs
    total = 0
    while lheap:
        l_val = heapq.heappop(lheap)
        r_val = heapq.heappop(rheap)
        total += (abs(l_val - r_val))

    return total


def part2():
    # Read file
    with open("day1.txt","r") as f:
        lines = f.readlines()
    
    counts = defaultdict(int)
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
    print(part1())
    print(part2())