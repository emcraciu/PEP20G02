from socket import socket

from communication import Communicator
from communication.encrypt import encrypt


class Client(Communicator):

    def __init__(self, prime, base, host, port=None):
        super().__init__(prime, base)
        self.host = host
        self.port = port or 1234

    def start(self):
        """Start communication client to listen for incoming connections

        :return: None
        """
        self.socket = socket()
        self.socket.connect((self.host, self.port))
        self.__client_key_exchange()

    def __client_key_exchange(self):
        self.socket.send(bytes(str(self.local_distribute), encoding='UTF-8'))
        self.remote_distribute = int(self.socket.recv(4096))
        self.calculate_response_distribute()

    def send(self, message):
        encrypted_message = encrypt(message, self._Communicator__shared_secret)
        self.socket.send(bytes(encrypted_message, 'UTF-8'))
