

from typing import Generator, List

OPERATORS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "||": lambda x, y: int(f"{x}{y}"),
}
OPERATOR_ORDER = ["*", "+"]

def generate_combinations(operators: List[str], num_positions: int) -> Generator[List[str], None, None]:
    if num_positions == 1:
        for op in operators:
            yield [op]
    else:
        for smaller in generate_combinations(operators, num_positions - 1):
            for op in operators:
                yield smaller + [op]

def evaluate_instruction(answer: int, instruction: List[int], operations: List[str]) -> bool:
    for ops in generate_combinations(operations, len(instruction) - 1):

        current = instruction[0]
        for k in range(1, len(instruction)):
            current = OPERATORS[ops[k - 1]](current, instruction[k])
        
        if current == answer:
            return True

    return False

def solve(lines: List[str], operations: List[str]) -> int:
    return sum(
        int(line.split(": ")[0]) if evaluate_instruction(
            int(line.split(": ")[0]), 
            [int(n) for n in line.split(": ")[1].split(" ")],
            operations,
        ) else 0
        for line in lines
    )

def part1():
    with open("day7.txt", "r") as f:
        lines = f.read().split("\n")
    return solve(lines, ["*", "+"])

def part2():
    with open("day7.txt", "r") as f:
        lines = f.read().split("\n")
    return solve(lines, ["*", "+", "||"])



if __name__ == "__main__":
    print(part1())
    print(part2())