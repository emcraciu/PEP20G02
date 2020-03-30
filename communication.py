from random import randint

from communication import Client, Server
from communication.decrypt import decrypt
from communication.encrypt import encrypt
from utils.helpers import read_from_keyboard, prime_numbers

MAX_PRIME = 101
BASE = randint(5, MAX_PRIME)
TEXT = 'TEXT to send'

primes = prime_numbers(MAX_PRIME)
prime = read_from_keyboard(primes)

client = Client(prime, BASE)
server = Server(prime, BASE)
send_to_server = client.calculate_send_distribute()
send_to_client = server.calculate_send_distribute()
client.value_modifier(send_to_client)
server.value_modifier(send_to_server)
client_xor_key = client.calculate_response_distribute()
server_xor_key = server.calculate_response_distribute()

encrypted_text = encrypt(TEXT, client_xor_key)
decrypted_text = decrypt(encrypted_text, server_xor_key)
print(TEXT)
print(encrypted_text)
print(decrypted_text)
assert TEXT == decrypted_text, 'Decrypt failed'