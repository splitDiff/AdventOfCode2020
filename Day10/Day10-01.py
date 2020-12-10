#%%
# Get data
from functools import lru_cache

if 1:
    data_file = './Day10/Day10-Input.txt'
else:
    data_file = './Day10/Day10-TestInput.txt'

data = open(data_file, 'r').read()

#%%
adapters = list(map(int, data.split('\n')))
max_voltage = max(adapters) + 3

adapters = sorted([*adapters, 0, max_voltage])

print(adapters)

#%%
# Part 1 - Calculate differences

differences = {1:0, 2: 0, 3:0}

for a in range(len(adapters)-1):
    diff = adapters[a+1] - adapters[a]
    differences[diff] += 1

print(f"Difference counts: {differences}")
print(f"Part 1 - {differences[1] * differences[3]}")
#%%
# Valid Connections function

@lru_cache(maxsize=100)
def valid_connections(jolts):
    vc = []
    for j in range(1,4):
        if (jolts + j) in adapters:
            vc.append(jolts + j)
    return vc

#%%
# Part 2 - Build Adapter function

@lru_cache(maxsize=200)
def build_adapter(jolts):
    combinations = 0
    if jolts == max_voltage:
        return 1  
    for n in valid_connections(jolts):
        combinations += build_adapter(n)
    return combinations 

print(f"Part 2 - combinations: {build_adapter(adapters[0])}")
#%%