with open('day 5/input.txt') as file:
    line = file.readline()

    stack_num = (len(line) + 1) // 4
    stacks = [[] for i in range(stack_num)]

    # Make stack
    while line:
        if line[1] == '1':
            line = file.readline()
            break

        for stack_index in range(stack_num):
            string_index = (stack_index * 4) + 1
            letter = line[string_index]
            if letter != ' ':
                stacks[stack_index].insert(0, letter)

        line = file.readline()

    line = file.readline()
    second_stacks = [stack.copy() for stack in stacks]

    while line:
        parts = line.split(' ')
        amount = int(parts[1])
        origin = int(parts[3]) - 1
        destination = int(parts[5]) - 1

        # first stack
        for i in range(amount):
            crate = stacks[origin].pop()
            stacks[destination].append(crate)

        # second stacks
        origin_stack = second_stacks[origin]
        crates = origin_stack[len(origin_stack) - amount:]
        second_stacks[origin] = origin_stack[:len(origin_stack) - amount]
        second_stacks[destination] += crates

        line = file.readline()
    
    for stack_list in (stacks, second_stacks):
        top = [stack.pop() for stack in stack_list]
        print(''.join(top))

    # TLFGBZHCN
    # QRQFHFWCL