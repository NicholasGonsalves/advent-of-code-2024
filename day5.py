from typing import Dict, List
from collections import defaultdict


def find_middle_page_sum(pages: List[List[int]]) -> int:
    return sum(order[len(order) // 2] for order in pages)


def validate_orders(
    rules: Dict[int, List[int]], pages: List[List[int]]
) -> List[List[int]]:
    return [page for page in pages if validate_order(rules, page)]


def validate_order(rules: Dict[int, List[int]], pages: List[int]) -> bool:
    seen = set()
    for page in pages:
        if seen.intersection(rules[page]):
            return False
        seen.add(page)
    return True


def part1():
    with open("day5.txt", "r") as f:
        rules, pages = f.read().split("\n\n", 1)

    rules = [[int(x) for x in line.split("|", 1)] for line in rules.splitlines()]
    pages = [[int(x) for x in line.split(",")] for line in pages.splitlines()]

    adj = defaultdict(list)
    for r in rules:
        adj[r[0]].append(r[1])

    valid_orders = validate_orders(adj, pages)
    return find_middle_page_sum(valid_orders)


def part2(): ...


if __name__ == "__main__":
    print(part1())
    print(part2())
