
import pytest

from lib.present import * 

#exception should be raised when contents inside the object have already been passed under the wrap function, output should show exception "Contents has already been wrapped."

def test_item_already_wrapped_e():
    present1 = Present()
    with pytest.raises(Exception) as e:
        present1.wrap("ball")
        present1.wrap("headphones")
    error_message = str(e.value)
    assert error_message == "Contents has already been wrapped."

#exception should be raised when there are no contents inside the object to unwrap, output should show exception "No contents have been wrapped."

def test_no_wrapped_items_e():
    present2 = Present()
    with pytest.raises(Exception) as e:
        present2.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


def test_wrapping_item():
    present3 = Present()
    result = present3.wrap("bike")
    result == "bike"


def test_unwrapping_item():
    present4 = Present()
    present4.wrap("bike")
    result = present4.unwrap()
    result == "bike"

#initial state: return None when no contents are provided

def test_no_items():
    present5 = Present()
    result = present5.contents
    result == None


