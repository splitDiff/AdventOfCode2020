#%%
# Get data

if 0:
    data_file = './Day14/Day14-Input.txt'
else:
    data_file = './Day14/Day14-TestInput.txt'

data = open(data_file, 'r').read()

#%%

program = data.split('\n')

memory = [0b0 for b in range(36)]
mask = 'X' * 36

for line in program:
    if line[0:4] == 'mask':
        mask = line[6:]
        print(mask)

         

print(memory)
# %%
