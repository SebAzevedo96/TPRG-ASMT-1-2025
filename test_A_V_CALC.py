'''
TPRG 2131 ASMT 1
Sebastian Azevedo
Fall 2025

test_A_V_CALC.py is the pytest script ascociated with A_V_CALC.py.'''



import pytest
import math

# needed to process the input() function.
from unittest.mock import Mock

#bring in the script
import A_V_CALC 


#Tests for Pure Calculation Functions 

def test_area_rectangle():
    #Tests the area calculation for a rectangle
    assert A_V_CALC.area_rectangle(10, 5) == 50
    assert A_V_CALC.area_rectangle(0.5, 4) == 2.0
    assert A_V_CALC.area_rectangle(0, 5) == 0

def test_area_circle():
    #Tests the area calculation for a circle (pi * r^2).
    assert A_V_CALC.area_circle(1) == pytest.approx(math.pi)
    assert A_V_CALC.area_circle(2) == pytest.approx(4*math.pi)

def test_area_triangle():
    #Tests the area calculation for a triangle (0.5 * b * h).
    assert A_V_CALC.area_triangle(10, 5) == 25.0
    assert A_V_CALC.area_triangle(4, 2.5) == 5.0
    assert A_V_CALC.area_triangle(1, 1) == 0.5


def test_volume_cube():
    #Tests the volume calculation for a cube (s^3).
    assert A_V_CALC.volume_cube(3) == 27
    assert A_V_CALC.volume_cube(10) == 1000
    assert A_V_CALC.volume_cube(0.5) == 0.125


#  Tests for Interactive Function (Requires Mocking)
# all below was written by A.I. 

def test_get_positive_value_valid_first_try(monkeypatch):
    """Tests when a valid positive number is entered immediately."""
    # Use monkeypatch to simulate user entering '5.0'
    monkeypatch.setattr('builtins.input', lambda x: '5.0')
    assert A_V_CALC.get_positive_value("What is the value?") == 5.0

def test_get_positive_value_invalid_then_valid(monkeypatch):
    """
    Tests the retry loop by simulating invalid input (0.0, -1.0) followed 
    by a valid number (10.0).
    """
    # Configure mock to return a sequence of inputs
    mock_input = Mock(side_effect=['0.0', '-1.0', '10.0'])
    monkeypatch.setattr('builtins.input', mock_input)

    # Function should prompt three times and return 10.0
    result = A_V_CALC.get_positive_value("Prompt")
    
    assert result == 10.0
    assert mock_input.call_count == 3
    
def test_get_positive_value_non_numeric_input(monkeypatch):
    """Tests that a non-numeric string input raises a ValueError."""
    # Simulate user entering 'text'
    monkeypatch.setattr('builtins.input', lambda x: 'text')
    
    # Expect a ValueError to be raised by the function's internal error handling
    with pytest.raises(ValueError, match="Invalid input: value must be numeric."):
        A_V_CALC.get_positive_value("Prompt")
