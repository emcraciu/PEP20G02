from communication.communicator import Communicator


class Client(Communicator):

    def __init__(self, prime, base):
        super().__init__(prime, base)
