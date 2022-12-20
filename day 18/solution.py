points = set()

AIR = 0
STEAM = 1
CELL = 2

drops = [[[AIR for _ in range(25)] for _ in range(25)] for _ in range(25)]

with open('day 18/input.txt') as file:
    line = file.readline()
    while line:
        x, y, z = tuple(int(num) for num in (line.strip().split(',')))
        points.add((x, y, z))
        drops[x][y][z] = CELL
        line = file.readline()

dirs = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def out_of_bounds(a):
    return a < 0 or a >= 25

faces = 0
for pt in points:
    for dir in dirs:
        x, y, z = add(pt, dir)
        if drops[x][y][z] != CELL:
            faces += 1
print(faces)

queue = [(0, 0, 0)]
visited = set()

while len(queue) > 0:
    x, y, z = queue.pop(0)

    if (x, y, z) in visited:
        continue

    drops[x][y][z] = STEAM

    visited.add((x, y, z))

    for (dx, dy, dz) in dirs:
        if out_of_bounds(x + dx) or out_of_bounds(y + dy) or out_of_bounds(z + dz):
            continue

        if (x + dx, y + dy, z + dz) in visited:
            continue

        if drops[x + dx][y + dy][z + dz] != CELL:
            queue.append((x + dx, y + dy, z + dz))
        
faces = 0
for pt in points:
    for dir in dirs:
        x, y, z = add(pt, dir)
        if drops[x][y][z] == STEAM:
            faces += 1
print(faces)