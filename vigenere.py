def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))



if __name__ == '__main__':
    options = ["-p", "-e", "-k"]
    if sys.argv[1] not in options:
        print(help)
        exit(0)

    key = input("Key: ")
    msg = input("Message: ")

    if sys.argv[1] == options[0]:
        None
    elif sys.argv[1] == options[1]:
        print(encrypt(msg, key))
    elif sys.argv[1] == options[2]:
        print(decrypt(msg, key))