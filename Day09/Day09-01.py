#%%
# Get data

if 1:
    preamble = 25
    data_file = './Day09/Day09-Input.txt'
else:
    preamble = 5
    data_file = './Day09/Day09-TestInput.txt'

data = open(data_file, 'r').read()

#%%
raw = data.split('\n')

block = []

raw = [int(r) for r in raw]

for i in range(preamble):
    block.append(raw[i])

test_value = -1

for x in range(preamble, len(raw)):
    test_value = raw[x]
    found = False
    for y in range(len(block)):
        for z in range(y + 1, len(block)):
            b1, b2 = block[y], block[z]
            if test_value == b1 + b2:
                found = True
                break
        if found:
            break
    if found:
        del(block[0])
        block.append(test_value)
    else:
        print(f"Part 1 - {test_value} fails")
        break
#%%

failing_number = test_value

print(f"Looking for: {failing_number}")

for x in range(len(raw)):
    found = False
    y = 0
    while sum(raw[x:x+y]) < failing_number:
        y+=1
        # print(f"sum({x}:{x+y}) = {sum(raw[x:x+y])}")
    if sum(raw[x:x+y]) == failing_number:
        print(', '.join(map(str,raw[x:x+y])))
        min_in_list, max_in_list = min(raw[x:x+y]), max(raw[x:x+y])
        print(f"Part 2 - sum {min_in_list + max_in_list}")
        break

#%%
    