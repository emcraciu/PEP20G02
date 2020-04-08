from socket import socket
from threading import Thread

from communication import Communicator
from communication.decrypt import decrypt


class Server(Communicator):
    """Server for transferring encrypted data based on a shared secret key"""

    def __init__(self, prime, base, port=None):
        super().__init__(prime, base)
        self.host = 'localhost'
        self.port = port or 1234
        self.messages = []

    def start(self):
        """Start communication server to listen for incoming connections

        :return: None
        """
        self.socket = socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.process = Thread(target=self.receive_message,
                              args=(self.messages,))
        self.process.start()

    def stop(self):
        """Stop communication server
        :return:
        """
        self.process.join()

    def receive_message(self, messages):
        """Connect to socket and listen for incoming key exchange and message

        :param messages: list to
        :return:
        """
        connection, addr = self.socket.accept()
        with connection:
            print('Connected by', addr)
            self.__server_key_exchange(connection)
            encrypted_message = str(connection.recv(4096), encoding='UTF-8')
        message = decrypt(encrypted_message, self._Communicator__shared_secret)
        messages.append((addr, message))

    def __server_key_exchange(self, connection):
        self.remote_distribute = int(connection.recv(4096))
        connection.send(bytes(str(self.local_distribute), encoding='UTF-8'))
        self.calculate_response_distribute()
