
import pytest
from models.fibonacci import Fibonacci

def test_return_with_zero():
    """When given a non-int, raises a ValueError"""
    my_number = Fibonacci()
#     my_number.fibonacci_number("hi")
    with pytest.raises(ValueError):
        my_number.fibonacci_number("HI")
