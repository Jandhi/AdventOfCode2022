class Directory:
    all = []
    
    def __init__(self) -> None:
        self.parent = None
        self.children = {}
        self.files = {}
        self.size = 0
        Directory.all.append(self)
    
    def add_child(self, name):
        child = Directory()
        child.parent = self
        self.children[name] = child
        return child
    
    def add_file(self, name, size):
        self.files[name] = size
        self.add_size(size)

    def add_size(self, size):
        self.size += size

        if self.parent is not None:
            self.parent.add_size(size)

with open('day 7/input.txt') as file:
    root = Directory()
    current_dir = root

    line = file.readline().strip()

    while line:
        if line == "$ cd /":
            current_dir = root
        elif line == "$ cd ..":
            current_dir = current_dir.parent
        elif line.startswith("$ cd "):
            name = line[5:]
            current_dir = current_dir.children[name]
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            name = line[4:]
            current_dir.add_child(name)
        else:
            parts = line.split(' ')
            size = int(parts[0])
            name = parts[1]
            current_dir.add_file(name, size)

        line = file.readline().strip()
    
    print(sum([dir.size for dir in Directory.all if dir.size <= 100000])) # 1182909

    needed = root.size + 30000000 - 70000000

    best = None
    for dir in Directory.all:
        if dir.size >= needed and (best is None or best.size > dir.size):
            best = dir
    
    print(best.size) # 2832508