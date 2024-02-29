import unittest
import os
from tempfile import TemporaryDirectory
from unittest.mock import patch, Mock
from Encryptor import FileEncryptor  

class TestFileEncryptor(unittest.TestCase):
    def setUp(self):
        self.file_encryptor = FileEncryptor()

    def tearDown(self):
        pass

    @patch('OptionBox.option_box', return_value='testpassword')
    @patch('pyttsx3.init')
    @patch('pyttsx3.Engine.say')
    @patch('pyttsx3.Engine.runAndWait')
    def test_encrypt_and_decrypt(self, mock_option_box, mock_init, mock_say, mock_runAndWait):
        # Create a temporary directory to store test files
        with TemporaryDirectory() as temp_dir:
        #     # Create a test file for encryption
            input_file_path = os.path.join(temp_dir, 'test_file.txt')
            with open(input_file_path, 'w') as test_file:
                test_file.write('This is a test file.')
    pass

    def test_validate_file_path_invalid(self):
        # Test with an invalid file path
        invalid_file_path = 'nonexistent_file.txt'
        result = self.file_encryptor.validate_file_path(invalid_file_path)
        self.assertFalse(result)

    def test_validate_file_path_valid(self):
        # Test with a valid file path
        with TemporaryDirectory() as temp_dir:
            valid_file_path = os.path.join(temp_dir, 'valid_file.txt')
            with open(valid_file_path, 'w') as test_file:
                test_file.write('This is a valid test file.')

            result = self.file_encryptor.validate_file_path(valid_file_path)
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
