from cryptography.fernet import Fernet
import getpass

def decrypt_file():
    filepath = input("Enter the path to the encrypted file: ")
    password = getpass.getpass("Enter your password: ")
    with open('password.txt', 'r') as password_file:  # Load the password from the file
        correct_password = password_file.read().strip()
    if password != correct_password:
        print("Incorrect password. The file will not be decrypted.")
        return
    with open('key.key', 'rb') as key_file:  # Load the key from the file
        key = key_file.read()
    cipher_suite = Fernet(key)
    with open(filepath, 'rb') as file:
        decrypted_data = cipher_suite.decrypt(file.read())
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)
    print("File decrypted!")

decrypt_file()