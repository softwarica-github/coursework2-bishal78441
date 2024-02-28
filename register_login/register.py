from tkinter import *
import subprocess
import mysql.connector
from tkinter import messagebox
import os
import re
from tkinter import Tk, Canvas, PhotoImage, Label
import bcrypt

class TextSlider:
    def __init__(self, root, text, font, fg_color, bg_color, x, y):
        self.root = root
        self.text = text
        self.font = font
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.setup_slider()

    def setup_slider(self):
        count = 0

        label_text = StringVar()
        label = Label(self.root, textvariable=label_text, font=self.font, fg=self.fg_color, bg=self.bg_color)
        label.place(x=self.x, y=self.y)

        def slider():
            nonlocal count, label
            if count >= len(self.text):
                count = 0
                label_text.set("")
            else:
                label_text.set(self.text[:count + 1])
            count += 1
            label.after(100, slider)

        slider()

class Registrationroot:
    def __init__(self, root):
        self.root = root
        self.backgroundImage = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\image_1.png")
        self.setup_ui()

    def setup_ui(self):
        bg_image = Label(
            self.root,
            image=self.backgroundImage,
            bg="#525561"
        )
        bg_image.place(x=120, y=28)

        canvas = Canvas(bg_image, bg="#272A37", width=480, height=750, highlightthickness=0)
        canvas.place(x=0, y=30)  # Adjust the coordinates to place it at the top-left corner


        # Create text slider
        italic_font = ("ADLaM Display", 18, "bold italic")
        text_slider = TextSlider(canvas, "Your Digital Guardian, Always Vigilant", italic_font, "orange", "#272A37", 5, 30)


        # ================ CREATE ACCOUNT HEADER ====================
        self.createAccount_header = Label(
            bg_image,
            text="Create new account",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        self.createAccount_header.place(x=75, y=121)

        # ================ ALREADY HAVE AN ACCOUNT TEXT ====================
        text = Label(
            bg_image,
            text="Already a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        text.place(x=75, y=187)

        # ================ GO TO LOGIN ====================
        switchLogin = Button(
            bg_image,
            text="Login",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command = self.open_login_page
        )
        switchLogin.place(x=230, y=185, width=50, height=35)

        # ================ First Name Section ====================
        self.firstName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\input_img.png")
        self.firstName_image_Label = Label(
            bg_image,
            image=self.firstName_image,
            bg="#272A37"
        )
        self.firstName_image_Label.place(x=80, y=242)

        firstName_text = Label(
            self.firstName_image_Label,
            text="First name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        firstName_text.place(x=25, y=0)

        self.firstName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\name_icon.png")
        self.firstName_icon_Label = Label(
            self.firstName_image_Label,
            image=self.firstName_icon,
            bg="#3D404B"
        )
        self.firstName_icon_Label.place(x=159, y=15)

        self.firstName_entry = Entry(
            self.firstName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.firstName_entry.place(x=8, y=17, width=140, height=27)


        # ================ Last Name Section ====================
        self.lastName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\input_img.png")
        self.lastName_image_Label = Label(
            bg_image,
            image=self.lastName_image,
            bg="#272A37"
        )
        self.lastName_image_Label.place(x=293, y=242)

        lastName_text = Label(
            self.lastName_image_Label,
            text="Last name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        lastName_text.place(x=25, y=0)

        self.lastName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\name_icon.png")
        self.lastName_icon_Label = Label(
            self.lastName_image_Label,
            image=self.lastName_icon,
            bg="#3D404B"
        )
        self.lastName_icon_Label.place(x=159, y=15)

        self.lastName_entry = Entry(
            self.lastName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.lastName_entry.place(x=8, y=17, width=140, height=27)

        # ================ Email Name Section ====================
        self.emailName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\email.png")
        self.emailName_image_Label = Label(
            bg_image,
            image=self.emailName_image,
            bg="#272A37"
        )
        self.emailName_image_Label.place(x=80, y=311)

        emailName_text = Label(
            self.emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        emailName_text.place(x=25, y=0)

        self.emailName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\email-icon.png")
        self.emailName_icon_Label = Label(
            self.emailName_image_Label,
            image=self.emailName_icon,
            bg="#3D404B"
        )
        self.emailName_icon_Label.place(x=370, y=15)

        self.emailName_entry = Entry(
            self.emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.emailName_entry.place(x=8, y=17, width=354, height=27)


        # ================ Password Name Section ====================
        self.passwordName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\input_img.png")
        self.passwordName_image_Label = Label(
            bg_image,
            image=self.passwordName_image,
            bg="#272A37"
        )
        self.passwordName_image_Label.place(x=80, y=380)

        self.passwordName_text = Label(
            self.passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.passwordName_text.place(x=25, y=0)

        self.passwordName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\pass-icon.png")
        self.passwordName_icon_Label = Label(
            self.passwordName_image_Label,
            image=self.passwordName_icon,
            bg="#3D404B"
        )
        self.passwordName_icon_Label.place(x=159, y=15)

        self.passwordName_entry = Entry(
            self.passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.passwordName_entry.place(x=8, y=17, width=140, height=27)


        # ================ Confirm Password Name Section ====================
        self.confirm_passwordName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\input_img.png")
        self.confirm_passwordName_image_Label = Label(
            bg_image,
            image=self.confirm_passwordName_image,
            bg="#272A37"
        )
        self.confirm_passwordName_image_Label.place(x=293, y=380)

        self.confirm_passwordName_text = Label(
            self.confirm_passwordName_image_Label,
            text="Confirm Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.confirm_passwordName_text.place(x=25, y=0)

        self.confirm_passwordName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\pass-icon.png")
        self.confirm_passwordName_icon_Label = Label(
            self.confirm_passwordName_image_Label,
            image=self.confirm_passwordName_icon,
            bg="#3D404B"
        )
        self.confirm_passwordName_icon_Label.place(x=159, y=15)

        self.confirm_passwordName_entry = Entry(
        self.confirm_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)



        # =============== Submit Button ====================
        self.submit_buttonImage = PhotoImage(
            file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\button_1.png")
        self.submit_button = Button(
            bg_image,
            image=self.submit_buttonImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=self.insert_data
        )
        self.submit_button.place(x=130, y=460, width=333, height=65)

        headerText3 = Label(
        bg_image,
        text="Powered by ShieldXpert",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
        )
        headerText3.place(x=700, y=530)


    def open_login_page(self):
        self.root.withdraw()
        subprocess.Popen(['python', r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\login.py'], shell=True)

    def clear_form(self):
        self.firstName_entry.delete(0, 'end')
        self.lastName_entry.delete(0, 'end')
        self.emailName_entry.delete(0, 'end')
        self.passwordName_entry.delete(0, 'end')
        self.confirm_passwordName_entry.delete(0, 'end')  # Fix the variable name

        # Optionally set focus to the first field after clearing
        self.firstName_entry.focus()

    def validate_password(self, password):
    # Minimum length check
        if len(password) < 8:
            return False

        # Regex pattern for password format:
        # At least one uppercase, one lowercase, one digit, and one symbol
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+=-]).{8,}$"

        # Check if the password matches the pattern
        if re.match(pattern, password):
            return True
        else:
            return False

    def insert_data(self):
        # Retrieve data from Tkinter entries
        first_name = self.firstName_entry.get()
        last_name = self.lastName_entry.get()
        email = self.emailName_entry.get()
        password = self.passwordName_entry.get()
        confirm_password = self.confirm_passwordName_entry.get()

        # Check if password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")
            return

        # Ensure username contains only alphabets
        if password != confirm_password:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")
            return

        # Ensure email is in proper format
        if "@" not in email or "." not in email:
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        # Validate password format
        if not self.validate_password(password):
            messagebox.showerror("Invalid Password", "Password must contain letters, a number, and a symbol.")
            return

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="antivirus"
        )

        mycursor = mydb.cursor()

        # Check if email already exists in the database
        check_existing_email = "SELECT * FROM users WHERE email = %s"
        mycursor.execute(check_existing_email, (email,))
        existing_email = mycursor.fetchone()

        if existing_email:
            messagebox.showerror("Duplicate Entry", "User with this email already exists.")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Check if username already exists in the database
        check_existing_username = "SELECT * FROM users WHERE firstname = %s AND lastname = %s"
        mycursor.execute(check_existing_username, (first_name, last_name))
        existing_username = mycursor.fetchone()

        if existing_username:
            messagebox.showerror("Duplicate Entry", "User with this username already exists.")
            return

        # Insert data into the 'users' table
        sql = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
        val = (first_name, last_name, email, hashed_password.decode('utf-8'))  # Decode the bytes to string

        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "User registered successfully.")

        mycursor.close()
        mydb.close()
        self.clear_form()

    # Assign the insert_data function to the submit button
    # Assign the insert_data method to the submit button
        self.submit_button.config(command=self.insert_data)

# registration_root = Registrationroot(root)


if __name__ == "__main__":
    height = 650
    width = 1240
    root = Tk()

    root.geometry('{}x{}+{}+{}'.format(width, height, (root.winfo_screenwidth() // 2) - (width // 2), (root.winfo_screenheight() // 4) - (height // 4)))
    root.resizable(True, True)
    root.configure(bg="#525561")

    registration_root = Registrationroot(root)

    root.mainloop()
