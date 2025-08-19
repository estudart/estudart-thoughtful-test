import pytest

from thoughtful_test import is_bulky, is_heavy, sort

def test_high_volume_return_true_bulky():
    volume = 10000000
    dimensions = []
    assert is_bulky(volume, dimensions)

def test_high_dimension_return_true_bulky():
    volume = 100
    dimensions = [200]
    assert is_bulky(volume, dimensions)

def test_low_volume_return_false_bulky():
    volume = 1000
    dimensions = []
    assert not is_bulky(volume, dimensions)

def test_low_dimension_return_false_bulky():
    volume = 100
    dimensions = [20]
    assert not is_bulky(volume, dimensions)

def test_high_mass_return_true_heavy():
    mass = 100
    assert is_heavy(mass)

def test_low_mass_return_false_heavy():
    mass = 10
    assert not is_heavy(mass)

def test_negative_value_raises_exception():
    with pytest.raises(ValueError):
        sort(width=10, height=-1, lenght=5, mass=30)