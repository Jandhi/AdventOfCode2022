with open('day 10/input.txt') as file:
    lines = file.readlines()

    clock = 1
    x = 1
    signal_sum = 0
    crt = ''

    def crt_update():
        global crt
        crt_pos = (clock - 1) % 40

        print(crt_pos, x)
        if crt_pos - 1 <= x <= crt_pos + 1:
            crt += '#'
        else:
            crt += '.'

        if clock % 40 == 0:
            crt += '\n'
    
    def cycle():
        global signal_sum, crt

        if clock in (20, 60, 100, 140, 180, 220):
            signal_sum += x * clock

    for line in lines:
        crt_update()
        clock += 1
        cycle()

        if line.startswith("addx"):
            val = int(line.split(' ')[1].strip())
            crt_update()
            x += val
            clock += 1
            cycle()
    
    print(signal_sum) # 14220
    print(crt)