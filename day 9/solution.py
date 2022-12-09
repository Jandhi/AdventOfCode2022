def get_move(position, leader):
    px, py = position
    lx, ly = leader

    def sign(num):
        return 1 if num > 0 else -1

    dx, dy = (lx - px, ly - py)
    if dx == 0 and abs(dy) == 2:
        return (0, sign(dy))
    elif dy == 0 and abs(dx) == 2:
        return (sign(dx), 0)
    elif dx != 0 and dy != 0 and (abs(dx) + abs(dy)) > 2:
        return (sign(dx), sign(dy))
    return (0, 0)
    
with open('day 9/input.txt') as file:
    first_visited = set()
    second_visited = set()

    direction_vector = {
        'R' : (1, 0),
        'L' : (-1, 0),
        'U' : (0, 1),
        'D' : (0, -1),
    }
    dx, dy = (0, 0)
    moves = 0

    first_knots = [(0, 0) for _ in range(2)]
    second_knots = [(0, 0) for _ in range(10)]

    while True:
        for knots, visited in ((first_knots, first_visited), (second_knots, second_visited)):
            if knots[-1] not in visited:
                visited.add(knots[-1])

        if moves == 0:
            line = file.readline()

            if line is None or line == '':
                break # end of program

            parts = line.strip().split(' ')
            dx, dy = direction_vector[parts[0]]
            moves = int(parts[1])
        
        for knots in (first_knots, second_knots):
            head_x, head_y = knots[0]
            knots[0] = (head_x + dx, head_y + dy)

            for i in range(len(knots) - 1):
                move_x, move_y = get_move(knots[i + 1], knots[i])
                tail_x, tail_y = knots[i + 1]
                knots[i + 1] = (tail_x + move_x, tail_y + move_y)
        
        moves -= 1
    
    print(len(first_visited)) # 6642
    print(len(second_visited)) # 2765