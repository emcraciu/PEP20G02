from communication.communicator import Communicator


class Server(Communicator):

    def __init__(self, prime, base):
        super().__init__(prime, base)
