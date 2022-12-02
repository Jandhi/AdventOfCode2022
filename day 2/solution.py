

score = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

with open('day 2/input.txt') as file:
    my_score = 0
    my_strategic_score = 0

    for line in file.readlines():
        their_play = score[line[0]]
        my_play = score[line[2]]
        needed_outcome = score[line[2]] - 2

        my_score += my_play

        if my_play == their_play:
            my_score += 3 # tie
        elif my_play % 3 == (their_play % 3 + 1) % 3:
            my_score += 6 # win!

        my_strategy = (their_play + needed_outcome) % 3

        if my_strategy == 0:
            my_strategy = 3
        
        my_strategic_score += my_strategy
        my_strategic_score += (3 + 3 * needed_outcome)

    print(my_score)
    print(my_strategic_score)