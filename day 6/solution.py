with open('day 6/input.txt') as file:
    string = file.readline()

    for amt in (4, 14):
        for i in range(len(string)):
            if len(set(string[i:i+amt])) == amt:
                break
        print(i + amt)
    
    # 1282
    # 3513