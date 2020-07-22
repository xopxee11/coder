def cesar_code(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 ,.!?'
    code = ''
    for i in message:
        if i.lower() in alphabet:
            code += alphabet[(alphabet.index(i.lower()) + key) % len(alphabet)]
        else:
            code += i
    return code


def cesar_decode(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 ,.!?'
    decode = ''
    for i in message:
        if i.lower() in alphabet:
            decode += alphabet[(alphabet.index(i.lower()) - key) % len(alphabet)]
        else:
            decode += i
    return decode


def bruteforce(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 ,.!?'
    result = []
    for key in range(len(alphabet)):
        decode = ''
        for i in message:
            if i.lower() in alphabet:
                decode += alphabet[(alphabet.index(i.lower()) - key) % len(alphabet)]
            else:
                decode += i
        result.append(decode)
    return result
