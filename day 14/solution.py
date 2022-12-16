import os

rock = set()
sand = set()

maxy = 0 # used to track falling into the void
def add_rock(p):
    if p not in rock:
        rock.add(p)

def solid(p):
    return p in rock or p in sand

with open('day 14/input.txt') as file:
    for line in file.readlines():
        points = [tuple(int(num) for num in pair.split(',')) for pair in line.strip().split(' -> ')]
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            if max(y1, y2) > maxy:
                maxy = max(y1, y2)

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    add_rock((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    add_rock((x, y1))


sand_origin = (500, 0)
sand_count = 0
sx, sy = sand_origin

# leaving this here for debug purposes
def print_sand():
    os.system('cls')
    for y in range(0, maxy + 3):
        s = ''
        for x in range(480, 520):
            if (x, y) == sand_origin:
                s += '+'
            elif (x, y) in rock:
                s += '#'
            elif (x, y) in sand:
                s += 'o'
            elif (x, y) == (sx, sy):
                s += '@'
            else:
                s += '.'
        print(s)

# ugly to move into 
def simulate():
    global sx, sy, sand_count
    while True:
        cont = False

        if sy == maxy * 2 or sand_origin in sand:
            return

        for dx, dy in ((0, 1), (-1, 1), (1, 1)):
            if not solid((sx + dx, sy + dy)):
                sx, sy = (sx + dx, sy + dy)
                cont = True
                break

        if cont:
            continue
        
        sand.add((sx, sy))
        sand_count += 1
        sx, sy = sand_origin

simulate()
print(sand_count) # 817

sand = set()
floor = maxy + 2
for x in range(-1000, 1000):
    rock.add((x + 500, floor))

simulate()
print(sand_count) # 23416