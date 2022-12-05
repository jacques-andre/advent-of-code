stacks = {
         1 : ["N", "R", "J", "T", "Z", "B", "D", "F"],
         2 : ["H", "J", "N", "S", "R"],
         3 : ["Q","F","Z","G","J","N","R","C"],
         4 : ["Q","T","R","G","N","V","F"],
         5 : ["F","Q","T","L"],
         6 : ["N", "G", "R", "B", "Z", "W", "C","Q"],
         7: ["M", "H", "N", "S", "L", "C", "F"],
         8: ["J", "T", "M", "Q", "N", "D"],
         9: ["S","G", "P"],
 }

def part_1() -> str:
    with open('input-new.txt') as file:
        lines = [x.strip() for x in file]

    for line in lines:
        command = line.split(' ')

        amount_to_move = int(command[1])
        from_stack = int(command[3])
        to_stack = int(command[5])

        for stack_item in range(0,amount_to_move):
            value_pop = stacks[from_stack].pop()
            stacks[to_stack].append(value_pop)

    ans = ""
    for key, value in stacks.items():
        ans += value[0]
        print(f"{key}:{value}")
    return ans


if __name__ == "__main__":
    part_1_ans = part_1()
    print(f"part_1_ans:{part_1_ans}")
