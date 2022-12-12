class Monkey:
    def __init__(self, items : list[int], operation, test_num, true_monkey, false_monkey) -> None:
        self.items = items
        self.activity = 0
        self.operation = operation
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def take_turn(self, monkeys, use_worry_reduction, magic_number):
        while len(self.items) > 0:
            self.inspect(self.items.pop(0), monkeys, use_worry_reduction, magic_number)

    def inspect(self, item, monkeys, use_worry_reduction, magic_number):
        self.activity += 1
        item = self.operation(item)
        
        if use_worry_reduction:
            item = item // 3
        else:
            item = item % magic_number

        if item % self.test_num == 0:
            self.throw_to(item, self.true_monkey, monkeys)
        else:
            self.throw_to(item, self.false_monkey, monkeys)

    def throw_to(self, item, index, monkeys):
        monkeys[index].items.append(item)

def round(monkeys, use_worry_reduction, magic_number = 1):
    for monkey in monkeys:
        monkey.take_turn(monkeys, use_worry_reduction, magic_number)

def make_operation(line : str):
    parts = line[19:].strip().split(' ')

    def add(x, y):
        return x + y
    
    def mul(x, y):
        return x * y

    operator = add if parts[1] == '+' else mul

    if parts[2] == 'old':
        return lambda x : operator(x, x)
    else:
        return lambda x : operator(x, int(parts[2]))

def monkey_business(monkeys):
    activity_levels = sorted([monkey.activity for monkey in monkeys])
    return activity_levels[-1] * activity_levels[-2]

first_monkeys = []
second_monkeys = []

def fill_monkeys(arr):
    with open('day 11/input.txt') as file:
        line = file.readline()

        while line.startswith('Monkey'):
            items = [int(item) for item in file.readline()[18:].replace(',', '').strip().split(' ')]
            operation = make_operation(file.readline())
            test_num = int(file.readline().strip().split(' ')[3])
            true_monkey = int(file.readline().strip().split(' ')[5])
            false_monkey = int(file.readline().strip().split(' ')[5])
            arr.append(Monkey(items, operation, test_num, true_monkey, false_monkey))
            file.readline() # get rid of blank
            line = file.readline() # next monke
        
        



fill_monkeys(first_monkeys)
for i in range(20):
    round(first_monkeys, use_worry_reduction=True)

print(monkey_business(first_monkeys)) # 117640 

fill_monkeys(second_monkeys)
magic_number = 1
for m in second_monkeys:
    magic_number = magic_number * m.test_num
for i in range(10000):
    round(second_monkeys, use_worry_reduction=False, magic_number=magic_number)

print(monkey_business(second_monkeys)) # 30616425600