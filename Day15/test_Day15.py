import Day15

def test_part1_1():
    assert Day15.part1([0,3,6]) == 436

def test_part1_2():
    assert Day15.part1([1,3,2]) == 1

def test_part1_3():
    assert Day15.part1([2,1,3]) == 10

def test_part1_4():
    assert Day15.part1([1,2,3]) == 27

def test_part1_5():
    assert Day15.part1([2,3,1]) == 78

def test_part1_6():
    assert Day15.part1([3, 2, 1]) == 438

def test_part1_7():
    assert Day15.part1([3,1,2]) == 1836


def test_part2_2():
    assert Day15.part2([1,3,2], 2020) == 1
def test_part2_3():
    assert Day15.part2([2,1,3], 2020) == 10
def test_part2_4():
    assert Day15.part2([1,2,3], 30_000_000) == 261214
def test_part2_5():
    assert Day15.part2([3,2,1], 30_000_000) == 18
def test_part2_6():
    assert Day15.part2([3,1,2], 30_000_000) == 362