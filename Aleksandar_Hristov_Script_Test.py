import pytest

def aPlusb(a,b):
        c = a + b
        return c

def tests_aPlusb():
    result = aPlusb(4,5)
    assert result == 9
    #result = aPlusb(5,6)
    #assert result == 9