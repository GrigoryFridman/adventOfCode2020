# Part 1

# with open("input.txt", "r") as file:
#     instructions = file.readlines()
#     acc = 0
#     pointer = 0
#     exec_instructions = []
#     while pointer not in exec_instructions:
#         exec_instructions.append(pointer)
#         operation = instructions[pointer][:3]
#         argument = int(instructions[pointer][4:])
#         if operation == 'acc':
#             acc += argument
#             pointer += 1
#         elif operation == 'jmp':
#             pointer += argument
#         elif operation == 'nop':
#             pointer += 1
#     print(acc)

# Part 2


def terminates(instructs):
    acc = 0
    pointer = 0
    exec_instructions = []
    while pointer not in exec_instructions:
        if pointer >= len(instructs):
            return True, acc
        exec_instructions.append(pointer)
        operation = instructs[pointer][:3]
        argument = int(instructs[pointer][4:])
        if operation == 'acc':
            acc += argument
            pointer += 1
        elif operation == 'jmp':
            pointer += argument
        elif operation == 'nop':
            pointer += 1
    return False, acc


with open('input.txt', 'r') as file:
    instructions = file.readlines()
    for idx, instruction in enumerate(instructions):
        changed_instructions = instructions.copy()
        if instruction[:3] == 'jmp':
            changed_instructions[idx] = instruction.replace('jmp', 'nop')
        elif instruction[:3] == 'nop':
            changed_instructions[idx] = instruction.replace('nop', 'jmp')
        terms, acc = terminates(changed_instructions)
        if terms:
            print(acc)
