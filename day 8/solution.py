def scenic_score(x, y, grid, width, height):
    # edge case (literally)
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return 0

    up = 1
    while y - up > 0 and grid[y - up][x] < grid[y][x]:
        up += 1
    
    down = 1
    while y + down < height - 1 and grid[y + down][x] < grid[y][x]:
        down += 1
    
    left = 1
    while x - left > 0 and grid[y][x - left] < grid[y][x]:
        left += 1
    
    right = 1
    while x + right < width - 1 and grid[y][x + right] < grid[y][x]:
        right += 1
    
    return up * down * right * left


with open('day 8/input.txt') as file:
    grid = [[int(letter) for letter in line.strip()] for line in file.readlines()]
    width, height = len(grid[0]), len(grid)
    visible_grid = [[False for _ in row] for row in grid]

    vis_count = 0

    # down
    for x in range(width):
        tallest = -1
        
        for y in range(height):
            if tallest < grid[y][x]:
                if not visible_grid[y][x]: # no overcounting
                    vis_count += 1

                visible_grid[y][x] = True                
                tallest = grid[y][x]
        
    # up
    for x in range(width):
        tallest = -1

        for y in range(height - 1, 0, -1):
            if tallest < grid[y][x]:
                if not visible_grid[y][x]: # no overcounting
                    vis_count += 1

                visible_grid[y][x] = True
                tallest = grid[y][x]
    
    # right
    for y in range(height):
        tallest = -1

        for x in range(width - 1):
            if tallest < grid[y][x]:
                if not visible_grid[y][x]: # no overcounting
                    vis_count += 1

                visible_grid[y][x] = True
                tallest = grid[y][x]
    
    # left
    for y in range(height):
        tallest = -1

        for x in range(width - 1, 0, -1):
            if tallest < grid[y][x]:
                if not visible_grid[y][x]: # no overcounting
                    vis_count += 1

                visible_grid[y][x] = True
                tallest = grid[y][x]

    print(vis_count)

    high_score = 0
    for x in range(width):
        for y in range(height):
            score = scenic_score(x, y, grid, width, height)
            if score >= high_score:
                high_score = score
    
    print(high_score) # 201684 