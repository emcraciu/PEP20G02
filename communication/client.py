from random import randint


class Client():
    value = None

    def __init__(self, prime, base):
        self.client_rand = randint(1, 10)
        self.prime = prime
        self.base = base
        self.distribute = self.calculate_distribute(base)

    def value_modifier(self, value):
        self.value = value

    def calculate_distribute(self, base):
        return base ** self.client_rand % self.prime

    def calculate_send_distribute(self):
        if self.base:
            return self.calculate_distribute(self.base)
        else:
            raise ValueError('self.base is {}'.format(self.base))

    def calculate_response_distribute(self):
        if self.value:
            return self.calculate_distribute(self.value)
        else:
            raise ValueError('self.value is {}'.format(self.value))
