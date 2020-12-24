import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def write_key(key_name, password, salt):
    salt = bytes(salt, encoding='utf-8')
    password = bytes(password, encoding='utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    if os.path.exists(key_name):
        return
    key = base64.urlsafe_b64encode(kdf.derive(password))
    with open(key_name, "wb") as key_file:
        return key_file.write(key)

def load_key(key_name):
        return open(key_name, "rb").read()

def del_key(key_name):
    return os.remove(key_name)

def encrypt_manual(key, filename):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

        encrypted = f.encrypt(file_data)

        with open(filename, 'wb') as file:
            return file.write(encrypted)

def decrypt_manual(key, filename):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

        decrypted = f.decrypt(file_data)

        with open(filename, 'wb') as file:
            return file.write(decrypted)

def encrypt_auto(filename, password, salt):
    logfile = open('CryptingLog.txt', 'w')
    salt = bytes(salt, encoding='utf-8')
    password = bytes(password, encoding='utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)

    if filename == '.':
        return print("You are trying to encrypt the current folder.")

    if os.path.isdir(filename):
        for subdir, dirs, files_indir in os.walk(filename):
            for filename_indir in files_indir:
                filepath = subdir + os.sep + filename_indir
                with open(filepath, 'rb') as file:
                    file_data = file.read()

                    encrypted = f.encrypt(file_data)
                
                    with open(filepath, 'wb') as file:
                        file.write(encrypted)
                        logfile.writelines("Encrypted: " + str(filepath) + "\n")
                        print("Encrypted: " + str(filepath))
        return
                
    else:
        with open(filename, 'rb') as file:
            file_data = file.read()

            encrypted = f.encrypt(file_data)

            with open(filename, 'wb') as file:
                return file.write(encrypted)

def decrypt_auto(filename, password, salt):
    logfile = open('CryptingLog.txt', 'w')
    salt = bytes(salt, encoding='utf-8')
    password = bytes(password, encoding='utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)

    if filename == '.':
        return print("You are trying to decrypt the current folder.")

    if os.path.isdir(filename):
        for subdir, dirs, files_indir in os.walk(filename):
            for filename_indir in files_indir:
                filepath = subdir + os.sep + filename_indir
                with open(filepath, 'rb') as file:
                    file_data = file.read()

                    decrypted = f.decrypt(file_data)
                
                    with open(filepath, 'wb') as file:
                        file.write(decrypted)
                        logfile.writelines("Decrypted: " + str(filepath) + "\n")
                        print("Decrypted: " + str(filepath))
        return
                
    else:
        with open(filename, 'rb') as file:
            file_data = file.read()

            decrypted = f.decrypt(file_data)

            with open(filename, 'wb') as file:
                return file.write(decrypted)
