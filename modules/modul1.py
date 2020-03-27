def encrypt(data, xor_key=100):
    """

    :param data:
    :return:
    """

    result = data[::-1]
    print(result[0::2])
    print(result[1::2])
    result = result[0::2] + result[1::2]
    xor_result = []
    for index in range(len(result)):
        xor_result[index] = ord(result[index]).__xor__(xor_key)
    new_result = ''
    for letter in xor_result:
        new_result += letter
    return result


def decrypt(data):
    """

    :param data:
    :return:
    """
    len(data) % 2
    data1 = list(data[:5])
    print(data1)
    data2 = list(data[5:])
    print(data2)
    if len(data) % 2:
        data2.append('')
    result = data1 * 2
    print(result)
    result[::2] = data1
    result[1::2] = data2
    print(result)
    result = result[::-1]

    return result


clear_text = 'some text'
encrypted_text = encrypt(clear_text)
decrypted_text = decrypt(encrypted_text)
assert clear_text == decrypted_text
