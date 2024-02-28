import os
import pyAesCrypt
from OptionBox import option_box
from tkinter import filedialog, Tk
import pyttsx3

class FileEncryptor:
    def __init__(self):
        # encryption/decryption buffer size - 64K
        self.bufferSize = 64 * 1024
        self.file_name = '*'
        self.encrypted_file_path = None  # New variable to store the encrypted file path

    def encrypt(self, file_path=None, output_path=None):
        if not self.validate_file_path(file_path):
            return

        self.file_name = file_path.split('/')[-1]

        password = option_box(msg='Enter the password you want to set.',
                              b1='OK',
                              b2='Cancel',
                              frame=False,
                              entry=True,
                              t=False)

        aesOption = dict(defaultextension='.aes', initialfile=self.file_name + '.aes',
                         filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])

        if output_path is None:
            output_path = filedialog.asksaveasfilename(**aesOption)

        try:
            pyAesCrypt.encryptFile(file_path, output_path, password, self.bufferSize)
            # Save the encrypted file path
            self.encrypted_file_path = output_path

            # Announce the saved directory using text-to-speech
            self.speak("Encrypted file saved at " + self.encrypted_file_path)

            # Close the file dialog and destroy the root window
            self.close_file_dialog()
        except Exception as e:
            print(f"Error encrypting file: {e}")

    def decrypt(self, file_path=None, output_path=None):
        if not self.validate_file_path(file_path):
            return

        aesOption = dict(defaultextension='.aes', initialfile=self.file_name + '.aes',
                         filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])

        if file_path is None:
            file_path = filedialog.askopenfilename(**aesOption)
            self.file_name = file_path.split('/')[-1].replace('.aes', '')

        password = option_box(msg='Enter file password',
                              b1='OK',
                              b2='Cancel',
                              frame=False,
                              entry=True,
                              t=False)

        allOption = dict(initialfile=self.file_name, filetypes=[('All Files', '*.*')])

        if output_path is None:
            output_path = filedialog.asksaveasfilename(**allOption)

        try:
            pyAesCrypt.decryptFile(file_path, output_path, password, self.bufferSize)
            # Close the file dialog and destroy the root window
            self.close_file_dialog()
        except Exception as e:
            print(f"Error decrypting file: {e}")

    def validate_file_path(self, file_path):
        if file_path is None or not os.path.exists(file_path):
            # print("Invalid input file path.")
            return False
        return True

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def close_file_dialog(self):
        # Get the root Tkinter window
        root = Tk()
        # Withdraw (hide) the file dialog
        root.withdraw()
        # Destroy the root window
        root.destroy()

# Example usage:
file_encryptor = FileEncryptor()
file_encryptor.encrypt()

# Access the encrypted file path
# print("Encrypted file saved at:", file_encryptor.encrypted_file_path)

# Or perform decryption
# file_encryptor.decrypt()
