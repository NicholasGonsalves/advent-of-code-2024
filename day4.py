
DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

WORD = "XMAS"

def backtrack(i, j, grid, pos) -> int:
    ...

def part1():
    with open("day3.txt","r") as f:
        lines = f.read()
    return backtrack(lines)


def part2():
    ...
    

if __name__ == "__main__":
    print(part1())
    print(part2())