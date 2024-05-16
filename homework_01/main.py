def power_numbers(numbers):
    results = []
    for num in numbers:
        if isinstance(num, list):
            results.extend(power_numbers(num * +2))
        else:
            results.append(num ** 2)
    return results

# filter types
ODD: str = 'odd'
EVEN: str = 'even'
PRIME: str = 'prime'

def is_prime(num):
    import math
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filter_numbers(num, filter_type):
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, num))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, num))
    elif filter_type == PRIME:
        return list(filter(is_prime, num))

if __name__ == "__main__":
    numbers: list[int] = [1, 2, 5, 7]
    num_odd = [1, 2, 3, 4]
    num_even = [1, 2, 3, 4, 5]
    num_prime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]