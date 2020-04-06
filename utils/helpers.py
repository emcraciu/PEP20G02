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


class PrimesIter():

    def __init__(self, primes_list: list):
        self.primes_list = primes_list

    def __next__(self):
        if len(self.primes_list) == 0:
            raise StopIteration
        return self.primes_list.pop(0)

    def __iter__(self):
        return self

class Primes():

    def __init__(self):
        self.primes = []
        for x in range(1, 10000):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                self.primes.append(x)

    def __iter__(self):
        return PrimesIter(self.primes)
