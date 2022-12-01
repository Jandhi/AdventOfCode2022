elves = [[]]

with open('day 1/input.txt', 'r') as file:
    line = file.readline()

    while line:
        line = line.removesuffix('\n')

        if line == "":
            elves.append([])
        else:
            num = int(line)
            elves[-1].append(num)

        line = file.readline()

third_max = 0
second_max = 0
max = 0

for inv in elves:
    num = sum(inv)

    if num > max:
        third_max = second_max
        second_max = max
        max = num
    elif num > second_max:
        third_max = second_max
        second_max = num
    elif num > third_max:
        third_max = num

print(max) # 68787
print(max + second_max + third_max) # 198041
