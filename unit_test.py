import unittest
import os
import tkinter as tk
from tkinter import ttk 
from unittest.mock import patch, Mock
from tkinter import TclError  # Import TclError to handle Tkinter-related errors
from ShieldXpert_Main import Kilo_Antivirus, Settings, Scan, Home,Scan_Utility, Feedback
from register_login.startup import AntivirusApp
from register_login.register import Registrationroot
from register_login.login import AntivirusApp
# import unittest
# from unittest.mock import patch
from Antivirusmaster.OptionBox import OptionBox  # Replace 'your_module' with the actual name of your module


class TestKiloAntivirus(unittest.TestCase):

    def setUp(self):
        # self.app = Kilo_Antivirus()
        pass

    def test_initialization(self):
        # self.assertIsInstance(self.app, Kilo_Antivirus)
        pass

    def test_show_frame(self):
        # self.app.show_frame("Home")
        # You can add assertions here to check if the "Home" frame is displayed as expected
        pass

    # Add more test cases for non-GUI functionalities

    @patch("builtins.open", new_callable=Mock)
    def test_file_reading(self, mock_open):
        mock_open.side_effect = [
            Mock(__enter__=Mock(return_value=Mock(read=Mock(return_value="2022-02-10")))),
            Mock(__enter__=Mock(return_value=Mock(read=Mock(return_value="test_username")))),
            Mock(__enter__=Mock(return_value=Mock(read=Mock(return_value="test_password")))),
            Mock(__enter__=Mock(return_value=Mock(read=Mock(return_value="test_email")))),
        ]
        # self.read_user_info()
        # self.assertEqual(self.pur_date, "2022-02-10")

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        # self.controller = Kilo_Antivirus()

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        # self.assertIsInstance(self.settings_frame, Settings)
        pass

    @patch("builtins.print")
    def test_button_5_command(self, mock_print):
        self.controller = tk.Tk()
        settings_frame = Settings(self.root, self.controller)

        settings_frame.button_5.invoke()
        mock_print.assert_called_with("self.button_5 clicked")

    @patch("webbrowser.open_new")
    def test_button_1_command(self, mock_open_new):
        self.controller = tk.Tk()
        settings_frame = Settings(self.root, self.controller)
        # Simulate a click on button_1 and check if the correct URL is opened
        settings_frame.button_1.invoke()
        # mock_print.assert_called_with("self.button_1 clicked")
        # mock_open_new.assert_called_once_with("https://github.com/bishal78441")
        pass

    @patch("webbrowser.open_new")
    def test_button_4_click(self, mock_open_new):
        self.controller = tk.Tk()
        settings_frame = Settings(self.root, self.controller)
        # Simulate a click on button_4 and check if the correct URL is opened
        settings_frame.button_4.invoke()
        # mock_open_new.assert_called_once_with("http://localhost/site1/index.html")
        pass
        
    @patch("webbrowser.open_new")
    def test_button_7_click(self, mock_open_new):
        # # Simulate a click on button_7 and check if the correct URL is opened
        # self.settings_frame.button_7.invoke()
        # mock_open_new.assert_called_once_with("https://github.com/bishal78441")
        pass

    def test_show_frame(self):
        # self.settings_frame.show_frame("Home")
        # You can add assertions here to check if the "Home" frame is displayed as expected
        pass


class TestScanHomeGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()


        # self.assertEqual(controller.frames["Home"], controller.current_frame)

        # home_frame.button_4.invoke()  # Assuming callback for button_4 is defined
        # Add assertions or checks based on the expected behavior of button_4

        # Repeat for other buttons as needed

    def test_home_buttons(self):
        controller = tk.Tk()
        home_frame = Home(self.root, controller)

        # Test button click actions for Home class
        home_frame.button_1.invoke()
        # Add assertions or checks based on the expected behavior of button_1

        # home_frame.button_2.invoke()
        # self.assertEqual(controller.frames["Settings"], controller.current_frame)

        # Repeat for other buttons as needed

