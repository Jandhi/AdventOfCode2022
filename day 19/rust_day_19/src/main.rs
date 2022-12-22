use std::{collections::VecDeque, vec};

#[derive(Debug, Copy, Clone)]
enum Resource {
    Ore = 0,
    Clay = 1,
    Obsidian = 2,
    Geode = 3
}

fn index(resource : &Resource) -> usize {
    *resource as usize
}

#[derive(Debug, Copy, Clone)]
struct Blueprint {
    index: u16,
    costs: [[u16; 4]; 4]
}

#[derive(Debug, Clone)]
struct State {
    index: u16,
    blueprint: Blueprint,
    bots: [u16; 4],
    resources: [u16; 4],
    time_left: u16,
    intent: Resource,
}

impl State {
    fn can_afford(&self, bot_type : &Resource) -> bool {
        for i in 0..4 {
            if self.resources[i] < self.blueprint.costs[index(bot_type)][i] {
                return  false;
            }
        }

        true
    }

    fn buy(&mut self, bot_type : Resource) {
        for i in 0..4 {
            self.resources[i] -= self.blueprint.costs[index(&bot_type)][i];
        }

        self.bots[index(&bot_type)] += 1
    }

    fn next_state(&self, next_intent : Resource) -> State {
        State {
            index: self.index,
            blueprint: self.blueprint,
            bots: self.bots,
            resources: self.resources,
            time_left: self.time_left,
            intent: next_intent,
        }
    }

    fn gain_resources(&mut self) {
        for i in 0..4 {
            self.resources[i] += self.bots[i] as u16; 
        }
    }

    fn get_next_states(&mut self, part_two : bool) -> Vec<State> {
        let will_buy : bool = self.can_afford(&self.intent);

        self.gain_resources();
        self.time_left -= 1;

        if will_buy {
            self.buy(self.intent);
        } else {
            return  vec![self.clone()];
        }

        let mut next_states : Vec<State> = vec![];

        if self.time_left > 15 || (self.time_left > 10 && !part_two) { // Cutoff is 10 for p1
            next_states.push(self.next_state(Resource::Ore));
        }

        if self.time_left > 10 || (self.time_left > 5 && !part_two) { // Cutoff is 5 for p1
            next_states.push(self.next_state(Resource::Clay));
        }

        if self.bots[index(&Resource::Clay)] > 0 {
            next_states.push(self.next_state(Resource::Obsidian));
        }

        if self.bots[index(&Resource::Obsidian)] > 0 {
            next_states.push(self.next_state(Resource::Geode));
        }

        next_states
    }

    fn amount(&self, resource : &Resource) -> u16 {
        self.resources[index(resource)]
    }
}

fn most_geodes(blueprint : Blueprint, time: u16) -> u16 {
    let mut max_geodes: u16 = 0;
    let mut iterations: u32 = 0;

    let mut queue: VecDeque<State> = VecDeque::new();

    for res in [Resource::Ore, Resource::Clay] {
        queue.push_back(State {
            index: blueprint.index,
            blueprint: blueprint,
            bots: [1, 0, 0, 0],
            resources: [0, 0, 0, 0],
            time_left: time,
            intent: res,
        });
    }

    while queue.len() > 0 {
        iterations += 1;
        let mut state = queue.pop_front().expect("Queue is empty");

        if state.time_left == 0 {
            if max_geodes < state.amount(&Resource::Geode) {
                max_geodes = state.amount(&Resource::Geode);
            }
            continue;
        }

        for next in state.get_next_states(time == 32) {
            queue.push_back(next);
        }
    }

    println!("{}", iterations);


    max_geodes
}

fn load_blueprints(input : Vec<[u16; 6]>) -> Vec<Blueprint> {
    let mut i = 0;
    let mut bps : Vec<Blueprint> = vec![];

    for arr in input {
        i += 1;
        bps.push(Blueprint{
            index: i,
            costs: [
                [arr[0], 0, 0, 0],
                [arr[1], 0, 0, 0],
                [arr[2], arr[3], 0, 0],
                [arr[4], 0, arr[5], 0],
            ]
        })
    }

    bps
}

fn main() {
    let _sample = vec![
        [4, 2, 3, 14, 2, 7],
        [2, 3, 3, 8, 3, 12],
    ];

    let input = vec![
        [4, 4, 2, 11, 2, 7],
        [4, 4, 4, 12, 4, 19],
        [4, 4, 2, 10, 3, 14],
        [2, 2, 2, 15, 2, 7],
        [4, 4, 3, 10, 2, 14],
        [2, 3, 2, 17, 3, 19],
        [4, 3, 2, 13, 2, 10],
        [4, 3, 4, 18, 3, 13],
        [3, 3, 2, 13, 3, 12],
        [3, 4, 3, 10, 2, 7],
        [2, 2, 2, 20, 2, 14],
        [4, 3, 3, 20, 2, 19],
        [2, 4, 3, 17, 4, 20],
        [4, 4, 2, 15, 3, 16],
        [2, 4, 4, 18, 2, 11],
        [4, 4, 3, 14, 4, 8],
        [2, 4, 4, 11, 3, 8],
        [4, 4, 3, 7, 4, 20],
        [3, 4, 3, 19, 3, 8],
        [2, 3, 2, 16, 2, 9],
        [4, 3, 4, 8, 3, 7],
        [2, 3, 3, 13, 2, 20],
        [3, 4, 3, 6, 2, 10],
        [4, 4, 4, 10, 2, 7],
        [4, 3, 4, 8, 2, 8],
        [3, 3, 3, 11, 2, 8],
        [4, 4, 4, 8, 4, 14],
        [4, 3, 2, 19, 3, 13],
        [2, 4, 4, 20, 3, 14],
        [3, 4, 2, 15, 2, 13],
    ];

    let mut sum = 0;

    for bp in load_blueprints(input) {
        let most = most_geodes(bp, 24);
        println!("blueprint {}: {}", bp.index, most);
        sum += most * bp.index;
    }

    println!("Sum: {}", sum); // 1675

    let input = vec![
        [4, 4, 2, 11, 2, 7],
        [4, 4, 4, 12, 4, 19],
        [4, 4, 2, 10, 3, 14],
    ];

    let mut prod = 1;

    for bp in load_blueprints(input) {
        let most = most_geodes(bp, 32);
        println!("blueprint {}: {}", bp.index, most);
        prod *= most;
    }

    println!("Product: {}", prod); // 6840
}
