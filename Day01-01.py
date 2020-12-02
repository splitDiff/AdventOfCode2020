#%%
data = open('Day01-Input.txt').readlines()

data = [int(d.strip()) for d in data]

#%%
for i, x in enumerate(data):
    for j, y in enumerate(data[i:]):
        if x + y == 2020:
            print(f"two term answer: {x * y}")    
        for k, z in enumerate(data[j:]):
            if x + y + z == 2020:
                print(f"three term answer: {x * y * z}")    

# %%
