from lib.gratitudes import *

#intial output is the string "Be grateful for: " without any gratitudes added
def test_no_thanks():
    no_thanks = Gratitudes()
    result = no_thanks.format()
    assert result == "Be grateful for: "

#one gratitude is added, output is string "Be grateful for: " + the gratitude added

def test_one_thanks():
    one_thanks = Gratitudes()
    one_thanks.add("water")
    result = one_thanks.format()
    assert result == "Be grateful for: water"

#two gratitudes are added, output is string "Be grateful for: " + the two gratitude added, seperated by a ","

def test_two_thanks():
    two_thanks = Gratitudes()
    two_thanks.add("water")
    two_thanks.add("food")
    result = two_thanks.format()
    assert result == "Be grateful for: water, food"