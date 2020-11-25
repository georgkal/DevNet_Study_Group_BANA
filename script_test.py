# usr/bin/env python3 
import pytest

class Calculator():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum (self):
        return self.a + self.b

    def sub (self):
        return self.a + self.b

    def mul (self):
        return self.a * self.b

# Testing some functions
def test_sum():
    result = Calculator(55,56)
    assert result.sum()==111
    result_wrong = Calculator(7,8)
    assert result_wrong.sum()==111



