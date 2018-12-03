import pytest
import checksum


def test_detects_2_repeated_letters():
    assert checksum.has_repeated_letters('abcda', 2)


def test_detects_3_repeated_letters():
    assert checksum.has_repeated_letters('abcdaba', 3)


def test_detects_no_repeated_letters():
    assert checksum.has_repeated_letters('qwerty', 2) == False