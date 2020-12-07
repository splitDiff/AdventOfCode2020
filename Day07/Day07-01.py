
#%%
# Get data
import functools

data_file = 'Day07-Input.txt'

data = open(data_file, 'r').read()

#%%
# Bag Class
class Bag():
    def __init__(self, color):
        self.color = color
        self.contains = []
    def add_contains(self, bag):
        return self.contains.append(bag)
    def color(self):
        return self.color



#%%
# Parse Bag Rules
bag_rules = {} 

rules = data.split('\n')
for rule in rules:
    bag_name, contains = rule.split(r' contain ')
    bag_color = bag_name.replace(' bags', '')

    bag = Bag(bag_color)

    for content in contains.split(', '):
        content = content.replace('.', '').replace(' bags', '').replace(' bag', '')
        count, color = content.split(' ', 1)
        if count == "no":
            continue
        for c in range(int(count)):
            bag.add_contains(color)
    bag_rules[bag.color] = bag

#%%
# Count Shiny Gold Bags function
@functools.lru_cache(maxsize=200)
def count_shinys(c_bag):
    total_shinys = 0
    bag_types = set()
    bag_count = 0
    if c_bag.color == "shiny gold":
        return set(), 1, 1
    bag_count += 1
    for contents in c_bag.contains:
        c_bag_types, c_total_shinys, c_bag_count = count_shinys(bag_rules[contents])
        if c_total_shinys > 0:
            bag_types = bag_types.union({c_bag.color})
        total_shinys += c_total_shinys
        bag_count += c_bag_count
    return bag_types, total_shinys, bag_count


#%%
# Count number of bag types containing SGBs

total_shinys = 0
bag_types = set()

for i, bag in enumerate(bag_rules.keys()):
    b_bag_types, b_total_shinys, _ = count_shinys(bag_rules[bag])
    bag_types = bag_types.union(b_bag_types)
    total_shinys += b_total_shinys

print(f"Part 1 - bag type count: {len(bag_types)}")

# %%
# How many bags nested in a SGB?
total_bag_count = 0

for i, bag in enumerate(bag_rules['shiny gold'].contains):
    _, _, b_bag_count = count_shinys(bag_rules[bag])
    total_bag_count += b_bag_count

print(f"Part 2 - inside gold bag is {total_bag_count} bags")
# %%
