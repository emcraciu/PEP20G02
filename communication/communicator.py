from random import randint


class Communicator():

    def __init__(self, prime, base):
        self.__secret = randint(1, 10)
        self.__shared_secret = None
        self.prime = prime
        self.base = base
        self.local_distribute = self.calculate_distribute(base)
        self.remote_distribute = None

    def value_modifier(self, value):
        self.value = value

    def calculate_distribute(self, base):
        return base ** self.__secret % self.prime

    def calculate_response_distribute(self):
        if self.remote_distribute:
            self.__shared_secret = self.calculate_distribute(self.remote_distribute)
        else:
            raise ValueError('Missing shared secret')
