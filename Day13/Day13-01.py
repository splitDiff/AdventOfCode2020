#%%
# Get data
import math
import sys

if 1:
    data_file = './Day13/Day13-Input.txt'
else:
    data_file = './Day13/Day13-TestInput.txt'

data = open(data_file, 'r').read()

#%%
# Part 1 - best schedule

departure_time, schedules = data.split('\n')
departure_time = int(departure_time)
schedules = [int(s) if s != 'x' else s for s in schedules.split(',')]

best_schedule = ('', sys.maxsize )

for schedule in schedules:
    if schedule == 'x':
        continue
    wait_time = schedule - (departure_time % schedule) 
    if (wait_time < best_schedule[1]):
        best_schedule = schedule, wait_time

print(f"Part 1 - best schedule {best_schedule[0] * best_schedule[1]}")

# %%
# Part 2 - staggered departures

def status():
    for i in deltas:
        print(f"{i} - {test_time % i[1]}")

deltas = []

for i, s in enumerate(schedules):
    if s == 'x':
        continue
    if i == 0:
        deltas.append((i, s, i))
        continue
    deltas.append((i, s, s - (i % s)))

deltas = sorted(deltas, key = lambda x: x[1], reverse = True)

test_time = 0

prod = 1
test_time = deltas[0][2]


for i, dlt in enumerate(deltas[0:-1]):
    prod *= dlt[1]
    while test_time % deltas[i+1][1] != deltas[i+1][2]:
        test_time = test_time + prod 

print(f"Part 2 - Timestamp - {test_time}")

# %%
