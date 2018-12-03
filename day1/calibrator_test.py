import pytest
import calibrator


def test_read_file():
    content = calibrator.read_file('input.txt')
    assert len(content) > 0


def test_convert():
    values = ['-1', '0', '1', '546']
    converted_values = calibrator.convert_to_i(values)
    assert all(isinstance(value, int)for value in converted_values)

def test_sum():
    values = [10, 0, -101, 200]
    sum = calibrator.sum(values)
    assert sum == 109

def test_calculate_frequency():
   assert calibrator.calculate_frequency('input.txt') == 513 