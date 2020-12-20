#%%
# Get data
import re

def get_data(day, input):
    data_file = {
        0: f'./Day{day}/Day{day}-Input.txt',
        1: f'./Day{day}/Day{day}-TestInput.txt',
        2: f'./Day{day}/Day{day}-TestInput2.txt',
        }

    return open(data_file[input], 'r').read()

#%%

def parse_rules(rules_text):
    rules_dict = {}
    rules = rules_text.split('\n')
    for rule in rules_text.split('\n'):
        name, ranges = rule.split(': ')
        for range in ranges.split(' or '):
            rules_dict.setdefault(name, []).append(list(map(int, range.split('-'))))
    return rules_dict


def parse_tickets(ticket_text):
    ticket_list = []
    for ticket in ticket_text.split('\n'):
        if ticket != 'nearby tickets:':
            ticket_list.append(parse_ticket(ticket))
    return ticket_list

def parse_ticket(ticket):
    return [int(t.strip()) for t in ticket.split(',')]

def check_ticket(rules, ticket):
    invalid_values = []
    for value in ticket:
        valid = False
        for cls in rules.values():
            for range in cls:
                if range[0] <= value <= range[1]:
                    valid = True
                if valid:
                    break
            if valid:
                break
        if not(valid):
           invalid_values.append(value)
    return invalid_values

def check_rule(rule, value):
    valid = False
    for range in rule:
        if range[0] <= value <= range[1]:
            valid = True
    return valid

def part1():
    data = get_data(16,0)

    rules_text, my_ticket, nearby_tickets_text = data.split('\n\n')

    rules = parse_rules(rules_text)
    my_ticket = parse_ticket(my_ticket.split('\n')[1])
    nearby_tickets = parse_tickets(nearby_tickets_text)

    invalid_sum = 0
    for ticket in nearby_tickets:
        invalid_sum += sum(check_ticket(rules, ticket))
    print(f"Invalid Sum: {invalid_sum}")


#%%
part1()

#%%
def part2():
    data = get_data(16,0)

    rules_text, my_ticket, nearby_tickets_text = data.split('\n\n')

    rules = parse_rules(rules_text)
    my_ticket_values = parse_ticket(my_ticket.split('\n')[1])
    nearby_tickets = parse_tickets(nearby_tickets_text)

    valid_tickets = []
    for ticket in nearby_tickets:
        if len(check_ticket(rules, ticket)) == 0:
            valid_tickets.append(ticket)

    # print(f"Valid Tickets: {valid_tickets}")

    cls_columns = {}
    for cls in rules.keys():
        possible_columns = list(range(len(valid_tickets[0])))
        for col in possible_columns[:]:
            for ticket in valid_tickets:
                # print(f"checking {cls}, {rules[cls]}, {ticket[col]}, {col}, {check_rule(rules[cls],ticket[col])}")
                if not(check_rule(rules[cls],ticket[col])):
                    possible_columns.remove(col)
        cls_columns[cls] = possible_columns
    
    for cls in cls_columns.keys():
        for cls in cls_columns.keys():
            # print(f"{cls}: {cls_columns[cls]}")
            if len(cls_columns[cls]) == 1:
                # print(cls_columns[cls][0])
                for c in cls_columns.keys():
                    if c == cls:
                        continue
                    if cls_columns[cls][0] in cls_columns[c]:
                        cls_columns[c].remove(cls_columns[cls][0])
                    # print(f"cls_columns: {c}: {cls_columns[c]}")


    departure_cols = []
    for cls in cls_columns.keys():
        if cls[0:9] == 'departure':
            departure_cols.append(cls_columns[cls][0])
    print(f"final {departure_cols}")

    product = 1
    for c in departure_cols:
        product *= my_ticket_values[c]         
    print(product)

part2()
# %%
