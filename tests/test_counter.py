from lib.counter import *

def test_counter_response_five():
    counter1 = Counter()
    counter1.add(5)
    result = counter1.report()
    assert result == "Counter to 5 so far."