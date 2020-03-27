def prime_numbers(limit):
    prime_numbers_list = []
    for x in range(1, limit):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime_numbers_list.append(x)
    return prime_numbers_list


def read_from_keyboard(primes):
    value = int(input('Provide prime number:'))
    for prime in primes:
        if value == prime:
            return value
    else:
        raise Exception


def man_in_the_middle(prime, base, value=None):
    for i in range(1, 10):
        if value ** (1 / i) == base:
            return i