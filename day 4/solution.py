with open('day 4/input.txt') as file:
    full_overlaps = 0
    overlaps = 0
    for line in file.readlines():
        line = line.removesuffix('\n')
        parts = line.split(',')
        elf1 = list(map(int, parts[0].split('-')))
        elf2 = list(map(int, parts[1].split('-')))

        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
            full_overlaps += 1
        
        if (elf1[0] <= elf2[0] <= elf1[1]) or (elf2[0] <= elf1[0] <= elf2[1]):
            overlaps += 1
    
    print(full_overlaps) # 424
    print(overlaps) # 804