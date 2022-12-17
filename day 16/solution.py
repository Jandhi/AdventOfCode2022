nodes = {}

class Node:
    def __init__(self, name, flow_rate, neighbours) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours
        self.distances = {}
        nodes[self.name] = self
    
    def neighbour_nodes(self) -> list:
        return [nodes[name] for name in self.neighbours]

    def __repr__(self) -> str:
        return self.name

def find_distances(node : Node):
    visited = set(node.name)
    queue = [node]
    distances = {node : 0}

    while len(queue) > 0:
        curr : Node = queue.pop(0)

        for neighbour in curr.neighbour_nodes():
            if neighbour in visited:
                continue

            distances[neighbour] = distances[curr] + 1
            visited.add(neighbour)
            queue.append(neighbour)
    
    node.distances = distances

with open('day 16/input.txt') as file:
    line = file.readline()

    while line:
        # jank for plurals
        parts = line.strip().replace('valves', 'valve').replace('tunnels', 'tunnel').replace('leads', 'lead').split('; tunnel lead to valve ')
        first_parts = parts[0][len('Valve '):].split(' has flow rate=')
        name = first_parts[0]
        flow_rate = int(first_parts[1])
        neighbours = parts[1].split(', ')
        Node(name, flow_rate, neighbours)
        line = file.readline()

for node in nodes.values():
    find_distances(node)

nodes_by_flow_rate = sorted([node for node in nodes.values() if node.flow_rate > 0], key = lambda node : node.flow_rate)

def cost_of_path(path):
    curr : Node = nodes['AA']
    cost = 0

    for node in path:
        cost += 1 + curr.distances[node]
        curr = node
    
    return cost

def reward_of_path(path, total_time=30):
    curr : Node = nodes['AA']
    reward = 0
    cost = 0

    for node in path:
        cost += 1 + curr.distances[node]
        curr = node
        reward += (node.flow_rate * (total_time - cost))
    
    return reward

node_set = set(nodes_by_flow_rate)
queue = [[node] for node in nodes_by_flow_rate]
best_path = []
iterations = 0
cutoff = 1000 # I assume that any two paths picked in part 2 are each going to be at least as good as some cutoff, to make sure I don't need to search as wide

eligible_paths = []

while len(queue) > 0:
    path = queue.pop(0)

    if reward_of_path(path) > reward_of_path(best_path):
        best_path = path
    
    for node in node_set - set(path):
        new_path = path + [node]

        if cost_of_path(new_path) > 30:
            continue
        
        if cost_of_path(new_path) <= 26 and reward_of_path(new_path) > cutoff:
            eligible_paths.append((new_path, reward_of_path(new_path, total_time=26)))

        queue.append(new_path)

print(reward_of_path(best_path), best_path) # 1460 [OG, UU, KT, OX, ZR, GU]

best_pair = None
best_rw = 0


for path, reward in eligible_paths:
    for other_path, other_reward in eligible_paths:
        if len(set(path).intersection(set(other_path))) == 0:
            rw = reward + other_reward

            if rw > best_rw:
                best_rw = rw
                best_pair = path, other_path

print(best_rw, best_pair)