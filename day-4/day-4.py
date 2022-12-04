def expand_pair(data: list[str]) -> list[int]:
    return [x for x in range(int(data[0]), int(data[1]) + 1)]


def list_contains(list1, list2) -> bool:
    set1 = set(list1)
    set2 = set(list2)
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    return False


def part_1() -> int:
    total = 0
    with open("input.txt") as file:
        for line in file:
            pairs = line.strip().split(",")

            first_pair = expand_pair(pairs[0].split("-"))
            seccond_pair = expand_pair(pairs[1].split("-"))

            if list_contains(first_pair, seccond_pair):
                total += 1

    return total


if __name__ == "__main__":
    part_1_ans = part_1()
    print(f"part_1_ans: {part_1_ans}")
