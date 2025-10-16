# test_geometry.py

import math
import pytest
from A_V_CALC_2 import (
    area_rectangle,
    area_circle,
    area_triangle,
    volume_sphere,
    volume_cube
)

def test_area_rectangle():
    area, calc = area_rectangle(5, 3)
    assert area == 15
    assert calc == "A * B = 5 * 3"

def test_area_circle():
    r = 2
    area, calc = area_circle(r)
    expected_area = math.pi * r**2
    assert math.isclose(area, expected_area, rel_tol=1e-9)
    assert calc == f"pi * r^2 = {math.pi:.4f} * ({r}^2)"

def test_area_triangle():
    area, calc = area_triangle(4, 6)
    assert area == 12
    assert calc == "0.5 * B * H = 0.5 * 4 * 6"

def test_volume_sphere():
    r = 3
    vol, calc = volume_sphere(r)
    expected_vol = (4/3) * math.pi * r**3
    assert math.isclose(vol, expected_vol, rel_tol=1e-9)
    assert calc == f"(4/3) * pi * r^3 = 1.3333 * {math.pi:.4f} * ({r}^3)"

def test_volume_cube():
    vol, calc = volume_cube(2)
    assert vol == 8
    assert calc == "s^3 = 2^3"
