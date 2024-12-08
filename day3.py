def evaluate(program: str) -> int:
    total = 0
    for possible_expression in program.split("mul("):
        inside_plus = possible_expression.split(")", 1)
        if len(inside_plus) == 1:
            continue
        inside = inside_plus[0]
        if "," not in inside:
            continue
        l, r = inside.split(",")
        if l.isdigit() and r.isdigit():
            total += int(l) * int(r)
    return total


def part1():
    with open("day3.txt", "r") as f:
        lines = f.read()
    return evaluate(lines)


def part2():
    with open("day3.txt", "r") as f:
        lines = f.read()

    total = 0
    for do_portion in lines.split("do()"):
        enabled = True
        for section in do_portion.split("don't()"):
            if enabled:
                total += evaluate(section)
            enabled = False

    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
