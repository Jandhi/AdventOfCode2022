with open('day 17/input.txt') as file:
    jets = file.readline().strip()
    

rocks = [
    set([(0, 0), (1, 0), (2, 0), (3, 0)]), # worm
    set([(0, 1), (1, 1), (2, 1), (1, 2), (1, 0)]), # plus
    set([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]), # corner
    set([(0, 0), (0, 1), (0, 2), (0, 3)]), # tower
    set([(0, 0), (1, 0), (0, 1), (1, 1)]) # square
]

rock_count = 0

def get_next_rock():
    global rock_count
    rock = rocks[(rock_count) % len(rocks)]
    rock_count += 1
    return rock

def get_transposed(rock, vector):
    return set([(x + vector[0], y + vector[1]) for (x, y) in rock])

# these are nicer to use than dir points
def left(vector):
    return vector[0] - 1, vector[1]

def right(vector):
    return vector[0] + 1, vector[1]

def down(vector):
    return vector[0], vector[1] - 1

jet_count = 0

def get_next_jet():
    global jet_count
    jet = jets[jet_count % len(jets)]
    jet_count += 1
    return jet

width = 7
colliders = set([(x, 0) for x in range(width)])



def print_chute(top_y, rock, rock_point):
    falling_points = get_transposed(rock, rock_point)

    print('-----')
    for y in range(20):
        s = ''
        for x in range(7):
            if (x, top_y - y) in falling_points:
                s += '@'
            elif (x, top_y - y) in colliders:
                s += '#'
            else:
                s += '.'
        print(s)

def clean_colliders(highest_y):
    global colliders
    new_colliders = set()
    for y in range(100):
        for x in range(7):
            if (x, highest_y - y) in colliders:
                new_colliders.add((x, y))
    
    colliders = new_colliders

def sim_fall(fall_count):
    fallen = 0
    highest_y = 0
    while fallen < fall_count:
        rock = get_next_rock()
        rock_x = 2
        rock_y = highest_y + 4

        while True:
            jet = get_next_jet()

            if jet == '<':
                if rock_x > 0 and all((point not in colliders for point in get_transposed(rock, left((rock_x, rock_y))))):
                    rock_x -= 1
            
            if jet == '>':
                if all((point not in colliders and point[0] < width for point in get_transposed(rock, right((rock_x, rock_y))))):
                    rock_x += 1
            
            if rock_y == 1 or any((point in colliders for point in get_transposed(rock, down((rock_x, rock_y))))):
                for p in get_transposed(rock, (rock_x, rock_y)):
                    if p[1] > highest_y:
                        highest_y = p[1]
                    colliders.add(p)

                if len(colliders) > 10000:
                    clean_colliders(highest_y)
                    
                fallen += 1
                break
            else:
                rock_y -= 1

    print(highest_y) 

sim_fall(2022) # 3071

rock_count = 0
jet_count = 0
colliders = set()

sim_fall(1000000000000)