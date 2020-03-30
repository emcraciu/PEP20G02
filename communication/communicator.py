from random import randint


class Communicator():
    value = None

    def __init__(self, prime, base):
        self.__secret = randint(1, 10)
        self.__shared_secret = None
        self.prime = prime
        self.base = base
        self.distribute = self.calculate_distribute(base)

    def value_modifier(self, value):
        self.value = value

    def calculate_distribute(self, base):
        return base ** self.__secret % self.prime

    def calculate_send_distribute(self):
        if self.base:
            return self.calculate_distribute(self.base)
        else:
            raise ValueError('self.base is {}'.format(self.base))

    def calculate_response_distribute(self):
        if self.value:
            self.__shared_secret = self.calculate_distribute(self.value)
            return self.__shared_secret
        else:
            raise ValueError('self.value is {}'.format(self.value))
