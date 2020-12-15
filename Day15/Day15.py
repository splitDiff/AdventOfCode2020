def part1(seq):
    for step in range(len(seq), 2021):
        if seq[-1] in seq[0:-1]:
            position = 1 + seq[-2::-1].index(seq[-1])
            seq.append(position)
        else:
            seq.append(0)
    return seq[2020 - 1]


print(f"Part 1 - {part1([16,12,1,0,15,7,11])}")

def part2(seq, max):
    last_position = {}
    for i, s in enumerate(seq[0:-1]):
        last_position[s] = i

    target = seq[-1]

    for step in range(len(seq) - 1, max - 1):
        if target in last_position.keys():
            lp = last_position[target]
            last_position[target] = step
            target = step - lp
        else:
            last_position[target] = step
            target = 0

    return target

if __name__ == "__main__":
    import time
    print(f"Part 1 with part 2 code - {part2([16,12,1,0,15,7,11], 2020)}")
    t0 = time.time()
    print(f"Part 2 - {part2([16,12,1,0,15,7,11], 30_000_000)}")
    print(f"Time elapsed: {time.time() - t0}")

