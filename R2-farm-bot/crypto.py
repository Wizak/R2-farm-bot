from cryptography.fernet import Fernet


def encrypter():
    key = Fernet.generate_key()
    filename = 'R2bot.exe'

    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)