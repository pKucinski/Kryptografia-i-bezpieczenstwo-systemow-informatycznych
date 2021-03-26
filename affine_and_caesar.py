import string
import sys

abc = string.ascii_lowercase
one_time_pad = list(abc)

help = """help:
-p prepare
-e encrypt
-k cryptanalysis 
"""


class Afiniczny:
    def __init__(self, text):
        self.text = text

        f = open("plain.txt", "w+")
        f.write(text[:-6])
        f.close()

    def rozszerzony_euklides(self, a):
        for i in range(1, 27):
            if (a * i) % 26 == 1:
                return i

    def szyfrowanie(self, a, b):
        open("crypto.txt", "w").close()
        alphabet = list(string.ascii_lowercase)
        ALPHABET = list(string.ascii_uppercase)
        w = open("crypto.txt", "a")

        for letter in self.text[:-6]:
            if letter in ALPHABET:
                number = ALPHABET.index(letter)
                sign = (a * int(number) + b) % 26
                w.write(ALPHABET[sign])
            elif letter in alphabet:
                number = alphabet.index(letter)
                sign = (a * int(number) + b) % 26
                w.write(alphabet[sign])
            else:
                w.write(letter)
        w.close()

    def odszyfrowywanie(self, a, b):
        key = self.rozszerzony_euklides(a)

        open("decrypto.txt", "w").close()

        alphabet = list(string.ascii_lowercase)
        ALPHABET = list(string.ascii_uppercase)

        decrypto = open("decrypto.txt", "a")
        crypto = open("crypto.txt", "r").read()

        for letter in crypto:
            if letter in alphabet:
                sign = (key * (alphabet.index(letter) - b))
                sign = sign % 26
                decrypto.write(alphabet[sign])
            elif letter in ALPHABET:
                sign = (key * (ALPHABET.index(letter) - b))
                sign = sign % 26
                decrypto.write(ALPHABET[sign])
            else:
                decrypto.write(letter)

        decrypto.close()

    def kryptoanaliza(self):
        None

    def lamanie_szyfru(self):
        None

class Cezar():
        def __init__(self, text):
            self.text = text

            f = open("plain.txt", "w+")
            f.write(text[:-6])
            f.close()

        def szyfrowanie(self, key):
            open("crypto.txt", "w").close()
            alphabet = list(string.ascii_lowercase)
            ALPHABET = list(string.ascii_uppercase)
            w = open("crypto.txt", "a")

            for letter in self.text[:-6]:
                if letter in ALPHABET:
                    number = ALPHABET.index(letter)
                    sign = (int(number) + key) % 26
                    w.write(ALPHABET[sign])
                elif letter in alphabet:
                    number = alphabet.index(letter)
                    sign = (int(number) + key) % 26
                    w.write(alphabet[sign])
                else:
                    w.write(letter)

            w.close()

        def odszyfrowywanie(self, key):
            open("decrypto.txt", "w").close()

            alphabet = list(string.ascii_lowercase)
            ALPHABET = list(string.ascii_uppercase)

            decrypto = open("decrypto.txt", "a")
            crypto = open("crypto.txt", "r").read()
            key = key

            for letter in crypto:
                if letter in alphabet:
                    number = alphabet.index(letter)
                    sign = (int(number) + key) % 26
                    decrypto.write(alphabet[sign])
                elif letter in ALPHABET:
                    number = ALPHABET.index(letter)
                    sign = (int(number) + key) % 26
                    decrypto.write(ALPHABET[sign])
                else:
                    decrypto.write(letter)

            decrypto.close()

        def lamanie_szyfru(self):
            crypto = open("crypto.txt", "r").read()
            f = open("plain.txt", "w")
            alphabet = list(string.ascii_lowercase)
            ALPHABET = list(string.ascii_uppercase)

            for i in range(1, 26):
                for letter in crypto:
                    if letter in alphabet:
                        number = alphabet.index(letter)
                        sign = (int(number) + i) % 26
                        f.write(alphabet[sign])
                    elif letter in ALPHABET:
                        number = ALPHABET.index(letter)
                        sign = (int(number) + i) % 26
                        f.write(ALPHABET[sign])
                    else:
                        f.write(letter)
                f.write('\n')

        def kryptoanaliza(self):
            crypto = open("crypto.txt", "r").read()
            decrypto = open("decrypto.txt", "r").read()

            alphabet = list(string.ascii_lowercase)

            key = alphabet.index(decrypto[0]) - alphabet.index(crypto[0])

            if key < 0:
                key = -key
            print("key wynosi", key)


def get_key():
    key = input()
    key = int(key)
    while True:
        if (key >= 1 and key < 26):
            break
            key = input()
            print("x")
        else:
            print("klucz musi być w zakresie 1-26")
    return key


if __name__ == '__main__':
    options = ["-p", "-e", "-k"]
    if len(sys.argv) == 1 or sys.argv[1] not in options:
        print(help)
        exit(0)

    key = input("Key: ")
    msg = input("Message: ")

    if sys.argv[1] == options[0]:
        None
    elif sys.argv[1] == options[1]:
        Cezar.
    elif sys.argv[1] == options[2]:
        print(decrypt(msg, key))
