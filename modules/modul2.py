from random import randint

data = 'some random text _1'

client_rand = randint(1, 10)
server_rand = randint(1, 10)


def client(prime, base, value=None):
    if value is None:
        power = base ** client_rand % prime
    else:
        power = value ** client_rand % prime
    return power


def server(prime, base, value=None):
    if value is None:
        power = base ** server_rand % prime
    else:
        power = value ** server_rand % prime
    return power


def encrypt(data, xor_value=100):
    print(data)
    result1 = data[::-1]
    result2 = result1[0::2] + result1[1::2]
    result3 = ''
    for char in result2:
        result3 += chr(ord(char).__xor__(xor_value))
    print(result3)
    return result3


def decrypt(data, xor_value=100):
    result = ''
    for char in data:
        result += chr(ord(char).__xor__(xor_value))
    split = len(result) // 2 + len(result) % 2
    data1 = list(result[:split])
    data2 = list(result[split:])
    if len(result) % 2:
        data2.append('')
    list_data = data1 * 2
    list_data[0::2] = data1
    list_data[1::2] = data2
    result = ''
    for value in list_data:
        result += value
    result = result[::-1]
    print(result)
    return result


def prime_numbers(limit):
    prime_numbers_list = []
    for x in range(1, limit):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime_numbers_list.append(x)
    return prime_numbers_list


def read_from_keyboard(primes, limit):
    value = int(input('Provide prime number:'))
    for prime in primes(limit):
        if value == prime:
            return value
    else:
        raise Exception


def man_in_the_middle(prime, base, value=None):
    for i in range(1, 10):
        if value ** (1 / i) == base:
            return i


# read = read_from_keyboard()
# read(3)
#
#
# # while initial_value:
# #     for prime in primes:
# #         if initial_value == prime:
# #             break
# #     if initial_value == prime:
# #         break
# #     initial_value = int(input('Please provide prime number:'))
#
# # enc_txt = encrypt(data)
# # org_txt = decrypt(enc_txt)
# # print(data == org_txt)

if __name__ == '__main__':
    prime = read_from_keyboard(prime_numbers, 101)
    base = randint(5, prime)
    send_to_server = client(prime, base)
    send_to_client = server(prime, base)
    # print(man_in_the_middle(prime, base, send_to_server))
    # print(man_in_the_middle(prime, base, send_to_server))
    result1 = client(prime, base, send_to_client)
    print(result1)
    result2 = server(prime, base, send_to_server)
    print(result2)
