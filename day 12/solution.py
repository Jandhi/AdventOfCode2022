with open('day 12/input.txt') as file:
    grid = [line.strip() for line in file.readlines()]

start = None
end = None

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            start = (x, y)
        
        if grid[y][x] == 'E':
            end = (x, y)


visited = set()
queue = [[start]]

def is_neighbour(pos, neighbour_pos, reversed):
    x, y = pos
    nx, ny = neighbour_pos
    if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
        return False
    
    if not reversed:
        if grid[ny][nx] == 'E':
            return grid[y][x] == 'y' or grid[y][x] == 'z'
        elif grid[ny][nx] == 'S':
            return False
        elif grid[y][x] == 'S':
            return ord('a') + 1 >= ord(grid[ny][nx])
        else:
            return ord(grid[y][x]) + 1 >= ord(grid[ny][nx])
    else:
        if grid[ny][nx] == 'E':
            return False
        elif grid[ny][nx] == 'S':
            return ord('a') + 1 >= ord(grid[y][x])
        elif grid[y][x] == 'E':
            return ord(grid[ny][nx]) + 1 >= ord('z')
        else:
            return ord(grid[ny][nx]) + 1 >= ord(grid[y][x])

def get_neighbours(x, y, reversed = False):
    neighbours = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n_pos = (x + dx, y + dy)
        if is_neighbour((x, y), n_pos, reversed):
            neighbours.append(n_pos)
    return neighbours

while len(queue) > 0:
    path = queue.pop(0)
    end_x, end_y = path[-1]
    if (end_x, end_y) in visited:
        continue

    visited.add((end_x, end_y))

    if grid[end_y][end_x] == 'E':
        print(len(path) - 1)
        break
    
    for neighbour in get_neighbours(end_x, end_y):
        if neighbour not in visited:
            queue.append(path + [neighbour])

visited = set()
queue = [[end]]

while len(queue) > 0:
    path = queue.pop(0)
    end_x, end_y = path[-1]
    if (end_x, end_y) in visited:
        continue

    visited.add((end_x, end_y))

    if grid[end_y][end_x] == 'S' or grid[end_y][end_x] == 'a':
        print(len(path) - 1)
        break

    for neighbour in get_neighbours(end_x, end_y, True):
        if neighbour not in visited:
            queue.append(path + [neighbour])