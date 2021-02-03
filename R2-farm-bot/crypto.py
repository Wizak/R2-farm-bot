from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('crypto.key', 'rb').read()

def decrypter(key):
    filename = 'R2bot.exe'

    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def encrypter():
    key = 'n4BppjMYzCRYvbmEqO3I9_Wxtipzgh2qLOac8i6_tC4=' #input data!
    filename = 'R2bot.exe'

    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


if __name__ == '__main__':
    write_key()