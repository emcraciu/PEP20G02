def encrypt(data, xor_value=100):
    result = ''
    for char in data:
        result += chr(ord(char).__xor__(xor_value))
    return result