from lib.check_codeword import *

def test_add_horse_returns_ok():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_add_banjo_returns_wrong():
    result = check_codeword("banjo")
    assert result == "WRONG!"