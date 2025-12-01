from lib.string_builder import *

def test_string_hello():
    hellostr = StringBuilder()
    hellostr.add("hello")
    hellostr.size()
    result = hellostr.output()
    assert result == "hello"

def test_string_length_karen():
    hellostr = StringBuilder()
    hellostr.add("Karen")
    hellostr.size()
    result = hellostr.size()
    assert result == 5

def test_string_builds_two_words():
    hellostr = StringBuilder()
    hellostr.add("Hello")
    hellostr.add("Karen")
    result = hellostr.output()
    assert result == "HelloKaren"

def test_string_length_hellokaren():
    hellostr = StringBuilder()
    hellostr.add("Hello")
    hellostr.add("Karen")
    hellostr.size()
    result = hellostr.size()
    assert result == 10