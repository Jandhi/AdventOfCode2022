with open('day 20/sample.txt') as file:
    arr = [int(num.strip()) for num in file.readlines()]

verbose = False

decryption_key = 811589153
size = len(arr)

def transform(num):
    ans = (num * decryption_key) % (size - 1)

    if num < 0:
        return ans - (size - 1)
    else:
        return ans

arr2 = [transform(num) for num in arr]

def mix(arr):
    indices = [i for i in range(size)]

    for i in range(size):
        index = indices[i]
        item = arr[index]
        destination = (index + item) % (size - 1)

        if item < 0 and destination == 0:
            destination = size - 1
        
        if destination > index:
            before = arr[:index]
            between = arr[index+1:destination+1]
            after = arr[destination+1:]

            # all in between lose 1 in index

            for j in range(size):
                if index + 1 <= indices[j] < destination + 1:
                    indices[j] -= 1

            arr = before + between + [item] + after
            indices[i] = destination

        elif destination < index:
            before = arr[:destination]
            between = arr[destination:index]
            after = arr[index+1:]

            # all in between gain 1 in index

            for j in range(size):
                if destination + 1 <= indices[j] < index + 1:
                    indices[j] -= 1
            
            arr = before + [item] + between + after
            indices[i] = destination
        elif verbose:
            print(f'{item} does not move')
            print(arr)
            continue
        
        if not verbose:
            continue
        
        print(f'{item} at {index} moves {item % size} between {arr[(destination - 1) % size]} and {arr[(destination + 1) % size]}')
        print(arr)

    return arr

arr = mix(arr)

def get_sol(arr, p2 = False):
    zero_index = arr.index(0)
    def at(i):
        return arr[(i + zero_index) % len(arr)] 
        
    print(at(1000) + at(2000) + at(3000))

get_sol(arr)

print(arr2)
for i in range(10):
    arr2 = mix(arr2)
    print(f'MIX {i + 1} : {arr2}')

get_sol(arr2, p2=True)

r1 = [0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153]
r2 = [0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153]

def normalize(r):
    return [(num % (size - 1)) - ((size - 1) if num < 0 else 0) for num in r]

print(normalize(r1))
print(normalize(r2))

verbose = True

mix(normalize(r1))

