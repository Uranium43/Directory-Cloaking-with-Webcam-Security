import cv2
import os
import shutil
import getpass
from cryptography.fernet import Fernet

class FileLocker:
    def __init__(self):
        self.filepath = input("Enter the path to the file: ")
        self.password = getpass.getpass("Set a password for the file: ")
        with open('password.txt', 'w') as password_file:  # Save the password to a file
            password_file.write(self.password)
        self.attempts = 0
        self.key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:  # Save the key to a file
            key_file.write(self.key)
        self.cipher_suite = Fernet(self.key)
        self.hidden_path = r"C:\Users\ajink\OneDrive\Desktop\Secrete"


    def lock_file(self):
        with open(self.filepath, 'rb') as file:
            encrypted_data = self.cipher_suite.encrypt(file.read())
        with open(self.filepath, 'wb') as file:
            file.write(encrypted_data)

    def unlock_file(self):
        while self.attempts < 3:
            password = getpass.getpass("Enter your password: ")
            with open('password.txt', 'r') as password_file:  # Load the password from the file
                correct_password = password_file.read().strip()
            if password == correct_password:
                with open('key.key', 'rb') as key_file:  # Load the key from the file
                    self.key = key_file.read()
                self.cipher_suite = Fernet(self.key)
                self.decrypt_file()
                print("File unlocked!")
                return
            else:
                self.attempts += 1
                print("Incorrect password. Try again.")
        print("Too many incorrect attempts. The file will be hidden.")
        self.capture_photo()
        self.hide_file()

    def decrypt_file(self):
        with open(self.filepath, 'rb') as file:
            decrypted_data = self.cipher_suite.decrypt(file.read())
        with open(self.filepath, 'wb') as file:
            file.write(decrypted_data)

    def hide_file(self):
        shutil.move(self.filepath, self.hidden_path)

    def capture_photo(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(os.path.join(self.hidden_path, "intruder.jpg"), frame)
        cam.release()

locker = FileLocker()
locker.lock_file()
locker.unlock_file()