#%%
# Get data
import re

day = '14'

data_file = {
    0: f'./Day{day}/Day{day}-Input.txt',
    1: f'./Day{day}/Day{day}-TestInput.txt',
    2: f'./Day{day}/Day{day}-TestInput2.txt',
    }

data = open(data_file[2], 'r').read()

#%%

program = data.split('\n')

memory = {}
mask = 'X' * 36

for line in program:
    if line[0:4] == 'mask':
        mask = line[7:]

    if line[0:3] == 'mem':
        address, value = re.match(r"mem\[(\d*)\] = (\d*)", line).groups()
        value = list(f"{int(value):>036b}")

        for i, bit in enumerate(mask):
            if bit != 'X':
                value[i] = bit

        value = int('0b' + ''.join(value), 2)

        memory[address] = value


accumulator = 0
for value in memory.values():
    accumulator += value

print(f"Part 1 - accumulator: {accumulator}")

# %%

memory = {}
mask = 'X' * 36

for line in program:
    if line[0:4] == 'mask':
        mask = line[7:]

    if line[0:3] == 'mem':
        floating_addresses = []
        address, value = re.match(r"mem\[(\d*)\] = (\d*)", line).groups()
        address = list(f"{int(address):>036b}")

        for i, bit in enumerate(mask):
            if bit != '0':
                address[i] = bit
        
        floating_addresses = [address[:]]
        
        for i, bit in enumerate(address):
            if bit == 'X':
                fa = []
                for a in floating_addresses:
                    fa.append(a[0:i] + ['0'] + a[i+1:])
                    fa.append(a[0:i] + ['1'] + a[i+1:])
                floating_addresses = fa

        for a in floating_addresses:
            address = int('0b' + ''.join(a), 2)
            memory[address] = value


accumulator = 0
for value in memory.values():
    accumulator += value

print(f"Part 1 - accumulator: {accumulator}")
