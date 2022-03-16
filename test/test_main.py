"""
Contains tests for main
"""
from src.main import say_hi


def test_say_hi():
    """
    Tests that the correct person is greeted in the expected manner
    :return: -
    """
    name = 'Test Name'
    assert say_hi(name) == f'Hi, {name}'
