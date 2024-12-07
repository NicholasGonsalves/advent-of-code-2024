from typing import List


def is_safe(levels: List[int]) -> bool:
    diffs = [a - b for a, b in zip(levels, levels[1:])]
    if any(abs(diff) < 1 or abs(diff) > 3 for diff in diffs):
        return False
    if not (all(diff >= 0 for diff in diffs) or all(diff <= 0 for diff in diffs)):
        return False
    return True


def part1():
    with open("day2.txt","r") as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        levels = [int(level) for level in line.split(" ")]
        total += is_safe(levels)
    return total


def part2():
    with open("day2.txt","r") as f:
        lines = f.readlines()
    
    # brute force..
    total = 0
    for line in lines:
        levels = [int(level) for level in line.split(" ")]
        if is_safe(levels):
            total += 1
            continue
        for i in range(len(levels)):
            tmp = levels[:]
            _ = tmp.pop(i)
            if is_safe(tmp):
                total += 1
                break
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())