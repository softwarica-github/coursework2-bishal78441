from tkinter import *
from tkinter.ttk import Progressbar
import os
from PIL import Image, ImageTk

class AntivirusApp:
    def __init__(self, master):
        self.master = master
        height = 430
        width = 530
        x = (self.master.winfo_screenwidth()//2)-(width//2)
        y = (self.master.winfo_screenheight()//2)-(height//2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.overrideredirect(1)
        #self.master.wm_attributes('-alpha', 0.9)
        self.master.wm_attributes('-topmost', True)
        self.master.config(background='#90EE90')


        self.create_widgets()

    def create_widgets(self):
        self.load_image()

        self.welcome_label = Label(text='WELCOME TO MODERN ANTIVIRUS(ShieldXpert)', bg='#90EE90',
                                   font=("yu gothic ui", 13, "bold"), fg='black')
        self.welcome_label.place(x=65, y=10)

        self.bg_label = Label(self.master, image=self.image, bg='#90EE90')
        self.bg_label.place(x=130, y=65)

        self.progress_label = Label(self.master, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='black',
                                    bg='#90EE90')
        self.progress_label.place(x=190, y=350)

        self.progress = Progressbar(self.master, orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=15, y=390)

        self.exit_btn = Button(text='x', bg='#90EE90', command=self.exit_window, bd=0,
                               font=("yu gothic ui", 16, "bold"), activebackground='#90EE90', fg='white')
        self.exit_btn.place(x=490, y=0)

        self.i = 0

        self.load()

    def load_image(self):
        image_path = r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\register_login\assets\headerText_imageq.png'
        original_image = Image.open(image_path)
        resized_image = original_image.resize((275, 200), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(resized_image)

    def exit_window(self):
        self.master.destroy()

    def top(self):
        self.master.withdraw()
        os.system("python ShieldXpert_Main.py")
        self.master.destroy()

    def load(self):
        if self.i <= 10:
            txt = 'Please Wait...  ' + (str(10 * self.i) + '%')
            self.progress_label.config(text=txt)
            self.progress_label.after(1000, self.load)
            self.progress['value'] = 10 * self.i
            self.i += 1
        else:
            self.top()

def main():
    root = Tk()
    app = AntivirusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
