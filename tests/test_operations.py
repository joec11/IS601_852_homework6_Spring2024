'''My Calculator Test to test operations'''
# pylint: disable=invalid-name"
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

@pytest.fixture
def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    assert Calculation.create(a, b, operation).perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculation(Decimal('10'), Decimal('0'), divide).perform()
