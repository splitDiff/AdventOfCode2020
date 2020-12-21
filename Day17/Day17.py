#%%
# Get data

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def get_data(day, input):
    data_file = {
        0: f'./Day{day}/Day{day}-Input.txt',
        1: f'./Day{day}/Day{day}-TestInput.txt',
        2: f'./Day{day}/Day{day}-TestInput2.txt',
        }

    return open(data_file[input], 'r').read()

#%%

def set_up_space(first_input):
    space = np.array(first_input)
    dim = len(space[0])
    new_space = np.zeros((dim,dim,dim), np.int)
    new_space[1] = space
    return new_space

def expand_space(space):
    dim = max(space.shape)
    new_space = np.zeros((dim + 2, dim + 2, dim + 2), np.int)
    new_space[1:-1, 1:-1, 1:-1] = space
    return new_space
    
def conway_cell(space,position):
    active_count = 0
    current_value = 0
    for z in range(position[2]-1, position[2]+2):
        for y in range(position[1]-1, position[1]+2):
            for x in range(position[0]-1, position[0]+2):
                if (x,y,z) == position:
                    current_value = space[z,y,x]
                    # if current_value:
                    # else:
                    continue
                if space[z,y,x] == 1:
                    active_count += 1
    if current_value == 1:
        if 2<=active_count<=3:
            return 1
        else:
            return 0
    else:
        if active_count == 3:
            return 1
        else:
            return 0

def next_generation(space):
    next_gen = np.zeros(space.shape, np.int)
    dim = space.shape[0]
    for z in range(1,dim - 1):
        for y in range(1,dim - 1):
            for x in range(1, dim - 1):
                next_gen[z, y, x] = conway_cell(space,(x,y,z))
    return next_gen 

def part1():
    data = get_data(17, 0)
    first_input = list(data.replace('#', '1').replace('.','0').split('\n'))
    for i, row in enumerate(first_input):
       first_input[i] = list(map(int,row)) 

    space = set_up_space(first_input)

    space = expand_space(space)
    space = expand_space(space)

    for i in range(6):
        space = next_generation(space)
        space = expand_space(space)
    
    print(f"Part 1 - Non-zero {np.count_nonzero(space)}")


part1()

#%%

def set_up_space_2(first_input):
    space = np.array(first_input)
    dim = max(space.shape)
    new_space = np.zeros((dim,dim,dim,dim), np.int)
    new_space[1,1] = space
    return new_space

def expand_space_2(space):
    dim = max(space.shape)
    new_space = np.zeros((dim + 2, dim + 2, dim + 2, dim + 2), np.int)
    new_space[1:-1, 1:-1, 1:-1, 1:-1] = space
    return new_space
    
def conway_cell_2(space,position):
    active_count = 0
    # print(f"position: {position}, ")
    current_value = 0
    for z in range(position[3]-1, position[3]+2):
        for y in range(position[2]-1, position[2]+2):
            for x in range(position[1]-1, position[1]+2):
                for w in range(position[0]-1, position[0]+2):
                    if (w,x,y,z) == position:
                        current_value = space[z,y,x, w]
                        continue
                    if space[z,y,x,w] == 1:
                        active_count += 1
    if current_value == 1:
        if 2<=active_count<=3:
            return 1
        else:
            return 0
    else:
        if active_count == 3:
            return 1
        else:
            return 0

def next_generation_2(space):
    next_gen = np.zeros(space.shape, np.int)
    dim = space.shape[0]
    for z in range(1,dim - 1):
        for y in range(1,dim - 1):
            for x in range(1, dim - 1):
                for w in range(1, dim - 1):
                    next_gen[z, y, x, w] = conway_cell_2(space,(w,x,y,z))
    return next_gen 

def part2():
    data = get_data(17, 0)
    first_input = list(data.replace('#', '1').replace('.','0').split('\n'))
    for i, row in enumerate(first_input):
       first_input[i] = list(map(int,row)) 

    space = set_up_space_2(first_input)

    space = expand_space_2(space)
    space = expand_space_2(space)

    import time
    tic = time.perf_counter()
    for i in range(6):
        space = next_generation_2(space)
        space = expand_space_2(space)
        print(f"Step {i} - {time.perf_counter() - tic}")

    print(f"Part 2 - Non-zero {np.count_nonzero(space)}")

part2()
# %%
