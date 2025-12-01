
from lib.greet import *

def test_add_jonesy_returns_hello_jonesy():
    result = greet("Jonesy")
    assert result == "Hello, Jonesy!"

