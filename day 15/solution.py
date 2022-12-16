sensor_beacon_pairs = []
ranges = [] # these are INCLUSIVE
py = 2000000

def parse_coords(input : str):
    return tuple(int(num) for num in input.split(', y='))

with open('day 15/input.txt') as file:
    line = file.readline()

    while line:
        parts = line[len('Sensor at x='):].strip().split(': closest beacon is at x=')
        sx, sy = parse_coords(parts[0])
        bx, by = parse_coords(parts[1])
        sensor_beacon_pairs.append((sx, sy, bx, by))
        dist = abs(sx - bx) + abs(sy - by)
        width_at_sy = 2 * dist + 1
        ydiff = abs(sy - py)
        width_at_py = width_at_sy - 2 * ydiff
        if width_at_py > 0:
            ranges.append((sx - width_at_py // 2, sx + width_at_py // 2))
        line = file.readline()

def add_range(range : tuple[int, int], ranges : list[tuple[int, int]]):
    i = 0
    low, high = range

    while len(ranges) > i:
        other_low, other_high = ranges[i]

        if other_low <= low <= other_high or other_low <= high <= other_high: # intersection!
            low = min(low, other_low)
            high = max(high, other_high)
            ranges.pop(i)
            i -= 1

        i += 1
    
    ranges.insert(i, (low, high))

def clean_ranges(ranges): # get rid of redundancy
    new_ranges = []
    for r in ranges:
        add_range(r, new_ranges)
    return new_ranges

ranges = clean_ranges(ranges)

total = 0
for range in ranges:
    total += range[1] - range[0]
print(total) # 5166077

x, y = 0, 0
covered = True
while covered:
    if y % 1000 == 0:
        print(y)

    covered = False

    if x > 4000000:
        x = 0
        y += 1

    for sx, sy, bx, by in sensor_beacon_pairs:
        dist = abs(sx - bx) + abs(sy - by)
        width_at_sy = 2 * dist + 1
        ydiff = abs(sy - y)
        width_at_y = width_at_sy - 2 * ydiff

        if width_at_y <= 0:
            continue

        low, high = (sx - width_at_y // 2, sx + width_at_y // 2)

        if low <= x <= high:
            covered = True
            x = high + 1

print(x * 4000000 + y) # 13071206703981