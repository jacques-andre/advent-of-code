
stacks = {
        1: ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],
        2: ['R', 'S', 'N', 'J', 'H'],
        3: ['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],
        4: ['F', 'V', 'N', 'G', 'R', 'T', 'Q'],
        5: ['L', 'T', 'Q', 'F'],
        6: ['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],
        7: ['F', 'C', 'L', 'S', 'N', 'H', 'M'],
        8: ['D', 'N', 'Q', 'M', 'T', 'J'],
        9: ['P', 'G', 'S'],
        }

# example_stacks = {
#         1: ["Z","N"],
#         2: ["M","C","D"],
#         3: ["P"]
#         }

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
        ans += value[-1]
        print(f"{key}:{value}")
    return ans

def part_2() -> str:
    with open('input-new.txt') as file:
        lines = [x.strip() for x in file]

    for line in lines:
        command = line.split(' ')

        amount_to_move = int(command[1])
        from_stack = int(command[3])
        to_stack = int(command[5])

        if amount_to_move == 1:
            value_pop = stacks[from_stack].pop()
            stacks[to_stack].append(value_pop)
        else:
            to_move = stacks[from_stack][-amount_to_move:]
            del stacks[from_stack][-amount_to_move:]
            stacks[from_stack][:amount_to_move]
            stacks[to_stack].extend(to_move)
                

    ans = ""
    for key, value in stacks.items():
        ans += value[-1]
        print(f"{key}:{value}")
    return ans


if __name__ == "__main__":
    part_1_ans = part_1()
    print(f"part_1_ans:{part_1_ans}")
    part_2_ans = part_2()
    print(f"part_2_ans:{part_2_ans}")
    print(part_2_ans[::-1])
