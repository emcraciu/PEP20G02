from random import randint

from communication import Client, Server
from utils.helpers import read_from_keyboard, prime_numbers

MAX_PRIME = 101
BASE = randint(17, MAX_PRIME)
TEXT = 'Text that will be sent'

primes = prime_numbers(MAX_PRIME)
prime = read_from_keyboard(primes)

server = Server(prime, BASE)
client = Client(prime, BASE, 'localhost')

server.start()
client.start()

client.send(TEXT)
server.stop()

assert TEXT == server.messages[0][1], 'Decrypt failed'
