#%%
# Get data
from dataclasses import dataclass, field

data_file = './Day08/Day08-Input.txt'

data = open(data_file, 'r').read()

#%%
# Processor
@dataclass
class Processor:
    next_operation: int = 0
    accumulator: int = 0
    past_operations: list = field(default_factory = list)
    jump_out: bool = False

def jmp(value, processor):
    processor.next_operation += int(value)
    return processor

def nop(value, processor):
    processor.next_operation += 1
    return processor

def acc(value, processor):
    processor.accumulator += int(value)
    processor.next_operation += 1
    return processor

operations = {
    'jmp': jmp,
    'nop': nop,
    'acc': acc
}


#%%
# Run program
program = data.split('\n')
processor = Processor()

def run(program, processor):
    max_instruction = len(program) - 1
    while processor.next_operation not in processor.past_operations:
        processor.past_operations.append(processor.next_operation)
        operation, value = program[processor.next_operation].split(' ')
        processor = operations[operation](value, processor)

        if processor.next_operation > max_instruction:
            processor.jump_out = True
            break
    return processor

# %%
# Part 1 - Infinte Loop

processor = run(program, processor)
print(f"Part 1 - acc value: {processor.accumulator}")

# %%
# Part 2 - Flip an operation

all_nops_jmps = [i for i,p in enumerate(program) if p[0:3] == 'nop' or p[0:3] == 'jmp']

for n in all_nops_jmps:
    n_program = program[:]
    if n_program[0:3] == 'nop':
        n_program[n] = n_program[n].replace('nop', 'jmp')
    else:
        n_program[n] = n_program[n].replace('jmp', 'nop')
    n_processor = Processor()
    run(n_program, n_processor)
    if n_processor.jump_out:
        print(f"Part 2 - change to a {n_program[n][0:3]} at {n}")
        print(f"Part 2 - Accumulator = {n_processor.accumulator}")
        break

#%%
