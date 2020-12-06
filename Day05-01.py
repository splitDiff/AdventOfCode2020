#%%
data_file = 'Day05-Input.txt'

data = open(data_file, 'r').read()

#%%

boarding_passes = data.split('\n')

values = []

for boarding_pass in boarding_passes:
    rows = boarding_pass[0:7]
    seats = boarding_pass[7:10]
    if len(rows) < 7:
        next
    print(rows, "-", seats)
    row = rows.replace('B','1').replace('F','0')
    seat = seats.replace('R','1').replace('L','0')
    row_num = int(row, 2)
    seat_num = int(seat, 2)
    value = row_num * 8 + seat_num
    values.append(value)

print(max(values))

# %%
sorted_values = sorted(values)
for test in range(0, 1024):
    if test-1 in values and test not in values and test+1 in values:
        print(test)
# %%
