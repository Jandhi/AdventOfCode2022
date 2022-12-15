IN_ORDER = 1
NOT_IN_ORDER = -1
CONTINUE = 0

def is_in_order(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                return IN_ORDER
            elif right < left:
                return NOT_IN_ORDER
            else:
                return CONTINUE
        else:
            left = [left]
    
    if not isinstance(right, list):
        right = [right]
    
    length = min(len(left), len(right))

    for i in range(length):
        order = is_in_order(left[i], right[i])

        if order != CONTINUE:
            return order
    
    if len(left) < len(right):
        return IN_ORDER
    elif len(right) < len(left):
        return NOT_IN_ORDER
    else:
        return CONTINUE

sum = 0
items = []

with open('day 13/input.txt') as file:
    index = 0
    while True:
        index += 1
        line1 = file.readline()
        line2 = file.readline()
        blank = file.readline()

        if line1 == None or line1 == '':
            break
        
        left = eval(line1.strip())
        right = eval(line2.strip())

        items.append(left)
        items.append(right)

        if is_in_order(left, right) == IN_ORDER:
            sum += index

print(sum)

# Add dividers
divider_packet1 = [[2]]
divider_packet2 = [[6]]
items.append(divider_packet1)
items.append(divider_packet2)

sorted_items = []
while len(items) > 0:
    item = items.pop()
    index = 0

    while index < len(sorted_items) and is_in_order(sorted_items[index], item) == IN_ORDER:
        index += 1
    
    sorted_items.insert(index, item)

div_index1 = sorted_items.index(divider_packet1) + 1
div_index2 = sorted_items.index(divider_packet2) + 1
print(div_index1 * div_index2)