from tkinter import *
import webbrowser
import mysql.connector
from tkinter import messagebox
import os
import subprocess
from tkinter import Tk, Canvas, PhotoImage, Label
from bcrypt import checkpw
import bcrypt

class TextSlider:
    def __init__(self, master, text, font, fg_color, bg_color, x, y):
        self.master = master
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
        label = Label(self.master, textvariable=label_text, font=self.font, fg=self.fg_color, bg=self.bg_color)
        label.place(x=self.x, y=self.y)

        def slider():
            nonlocal count, label
            if count >= len(self.text):
                count = 0
                label_text.set("")
            else:
                label_text.set(self.text[:count + 1])
            count += 1
            self.master.after(100, slider)

        slider()
        

class AntivirusApp:
    def __init__(self):
        self.window = Tk()

        height = 650
        width = 1240
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 4) - (height // 4)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.window.configure(bg="#525561")

        # ================Background Image ====================
        Login_backgroundImage = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\image_1.png")
        self.bg_imageLogin = Label(
            self.window,
            image=Login_backgroundImage,
            bg="#525561"
        )
        self.bg_imageLogin.place(x=120, y=28)




        canvas = Canvas(self.bg_imageLogin, bg="#272A37", width=480, height=750, highlightthickness=0)
        canvas.place(x=0, y=30)  # Adjust the coordinates to place it at the top-left corner


        # Create text slider
        italic_font = ("ADLaM Display", 18, "bold italic")
        text_slider = TextSlider(canvas, "Your Digital Guardian, Always Vigilant", italic_font, "orange", "#272A37", 5, 30)



        # ================ LOGIN TO ACCOUNT HEADER ====================
        loginAccount_header = Label(
            self.bg_imageLogin,
            text="Login to continue",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        loginAccount_header.place(x=75, y=121)

        # ================ NOT A MEMBER TEXT ====================
        loginText = Label(
            self.bg_imageLogin,
            text="Not a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        loginText.place(x=75, y=187)

        # ================ GO TO SIGN UP ====================
        switchSignup = Button(
            self.bg_imageLogin,
            text="Sign Up",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=self.open_signup_page
        )
        switchSignup.place(x=220, y=185, width=70, height=35)

        update_button = Button(
            self.bg_imageLogin,
            text="Update",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=lambda: webbrowser.open_new("https://github.com/bishal78441/ShieldXpert/blob/main/README.md")
        )
        update_button.place(x=300, y=185, width=75, height=35)


         # ================ Email Name Section ====================
        Login_emailName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\email.png")
        self.Login_emailName_image_Label = Label(
            self.bg_imageLogin,
            image=Login_emailName_image,
            bg="#272A37"
        )
        self.Login_emailName_image_Label.place(x=76, y=242)

        Login_emailName_text = Label(
            self.Login_emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        Login_emailName_text.place(x=25, y=0)

        Login_emailName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\email-icon.png")
        Login_emailName_icon_Label = Label(
            self.Login_emailName_image_Label,
            image=Login_emailName_icon,
            bg="#3D404B"
        )
        Login_emailName_icon_Label.place(x=370, y=15)

        self.Login_emailName_entry = Entry(
            self.Login_emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.Login_emailName_entry.place(x=8, y=17, width=354, height=27)

        # ================ Password Name Section ====================
        self.Login_passwordName_image = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\email.png")
        self.Login_passwordName_image_Label = Label(
            self.bg_imageLogin,
            image=self.Login_passwordName_image,
            bg="#272A37"
        )
        self.Login_passwordName_image_Label.place(x=80, y=330)

        self.Login_passwordName_text = Label(
            self.Login_passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.Login_passwordName_text.place(x=25, y=0)

        self.Login_passwordName_icon = PhotoImage(file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\pass-icon.png")
        self.Login_passwordName_icon_Label = Label(
            self.Login_passwordName_image_Label,
            image=self.Login_passwordName_icon,
            bg="#3D404B"
        )
        self.Login_passwordName_icon_Label.place(x=370, y=15)

        self.Login_passwordName_entry = Entry(
            self.Login_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

       # =============== Submit Button ====================
        Login_button_image_1 = PhotoImage(
            file=r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\button_1.png")
        self.Login_button_1 = Button(
            self.bg_imageLogin,
            image=Login_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=self.login  # Assign the login function directly here
        )
        self.Login_button_1.place(x=120, y=445, width=333, height=65)


        Login_headerText3 = Label(
            self.bg_imageLogin,
            text="Powered by ShieldXpert",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        Login_headerText3.place(x=700, y=530)

        # ================ Forgot Password ====================
        forgotPassword = Button(
            self.bg_imageLogin,
            text="Forgot Password",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            activebackground="#272A37",
            activeforeground="#ffffff",
            cursor="hand2",
            command=lambda: self.forgot_password(),
        )
        forgotPassword.place(x=210, y=400, width=150, height=35)


        # Assign the login function to the login button
        self.Login_button_1.config(command=self.login)

        self.window.resizable(True, True)
        self.window.mainloop()

    def open_signup_page(self):
        self.window.withdraw()
        subprocess.Popen(['python', r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\register.py'], shell=True)

    def open_startup(self):
        os.system("python C:\\Users\\asus\\Desktop\\Semester-3rd\\programming_and_algorithium-2\\project\\ShieldXpert-Antivirus\\register_login\\startup.py")

    def update_password(self, email, new_password):
        try:
            # Connect to MySQL
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="antivirus"
            )

            mycursor = mydb.cursor()

            # Hash the new password before storing in the database
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

            # Update the hashed password in the database
            update_query = "UPDATE users SET password = %s WHERE email = %s"
            mycursor.execute(update_query, (hashed_password, email))
            mydb.commit()

            messagebox.showinfo("Password Updated", "Your password has been successfully updated.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update password: {str(e)}")
        finally:
            mycursor.close()
            mydb.close()

    def forgot_password(self):
        def update_password():
            email = email_entry3.get()
            new_password = new_password_entry.get()

            self.update_password(email, new_password)
           

        win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('Forgot Password')
        win.configure(background='#272A37')
        win.resizable(False, False)

        email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
        email_entry3.place(x=40, y=80, width=256, height=50)
        email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
        email_label3.place(x=40, y=50)

        new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1, bd=0)
        new_password_entry.place(x=40, y=180, width=256, height=50)
        new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=150)

        update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                            cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                            command=update_password)  # Set the command to call the update_password function
        update_pass.place(x=40, y=260, width=256, height=45)

    def update_github(self):
        url = 'https://github.com/bishal78441/ShieldXpert/blob/main/README.md'
        webbrowser.open_new(url)
        self.update_github()

    def login(self):
        email = self.Login_emailName_entry.get()
        password = self.Login_passwordName_entry.get()

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="antivirus"
        )

        mycursor = mydb.cursor()

        # Retrieve hashed password from the database
        get_hashed_password_query = "SELECT password FROM users WHERE email = %s"
        mycursor.execute(get_hashed_password_query, (email,))
        hashed_password = mycursor.fetchone()

        if hashed_password:
            hashed_password = hashed_password[0]

            # Check if the entered password matches the hashed password
            if checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                mycursor.close()
                mydb.close()
                self.window.destroy()
                self.open_startup()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials.")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

            mycursor.close()
            mydb.close()

if __name__ == "__main__":
    app = AntivirusApp()
