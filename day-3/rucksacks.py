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

            print(f"common_letter:{common_letter}, value:{letter_value}")
    return total



if __name__ == "__main__":
    part1_ans = part_1()
    print(part1_ans)
