from random import randint

from communication import Client, server
from communication.decrypt import decrypt
from communication.encrypt import encrypt
from utils.helpers import read_from_keyboard, prime_numbers

MAX_PRIME = 101
BASE = randint(5, MAX_PRIME)
TEXT = 'TEXT to send'

primes = prime_numbers(MAX_PRIME)
prime = read_from_keyboard(primes)

client = Client(prime, BASE)
send_to_server = client.calculate_send_distribute()
send_to_client = server(prime, BASE)
client.value_modifier(send_to_client)
client_xor_key = client.calculate_response_distribute()
server_xor_key = server(prime, BASE, send_to_server)

encrypted_text = encrypt(TEXT, client_xor_key)
decrypted_text = decrypt(encrypted_text, server_xor_key)
print(TEXT)
print(encrypted_text)
print(decrypted_text)
assert TEXT == decrypted_text, 'Decrypt failed'