def cesar_code(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for i in message:
        if i.lower() in alphabet:
            code += alphabet[(alphabet.index(i.lower()) + key) % len(alphabet)]
        else:
            code += i
    print(code)


def cesar_decode(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decode = ''
    for i in message:
        if i.lower() in alphabet:
            decode += alphabet[(alphabet.index(i.lower()) - key) % len(alphabet)]
        else:
            decode += i
    print(decode)


def brutforce(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(alphabet)):
        decode = ''
        for i in message:
            if i.lower() in alphabet:
                decode += alphabet[(alphabet.index(i.lower()) - key) % len(alphabet)]
            else:
                decode += i
        print(decode)

def start():
    print("Please, select mode:\n1 - encode\n2 - decode\n3 - brutforce secret message")


def encode_mode():
    print("Type your message, then press Enter and type the secret key, then press Enter")


def decode_mode():
    print("Type your encoded message, then press Enter and type the secret key, then press Enter")


def brutforce_help():
    print("Type secret message and press enter")


start()
flag = 0
while not flag:
    mode = int(input())
    if mode in (1, 2, 3):
        flag = 1
        if mode == 1:
            encode_mode()
            cesar_code(input(), int(input()))
        elif mode == 2:
            decode_mode()
            cesar_decode(input(), int(input()))
        elif mode == 3:
            brutforce_help()
            brutforce(input())
    else:
        print(f'No mode {mode}')
        start()
