with open('day 3/input.txt') as file:
    sum = 0
    badges = 0
    letters = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lines = [line.removesuffix('\n') for line in file.readlines()]
    counter = 0

    for line in lines:

        midpoint = len(line) // 2
        
        first_compartment = line[:midpoint]
        second_compartment = line[midpoint:]

        for letter in first_compartment:
            if letter in second_compartment:
                val = letters.index(letter)
                sum += val
                break
    
    for i in range(len(lines) // 3):
        badge = set(lines[i * 3]).intersection(set(lines[i * 3 + 1]), set(lines[i * 3 + 2])).pop()
        badges += letters.index(badge)

    print(sum) # 7872
    print(badges) # 2497