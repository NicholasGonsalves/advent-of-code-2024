from typing import Dict, List, Tuple
from collections import defaultdict


def parse_rules_and_pages(
    rules: str, pages: str
) -> Tuple[Dict[int, List[int]], List[List[int]]]:
    rules = [[int(x) for x in line.split("|", 1)] for line in rules.splitlines()]
    pages = [[int(x) for x in line.split(",")] for line in pages.splitlines()]

    adj = defaultdict(list)
    for r in rules:
        adj[r[0]].append(r[1])
    return adj, pages


def find_middle_page_sum(pages: List[List[int]]) -> int:
    return sum(order[len(order) // 2] for order in pages)


def filter_orders_by_validity(
    rules: Dict[int, List[int]],
    pages: List[List[int]],
    valid: bool = True,
) -> List[List[int]]:
    return [page for page in pages if filter_order_by_validity(rules, page, valid)]


def filter_order_by_validity(
    rules: Dict[int, List[int]], pages: List[int], valid: bool = True
) -> bool:
    seen = set()
    for page in pages:
        if seen.intersection(set(rules[page])):
            return not valid
        seen.add(page)
    return valid


def toposort(graph: Dict[int, List[int]]) -> List[int]:
    # Calculate in-degrees for all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    zero_in_degree = [node for node in in_degree if in_degree[node] == 0]

    sorted_order = []
    while zero_in_degree:
        current = zero_in_degree.pop()
        sorted_order.append(current)

        for neighbor in graph.get(current, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(sorted_order) != len(in_degree):
        raise ValueError("Found a cycle (we can;t sort a non-DAG!)")

    return sorted_order


def correct_order(rules: Dict[int, List[int]], order: List[int]) -> List[int]:
    relevant_rules = {
        k: [p for p in v if p in order] for k, v in rules.items() if k in order
    }
    return toposort(relevant_rules)


def correct_ordering(
    rules: Dict[int, List[int]], orders: List[List[int]]
) -> List[List[int]]:
    return [correct_order(rules, order) for order in orders]


def part1():
    with open("day5.txt", "r") as f:
        rules, _pages = f.read().split("\n\n", 1)

    adj, pages = parse_rules_and_pages(rules, _pages)
    valid_orders = filter_orders_by_validity(adj, pages, True)
    return find_middle_page_sum(valid_orders)


def part2():
    with open("day5.txt", "r") as f:
        rules, _pages = f.read().split("\n\n", 1)

    adj, pages = parse_rules_and_pages(rules, _pages)
    invalid_orders = filter_orders_by_validity(adj, pages, False)
    corrected_orders = correct_ordering(adj, invalid_orders)
    return find_middle_page_sum(corrected_orders)


if __name__ == "__main__":
    print(part1())
    print(part2())
