#%%
# get data
import re
data = open('Day02-Input.txt').readlines()
data = [d.strip() for d in data]
#%%
# Part 1
pwd_pass, pwd_fail = 0, 0

for dataline in data:
    matching_expression = r'(\d+)-(\d+) (\w): (\w*)'
    match = re.fullmatch(matching_expression, dataline)
    low, high, letter, pwd = match.groups()

    stripped_pwd = re.sub(f'[^{letter}]','',pwd)

    if int(low) <= len(stripped_pwd) <= int(high):
        pwd_pass += 1
    else:
        pwd_fail += 1

print(f"Part One: {pwd_pass}")
# %%
# Part 2
pwd_pass, pwd_fail = 0, 0

for dataline in data:
    matching_expression = r'(\d+)-(\d+) (\w): (\w*)'
    match = re.fullmatch(matching_expression, dataline)
    pos1, pos2, letter, pwd = match.groups()
    pos1, pos2 = int(pos1) - 1, int(pos2) - 1
    if (pwd[pos1] == letter ) ^ (pwd[pos2] == letter): 
        pwd_pass += 1
    else:
        pwd_fail += 1

print(f"Part Two: {pwd_pass}")
#%%