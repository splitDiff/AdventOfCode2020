#%%

data_file = 'Day06-Input.txt'

data = open(data_file, 'r').read()

#%%

groups = data.split('\n\n')

counts = []

for group in groups:
    group = set(group.replace('\n',''))
    counts.append(len(group))

print(f"Part 1: {sum(counts)}")

#%%

counts = []

for group in groups:
    yeses = set([chr(x) for x in range(97,123)])
    for person in group.split('\n'):
        yeses = yeses & set(list(person))
    counts.append(len(yeses))

print(f"Part 2: {sum(counts)}")

#%%
    