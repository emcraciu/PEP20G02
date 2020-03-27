from random import randint

server_rand = randint(1, 10)


def server(prime, base, value=None):
    if value is None:
        power = base ** server_rand % prime
    else:
        power = value ** server_rand % prime
    return power
