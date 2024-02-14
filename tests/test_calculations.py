'''My Calculator Test with the functions from operations.py'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that the addition function works.'''
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that the subtraction function works.'''
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that the multiplication function works.'''
    assert multiply(3, 4) == 12

def test_division():
    '''Test that the division function works.'''
    assert divide(18, 6) == 3
