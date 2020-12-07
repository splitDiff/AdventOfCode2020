
#%%
import functools

data_file = 'Day07-Input.txt'

data = open(data_file, 'r').read()

#%%

class Bag():
    def __init__(self, color):
        self.color = color
        self.contains = []
    def add_contains(self, bag):
        return self.contains.append(bag)
    def color(self):
        return self.color



#%%

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

@functools.lru_cache(maxsize=10000)
def count_shinys(c_bag):
    total_shinys = 0
    bag_types = set()
    if c_bag.color == "shiny gold":
        return set(), 1
    for contents in c_bag.contains:
        c_bag_types, c_total_shinys = count_shinys(bag_rules[contents])
        if c_total_shinys > 0:
            bag_types = bag_types.union({c_bag.color})
        total_shinys += c_total_shinys
    return bag_types, total_shinys

total_shinys = 0
bag_types = set()
rule_count = len(bag_rules.keys())

for i, bag in enumerate(bag_rules.keys()):
    print(f"{i} of {rule_count} - {bag}")
    b_bag_types, b_total_shinys = count_shinys(bag_rules[bag])
    bag_types = bag_types.union(b_bag_types)
    total_shinys += b_total_shinys

print(f"Part 1: {len(bag_types)} - {bag_types}")

# %%


