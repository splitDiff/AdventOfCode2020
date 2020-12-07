
#%%
# get data
import re

data_file = 'Day04-Input.txt'

data = open(data_file, 'r').read()

passports = data.split('\n\n')

passports = [re.sub(r'\n', ' ', p) for p in passports]

required_fields = {
        'byr'
        ,'iyr'
        , 'eyr'
        , 'hgt'
        , 'hcl'
        , 'ecl'
        , 'pid'
        }

# %%
# Part 1: Valid passports

valid_passports = [True for p in passports]

for seq, passport in enumerate(passports):
    field_blocks = passport.strip().split(' ')
    fields = {}
    for block in field_blocks:
        key, value = block.split(':')
        fields[key] = value

    for field_name in required_fields:
        if field_name not in fields.keys():
            valid_passports[seq] = False

print(f"Part 1: valid passports: {sum(valid_passports)}")
    
# %%
# Validity functions

def valid_byr(value):
    return 1920 <= int(value) <= 2002

def valid_iyr(value):
    return 2010 <= int(value) <= 2020

def valid_eyr(value):
    return 2020 <= int(value) <= 2030

def valid_hgt(value):
    if not re.fullmatch(r'\d*(cm|in)', value):
        return False
    hgt, units = re.match(r'(\d*)((cm|in))', value).group(1,2)
    if units == 'cm':
        return 150 <= int(hgt) <= 193
    else:
        return 59 <= int(hgt) <= 76

def valid_hcl(value):
    return bool(re.fullmatch(r'#[0-9a-f]{6}', value))

def valid_ecl(value):
    return value in 'amb blu brn gry grn hzl oth'.split(' ')

def valid_pid(value):
    return bool(re.fullmatch(r'\d{9}',value))

def valid_cid(value):
    return True

validity_functions = {
    'byr': valid_byr,
    'iyr': valid_iyr,
    'eyr': valid_eyr,
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': valid_pid,
    'cid': valid_cid
}

# %%
#Part 2 - data validation

valid_passports = [True for p in passports]

for seq, passport in enumerate(passports):
    field_blocks = passport.strip().split(' ')
    fields = {}
    for block in field_blocks:
        key, value = block.split(':')
        fields[key] = value

    for field_name in required_fields:
        if field_name not in fields.keys():
            valid_passports[seq] = False

    for key in fields.keys():
        if not validity_functions[key](fields[key]):
            valid_passports[seq] = False


print(f"Part 2: valid passports: {sum(valid_passports)}")
    
# %%
