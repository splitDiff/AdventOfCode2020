#%%
# Get data
import copy
import dataclasses

if 1:
    data_file = './Day11/Day11-Input.txt'
else:
    data_file = './Day11/Day11-TestInput.txt'

data = open(data_file, 'r').read()

#%%

grid = []

for row in data.split('\n'):
    grid.append(list(row))

def print_grid(grid):
    for row in grid:
        print(''.join(row))

max_y = len(grid)
max_x = len(grid[0])

#%%
# Part 1 - Set seat status function

def new_seat_status(grid, x, y):
    if grid[y][x] == '.':
        return '.'
    occupied_seats = 0
    for j in range(max(0, y-1), min(y+2, max_y)):
        for i in range(max(0, x-1), min(x+2, max_x)):
            if grid[j][i] == '#' and not(i == x and j == y):
                occupied_seats += 1
    if grid[y][x] == 'L' and occupied_seats == 0:
        return '#'
    if grid[y][x] == '#' and occupied_seats >= 4:
        return 'L'
    return grid[y][x]
#%%
# End state functions

def same_grid(grid_1, grid_2):
    for j in range(max_y):
        for i in range(max_x):
            if grid_1[j][i] != grid_2[j][i]:
                return False
    return True

def count_filled(grid):
    filled_seats = 0
    for j in range(max_y):
        for i in range(max_x):
            if grid[j][i] == '#':
                filled_seats += 1
    return filled_seats
#%%
# Part 1 run

new_grid = copy.deepcopy(grid)
current_grid = copy.deepcopy(grid)

for t in range(100):
    for j in range(max_y):
        for i in range(max_x):
            new_grid[j][i] = new_seat_status(current_grid, i, j)
    if same_grid(new_grid, grid):
        break
    current_grid = copy.deepcopy(new_grid)

print(f"Part 1 - filled seats: {count_filled(new_grid)}")

#%%
# Part 2 - Set seat status function

@dataclasses.dataclass
class Direction():
    steps:int
    x_step:int
    y_step:int

def new_seat_status_part_2(grid, x, y):
    if grid[y][x] == '.':
        return '.'
    occupied_seats = 0

    directions = {
        'left' : Direction(x, -1, 0), 
        'right': Direction(max_x - x - 1, 1, 0), 
        'up'   : Direction(y, 0, -1), 
        'down' : Direction(max_y - y - 1, 0, 1), 
        'ul'   : Direction(min(x, y), -1, -1), 
        'ur'   : Direction(min(max_x - x - 1, y), 1, -1), 
        'dl'   : Direction(min(x, max_y - y - 1), -1, 1), 
        'dr'   : Direction(min(max_x - x - 1, max_y - y -1), 1, 1) 
    }

    for d in directions.values():
        i, j = x, y
        for k in range(0, d.steps):
            i += d.x_step
            j += d.y_step
            if grid[j][i] == '#':
                occupied_seats += 1
                break
            if grid[j][i] == 'L':
                break

    if grid[y][x] == 'L' and occupied_seats == 0:
        return '#'
    if grid[y][x] == '#' and occupied_seats >= 5:
        return 'L'
    return grid[y][x]

# %%
# Part 2 run

new_grid = copy.deepcopy(grid)
current_grid = copy.deepcopy(grid)

for t in range(100):
    for j in range(max_y):
        for i in range(max_x):
            new_grid[j][i] = new_seat_status_part_2(current_grid, i, j)
    if same_grid(new_grid, current_grid):
        break
    current_grid = copy.deepcopy(new_grid)

print(f"Part 2 - filled seats: {count_filled(new_grid)}")
#%%