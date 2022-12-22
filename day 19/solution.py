from dataclasses import dataclass

ore_bot_str   = 'Each ore robot costs '
clay_bot_str  = ' ore. Each clay robot costs '
obs_bot_str   = ' ore. Each obsidian robot costs '
geode_bot_str = ' clay. Each geode robot costs '

blueprints = []
class Blueprint:
    def __init__(self, index, cost) -> None:
        self.index = index
        self.cost  = cost

with open('day 19/input.txt') as file:
    line = file.readline()
    i = 1
    while line:
        ore_bot_index = line.find(ore_bot_str)
        clay_bot_index = line.find(clay_bot_str)
        obs_bot_index = line.find(obs_bot_str)
        geode_bot_index = line.find(geode_bot_str)

        ore_cost = (int(line[ore_bot_index + len(ore_bot_str):clay_bot_index]), 0, 0, 0)
        clay_cost = (int(line[clay_bot_index + len(clay_bot_str):obs_bot_index]), 0, 0, 0)

        obs_cost = line[obs_bot_index + len(obs_bot_str) : geode_bot_index].split(' ore and ')
        obs_cost = (int(obs_cost[0]), int(obs_cost[1]), 0, 0)

        geode_cost = line[geode_bot_index + len(geode_bot_str):].replace(' obsidian.\n', '').split(' ore and ')
        geode_cost = (int(geode_cost[0]), 0, int(geode_cost[1]), 0)

        print(f'{[ore_cost[0], clay_cost[0], obs_cost[0], obs_cost[1], geode_cost[0], geode_cost[2]]},')

        blueprints.append(Blueprint(
            i,
            cost = (ore_cost, clay_cost, obs_cost, geode_cost),
        ))

        line = file.readline()
        i += 1

ORE   = 0
CLAY  = 1
OBS   = 2
GEODE = 3
RES_COUNT = 4

local_maxima = [[0 for _ in range(24)] for _ in blueprints]
maxima = [0 for _ in blueprints]
queue = []

best_resources_counts = [[{} for _ in range(24)] for _ in blueprints]

@dataclass
class State:
    blueprint : Blueprint
    index : int
    bots : list[int]
    resources : list[int]
    time_left : int
    intent : int # what bot to buy next

    def can_afford(self, bot_type : int):
        return all(required <= owned for (required, owned) in zip(self.blueprint.cost[bot_type], self.resources))

    def buy(self, bot_type : int):
        self.bots[bot_type] += 1

        for i in range(RES_COUNT):
            self.resources[i] -= self.blueprint.cost[bot_type][i]

    def next_state(self, next_intent : int):
        return State(
                blueprint=self.blueprint,
                index=self.index,
                bots=self.bots.copy(),
                resources=self.resources.copy(),
                time_left=self.time_left,
                intent=next_intent
            )
        
    def tick(self):
        global maxima
        global local_maxima

        if self.time_left == 0:
            if maxima[self.index - 1] < self.resources[GEODE]:
                maxima[self.index - 1] = self.resources[GEODE]
            return

        if self.resources[GEODE] > local_maxima[self.index - 1][self.time_left - 1]:
            local_maxima[self.index - 1][self.time_left - 1] = self.resources[GEODE]

        # bad
        if self.bots[CLAY] == 0 and self.time_left < 15:
            return
        
        # trim bad generators
        if self.resources[GEODE] <= local_maxima[self.index - 1][self.time_left - 1] - 2:
            return
        
        will_buy = self.can_afford(self.intent)

        for i in range(RES_COUNT):
            self.resources[i] += self.bots[i]
        
        self.time_left -= 1

        if will_buy:
            self.buy(self.intent)
        else:
            queue.append(self)
            return

        # Need to get geode bots eventually
        if self.bots[GEODE] == 0 and self.time_left < 8:
            queue.append(self.next_state(GEODE))
            return

        # NEXT INTENT
        if self.time_left > 5:
            queue.append(self.next_state(ORE))

        if self.time_left > 5:
            queue.append(self.next_state(CLAY))

        if self.bots[CLAY] > 0 and self.time_left > 2:
            queue.append(self.next_state(OBS))

        if self.bots[OBS] > 0:
            queue.append(self.next_state(GEODE))

i = 0
for bp in blueprints:
    i += 1
    for intent in range(4):
        queue.append(State(
            blueprint=bp,
            index=i,
            bots=[1,0,0,0],
            resources=[0,0,0,0],
            time_left=24,
            intent=intent,
        ))

min_time = 24

while len(queue) > 0:
    state : State = queue.pop(0)
    state.tick()

    if state.time_left < min_time:
        min_time = state.time_left
        print(min_time)

print(maxima)
print(local_maxima)

total = 0

for i in range(len(blueprints)):
    total += (i + 1) * maxima[i]

print(total)