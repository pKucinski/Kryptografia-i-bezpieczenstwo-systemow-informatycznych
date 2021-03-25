import string


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

    def lamanie_szyfru(self):

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
    text = input()
    if "-c" == text[-5:-3]:
        cezar = szyfr_cezara.Cezar(text)
        if "-e" == text[-2:]:
            key = get_key()
            cezar.szyfrowanie(key)
        elif "-d" == text[-2:]:
            key = get_key()
            cezar.odszyfrowywanie(key)
        elif "-j" == text[-2:]:
            cezar.kryptoanaliza()
        elif "-k" == text[-2:]:
            cezar.lamanie_szyfru()
        else:
            print("Nieprawidłowa opcja")

    elif "-a" in text:
        afiniczny = szyfr_afiniczny.Afiniczny(text)
        if "-e" in text:
            a = get_key()
            b = input()
            b = int(b)
            afiniczny.szyfrowanie(a, b)
        elif "-d" in text:
            a = get_key()
            b = input()
            b = int(b)
            afiniczny.odszyfrowywanie(a, b)
        elif "-j" in text:
            afiniczny.kryptoanaliza()
        elif "-k" in text:
            afiniczny.lamanie_szyfru()
        else:
            print("Nieprawidłowa opcja")
