import string

alphabet_lower = [x for x in string.ascii_lowercase]
alphabet_upper = [x for x in string.ascii_uppercase]

def find_common(list1: list[str], list2: list[str]) -> str:
    for letter in list1:
        if letter in list2:
            return letter
    return ""

def part_1() -> int:
    total = 0
    with open("input.txt") as file:
        for line in file:
            current_rucksack_line = line.strip()
            current_rucksack = [x for x in current_rucksack_line]

            first_compartment = current_rucksack[:len(current_rucksack)//2]
            seccond_compartment = current_rucksack[len(current_rucksack)//2:]

            common_letter = find_common(first_compartment, seccond_compartment)


            letter_value = 0
            if common_letter in alphabet_lower:
                letter_value = alphabet_lower.index(common_letter) + 1

            if common_letter in alphabet_upper:
                letter_value = alphabet_upper.index(common_letter) + 27

            total += letter_value

    return total


def part_2() -> int:
    total = 0
    all_lines = []
    with open("input.txt") as file:
        all_lines = [x.strip() for x in file]

    for i in range(0, len(all_lines),6):
        # TODO: refactor, terrible (but works)
        group_1_rucksack_1 = (list(all_lines[i]))
        group_1_rucksack_2 = (list(all_lines[i+1]))
        group_1_rucksack_3 = (list(all_lines[i+2]))

        group_2_rucksack_1 = (list(all_lines[i+3]))
        group_2_rucksack_2 = (list(all_lines[i+4]))
        group_2_rucksack_3 = (list(all_lines[i+5]))

        common_letter_group_1 = list(set(group_1_rucksack_1).intersection(group_1_rucksack_2, group_1_rucksack_3))[0]
        common_letter_group_2 = list(set(group_2_rucksack_1).intersection(group_2_rucksack_2, group_2_rucksack_3))[0]


        letter_value = 0
        if common_letter_group_1 in alphabet_lower:
            letter_value = alphabet_lower.index(common_letter_group_1) + 1
            total += letter_value

        if common_letter_group_1 in alphabet_upper:
            letter_value = alphabet_upper.index(common_letter_group_1) + 27
            total += letter_value

        if common_letter_group_2 in alphabet_lower:
            letter_value = alphabet_lower.index(common_letter_group_2) + 1
            total += letter_value

        if common_letter_group_2 in alphabet_upper:
            letter_value = alphabet_upper.index(common_letter_group_2) + 27
            total += letter_value

    return total




if __name__ == "__main__":
    part1_ans = part_1()
    print(f"part_1: {part1_ans}")
    part2_ans = part_2()
    print(f"part_2: {part2_ans}")