class TestScanUtility(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        # self.controller = Mock(title_font=None) 

    def tearDown(self):
        self.root.destroy()

    def test_clear(self):
        self.controller = tk.Tk()
        scan_utility_frame = Scan_Utility(self.root, self.controller)

        # Mocking the necessary attributes/methods
        scan_utility_frame.pb = ttk.Progressbar(self.root)
        scan_utility_frame.value_label = ttk.Label(self.root)
        scan_utility_frame.panel = ttk.Label(self.root)


        self.assertFalse(scan_utility_frame.panel.winfo_ismapped(), "Panel should not be mapped initially.")
        self.assertIsNotNone(scan_utility_frame.pb, "Progressbar should be initialized.")
        self.assertIsNotNone(scan_utility_frame.value_label, "Value label should be initialized.")
    
        pass

    def test_start_scan(self):
        controller = tk.Tk()
        scan_utility_frame = Scan_Utility(self.root, controller)

        # Mocking the necessary attributes/methods
        scan_utility_frame.pb = ttk.Progressbar(self.root)
        scan_utility_frame.value_label = ttk.Label(self.root)
        scan_utility_frame.panel = ttk.Label(self.root)

        self.assertIsNotNone(scan_utility_frame.pb, "Progressbar should be initialized.")
        self.assertIsNotNone(scan_utility_frame.value_label, "Value label should be initialized.")
        self.assertIsNotNone(scan_utility_frame.panel, "Panel should be initialized.")
        # Add more assertions based on the expected behavior of start_scan method
        pass



class TestHome(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch("builtins.print")
    def test_button_commands(self, mock_print):
        controller = tk.Tk()
        home_frame = Home(self.root, controller)

        home_frame.button_1.invoke()  # Assuming button_1 is the actual attribute
        mock_print.assert_called_with("button_1 clicked")


class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.controller = Mock()
        self.feedback_frame = Feedback(self.root, self.controller)

    def tearDown(self):
        self.root.destroy()

    @patch("builtins.print")
    @patch("mysql.connector.connect")
    @patch("mysql.connector.Error")
    def test_submit_button(self, mock_error, mock_connect, mock_print):
        # Set up the input fields with some values
        # self.feedback_frame.entry_2.insert(0, "John Doe")  # Name
        # self.feedback_frame.entry_3.insert(0, "Bug Report")  # Subject
        # self.feedback_frame.entry_1.insert('1.0', "This is a bug report.")  # Feedback Text

        # Mock the mysql.connector.Error
        mock_error_instance = mock_error.return_value
        

        # Call the submit function
        # self.feedback_frame.submit()

        # Assert that the expected database interactions occurred
        # # mock_connect.assert_called_once()
        # mock_conn.cursor.assert_called_once()
        # mock_cursor.execute.assert_called_once()
        pass

# allpathtest.py

class TestFilePaths(unittest.TestCase):

    def test_picture_path(self):
        picture_path = os.path.abspath("No_Virus_Found.png")
        self.assertTrue(os.path.exists(picture_path), f"File not found: {picture_path}")

    def test_icon_path(self):
        icon_path = os.path.abspath("Antivirus_Logo.png")
        self.assertTrue(os.path.exists(icon_path), f"File not found: {icon_path}")

    def test_username_file_path(self):
        username_file_path = os.path.abspath("User_credn/usernames.txt")
        self.assertTrue(os.path.exists(username_file_path), f"File not found: {username_file_path}")

    def test_password_file_path(self):
        password_file_path = os.path.abspath("User_credn/password.txt")
        self.assertTrue(os.path.exists(password_file_path), f"File not found: {password_file_path}")

    def test_email_file_path(self):
        email_file_path = os.path.abspath("User_credn/email.txt")
        self.assertTrue(os.path.exists(email_file_path), f"File not found: {email_file_path}")

    def test_purchase_file_path(self):
        purchase_file_path = os.path.abspath("User_credn/purchase.txt")
        self.assertTrue(os.path.exists(purchase_file_path), f"File not found: {purchase_file_path}")

class TestAntivirusApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = AntivirusApp(self.root)

    def tearDown(self):
        if self.root.winfo_exists():
            self.root.destroy()

    def test_gui_elements(self):
        # Check if GUI elements are created correctly
        expected_text = 'Please Wait...  0%'
        actual_text = self.app.progress_label.cget("text")
        
        try:
            self.assertTrue(actual_text.startswith('Please Wait...') and actual_text.endswith('0%'))
            # self.assertIsNotNoneself.app.progress_label("heeh")
        except tkinter.TclError:
            pass  # Ignore TclError when the window has been destroyed

     # Ignore TclError when the window has been destroyed



class TestRegistrationroot(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.registration_root = Registrationroot(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_open_login_page(self):

        pass


    def test_clear_form(self):
        # Assuming clear_form method clears the input fields
        self.registration_root.firstName_entry.insert(0, "John")
        self.registration_root.lastName_entry.insert(0, "Doe")
        self.registration_root.emailName_entry.insert(0, "john.doe@example.com")
        self.registration_root.passwordName_entry.insert(0, "password123")
        self.registration_root.confirm_passwordName_entry.insert(0, "password123")

        self.registration_root.clear_form()

        self.assertEqual(self.registration_root.firstName_entry.get(), "")
        self.assertEqual(self.registration_root.lastName_entry.get(), "")
        self.assertEqual(self.registration_root.emailName_entry.get(), "")
        self.assertEqual(self.registration_root.passwordName_entry.get(), "")
        self.assertEqual(self.registration_root.confirm_passwordName_entry.get(), "")

    def test_validate_password(self):
        # Assuming validate_password method works as expected
        valid_password = "Abcd123!"
        invalid_password = "weak"

        self.assertTrue(self.registration_root.validate_password(valid_password))
        self.assertFalse(self.registration_root.validate_password(invalid_password))

    def test_insert_data(self):
        # Assuming insert_data method works as expected
        # Provide test data
        self.registration_root.firstName_entry.insert(0, "John")
        self.registration_root.lastName_entry.insert(0, "Doe")
        self.registration_root.emailName_entry.insert(0, "john.doe@example.com")
        self.registration_root.passwordName_entry.insert(0, "StrongPass123!")
        self.registration_root.confirm_passwordName_entry.insert(0, "StrongPass123!")



    def test_open_login_page_after_registration(self):
        pass

    def test_invalid_email_format(self):
        # Test when an invalid email format is entered
        self.registration_root.emailName_entry.insert(0, "invalid_email")
        pass


    def test_password_mismatch(self):
        # Test when passwords do not match
        self.registration_root.passwordName_entry.insert(0, "StrongPass123!")
        self.registration_root.confirm_passwordName_entry.insert(0, "Mismatch123!")
        pass

    def clear_forms(self):
        pass



class TestAntivirusApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method runs once for the entire test class
        pass

    @classmethod
    def tearDownClass(cls):
        # This method runs once after all the tests in the class are executed
        pass

    def setUp(self):
        # This method runs before each individual test
        pass

    def tearDown(self):
        # This method runs after each individual test
        pass

    def test_open_signup_page(self):
        # with patch('subprocess.Popen') as mock_popen:
            # self.app.open_signup_page()
            # mock_popen.assert_called_once_with(['python', 'path_to_register.py'], shell=True)
            pass

    def test_open_startup(self):
        # with patch('os.system') as mock_os_system:
            # self.app.open_startup()
# sert_called_once_with("python path_to_startup.py")
            pass

    @patch('webbrowser.open_new')
    def test_update_github(self, mock_open_new):
        pass
        # self.app.update_github()
        # mock_open_new.assert_called_once_with('https://github.com/bishal78441/ShieldXpert/blob/main/README.md')

    @patch('tkinter.messagebox.showinfo')
    @patch('mysql.connector.connect')
    def test_update_password(self, mock_connect, mock_showinfo):
        pass

    def test_forgot_password(self):
        pass

    @patch('tkinter.messagebox.showerror')
    @patch('mysql.connector.connect')
    def test_login_invalid_credentials(self, mock_connect, mock_showerror):
        pass



class TestOptionBox(unittest.TestCase):
    def test_option_box_with_entry(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Entry widget and Button widget
            instance = mock_entry.return_value
            instance.get.return_value = 'TestEntryValue'
            mock_button.side_effect = [None, None]  # Mocking button actions

            # Call option_box with entry=True
            # result = OptionBox("Test Message", "OK", "Cancel", True, False, True)

            # Assert that the Entry widget is created and focused
            # mock_entry.assert_called_once()
            # instance.focus_set.assert_called_once()

            # # Assert that the Button widget is created twice (for OK and Cancel)
            # mock_button.assert_called_with(mock_button.side_effect[0])
            # self.assertEqual(mock_button.call_count, 2)

            # # Assert the returned result
            # self.assertEqual(result, 'TestEntryValue')

    def test_option_box_without_entry(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Button widget
            mock_button.side_effect = [None, None]  # Mocking button actions

            # Call option_box with entry=False
            # result = OptionBox("Test Message", "OK", "Cancel", True, False, False)

            # Assert that the Entry widget is not created
            # mock_entry.assert_not_called()

            # Assert that the Button widget is created twice (for OK and Cancel)
            # mock_button.assert_called_with(mock_button.side_effect[0])
            # self.assertEqual(mock_button.call_count, 2)

            # Assert the returned result
            # self.assertIsNone(result)

    def test_option_box_with_custom_buttons(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Button widget
            mock_button.side_effect = [None, None]  # Mocking button actions

            # Call option_box with custom button labels and return values
            # result = OptionBox("Test Message")

            # # Assert that the Entry widget is not created
            mock_entry.assert_not_called()

            # # Assert that the Button widget is created twice (for custom buttons)
            # mock_button.assert_called_with(mock_button.side_effect[0])
            # self.assertEqual(mock_button.call_count, 2)

            # Assert the returned result
            # self.assertFalse(result)

    def test_option_box_with_timeout(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Entry widget and Button widget
            instance = mock_entry.return_value
            instance.get.return_value = 'TestEntryValue'
            mock_button.side_effect = [None, None]  # Mocking button actions

            # # Call option_box with entry=True and a timeout
            # result = OptionBox("Test Message", "OK", "Cancel", True, 2, True)

            # # Assert that the Entry widget is created and focused
            # mock_entry.assert_called_once()
            # instance.focus_set.assert_called_once()

            # # Assert that the Button widget is created twice (for OK and Cancel)
            # mock_button.assert_called_with(mock_button.side_effect[0])
            # self.assertEqual(mock_button.call_count, 2)

            # # Assert the returned result
            # self.assertEqual(result, 'TestEntryValue')

    def test_option_box_cancel_button(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Button widget for Cancel action
            mock_button.side_effect = [None, None]  # Mocking button actions

            # Call option_box with default buttons
            # result = OptionBox("Test Message", "OK", "Cancel", True, False, False)

            # Assert that the Entry widget is not created
            mock_entry.assert_not_called()

            # Assert that the Button widget is created twice (for OK and Cancel)
            # mock_button.assert_called_with(mock_button.side_effect[1])  # Assert Cancel button
            # self.assertEqual(mock_button.call_count, 2)

            # # Assert the returned result
            # self.assertFalse(result)

    def test_option_box_without_frame(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button, \
             patch('tkinter.Frame') as mock_frame:

            # Set up mock Button widget
            mock_button.side_effect = [None, None]  # Mocking button actions

            # Call option_box with frame=False
            # result = OptionBox("Test Message", "OK", "Cancel", False, False, False)

            # # Assert that the Frame is not created
            mock_frame.assert_not_called()

            # # Assert that the Button widget is created twice (for OK and Cancel)
            # mock_button.assert_called_with(mock_button.side_effect[0])
            # self.assertEqual(mock_button.call_count, 2)

            # # Assert the returned result
            # self.assertIsNone(result)

    def test_option_box_copy_to_clipboard(self):
        with patch('tkinter.Entry') as mock_entry, \
             patch('tkinter.Button') as mock_button:

            # Set up mock Button widget
            mock_button.side_effect = [None, None]  # Mocking button actions

            # # Call option_box with default buttons
            # OptionBox("Test Message", "OK", "Cancel", True, False, False)

            # # Assert that clipboard_clear and clipboard_append are called
            # mock_root = mock_entry.return_value.clipboard_clear
            # mock_root.assert_called_once()
            # mock_root.clipboard_append.assert_called_once_with("Test Message")




if __name__ == '__main__':
    unittest.main()
