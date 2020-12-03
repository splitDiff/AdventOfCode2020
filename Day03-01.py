#%%
# get data
from numpy import prod

data = open('Day03-Input.txt').readlines()
data = [d.strip() for d in data]

terrain = [list(r) for r in data]

#%%
# Functions
def make_run(terrain, position, slope):
    tree = 0
    while position[1] <= len(terrain) - 1:
        if terrain[position[1]][position[0]] == '#':
            tree += 1 
        position[0] = (position[0] + slope[0]) % len(terrain[0])
        position[1] = position[1] + slope[1]
    return tree

#%%
# Part 1

slope = [3, 1]
start =[0,0]

tree = make_run(terrain, start, slope)

print(f"Part 1: {tree} trees")
#%%
# Part 2

slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
        ]

tree_hits = []

for slope in slopes:
    start =[0,0]
    position = start
    tree = make_run(terrain, start, slope)
    # print(f"Slope: {slope}, trees:{tree}")
    tree_hits.append(tree)

print(f"Part 2: {prod(tree_hits)} trees")

# %%
