import os
import functools


def read_file(path):
    file = open(path, "r")
    lines = file.read().split("\n")
    file.close()
    return lines


def convert_to_i(values):
    return list(map(int, values))


def sum(values):
    return functools.reduce(lambda x, y: x + y, values)


def calculate_frequency(path):
    values_s = read_file(path)
    values_i = convert_to_i(values_s)
    return sum(values_i)


def find_repeated(increments):
    frequency = 0
    found_frequencies = {0}

    while True :
      for increment in increments:
          frequency += increment

          if frequency in found_frequencies:
              return frequency

          found_frequencies.add(frequency)


def find_frequency(path):
    values_s = read_file(path)
    values_i = convert_to_i(values_s)
    return find_repeated(values_i)


print(find_frequency('input.txt'))
