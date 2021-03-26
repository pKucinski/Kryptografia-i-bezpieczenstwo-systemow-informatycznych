import string
import sys

def encrypt(msg, key):
    return

def decrypt(ciphertext, key):
    return


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