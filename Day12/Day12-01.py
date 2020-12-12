#%%
# Get data
import dataclasses
import math

if 1:
    data_file = './Day12/Day12-Input.txt'
else:
    data_file = './Day12/Day12-TestInput.txt'

data = open(data_file, 'r').read()

#%%
# Data structures

@dataclasses.dataclass
class Step():
    action:str
    count:int

@dataclasses.dataclass
class State():
    direction:int
    x:int
    y:int
    w_x: int = 10
    w_y: int = 1

#%%
# Simple actions

def forward(state, count):
    state.x += round(math.cos(math.radians(state.direction))) * count
    state.y += round(math.sin(math.radians(state.direction))) * count
    return state

def north(state, count):
    state.y += count
    return state

def south(state, count):
    return north(state, -count)

def east(state, count):
    state.x += count
    return state

def west(state, count):
    return east(state, -count)

def right(state, count):
    state.direction = (state.direction - count) % 360

    return state

def left(state, count):
    state.direction = (state.direction + count) % 360
    return state

actions = {
    'N': north,
    'S': south,
    'E': east,
    'W':west,
    'F':forward,
    'L': left,
    'R': right
    }

#%%%
# Part 1 - Simple trip

lines = data.split('\n')
steps = [Step(s[0], int(s[1:])) for s in lines]

state = State(0, 0, 0)

for step in steps:
    state = actions[step.action](state, step.count)

print(f"Part 1 - Manhattan distance: {abs(state.x) + abs(state.y)}")


# %%
# Waypoint actions

def forward(state, count):
    state.x += state.w_x * count
    state.y += state.w_y * count
    return state

def north(state, count):
    state.w_y += count
    return state

def south(state, count):
    return north(state, -count)

def east(state, count):
    state.w_x += count
    return state

def west(state, count):
    return east(state, -count)

def right(state, count):
    r = math.sqrt(state.w_x ** 2 + state.w_y ** 2)
    t = math.atan2(state.w_y, state.w_x)
    t = (t - math.radians(count)) 
    state.w_x = round(r * math.cos(t))
    state.w_y = round(r * math.sin(t))
    return state

def left(state, count):
    right(state,-count)
    return state

actions = {
    'N': north,
    'S': south,
    'E': east,
    'W':west,
    'F':forward,
    'L': left,
    'R': right
    }



# %%
# Part 2 - Waypoint trip

state = State(0, 0, 0, 10, 1)

for step in steps:
    state = actions[step.action](state, step.count)

print(f"Part 2 - Manhattan distance: {abs(state.x) + abs(state.y)}")
# %%
