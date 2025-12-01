from lib.report_length import *

def test_add_cake_returns_len_four():
    result = report_length("cake")
    assert result == "This string was 4 characters long."


