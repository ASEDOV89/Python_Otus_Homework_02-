"""
Домашнее задание №1
Функции и структуры данных
"""

# from typing import List, Any

def power_numbers(numbers):
    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """
    results = []
    for num in numbers:
        if isinstance(num, list):
            results.extend(power_numbers(num * +2))
        else:
            results.append(num ** 2)
    return results

numbers = [1, 2, 5, 7]

print(power_numbers(numbers))

import math

# filter types
ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))

num_odd = [1, 2, 3]
num_even = [2, 3, 4, 5]
num_prime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(filter_numbers(num_odd, ODD))
print(filter_numbers(num_even, EVEN))
print(filter_numbers(num_prime, PRIME))
