import Day16

def test_parse_rules():
    assert Day16.parse_rules("class: 1-3 or 5-7") == {'class': [[1,3], [5,7]]}
    assert Day16.parse_rules("class: 1-3 or 5-7\nrow: 6-11 or 33-44") == {'class': [[1,3], [5,7]], 'row': [[6,11],[33,44]]}

def test_parse_tickets():
    assert(Day16.parse_tickets("nearby tickets:\n7,3,47\n40,4,50")) == [[7,3,47], [40,4,50]]

def test_parse_ticket():
    assert(Day16.parse_ticket("7,3,47")) == [7,3,47]



