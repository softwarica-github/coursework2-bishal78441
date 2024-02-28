# Project           : ShieldXpert 
# Author            : Laxmi Timsina
# Tester and Helper : MySelf
# Version           : 1.0 Main Release 

import mysql.connector
     

try:
    from datetime import date
    from tkinter import *
    import tkinter as tk                
    from tkinter import font as tkfont  
    import subprocess
except ImportError:
    from datetime import date
    from Tkinter import *
    import Tkinter as tk    
    import tkFont as tkfont  


#Import Variable
from all_paths import icon_path
from all_paths import Picture_path


import random
time = random.randint(100, 180)
percentage_c = random.randint(1, 100)
#Link
import webbrowser
def callback(url):
    webbrowser.open_new(url)

#Import path
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path

#Import file
with open(purchase_file_path, 'r') as file:
    pur_date = file.read().rstrip('\n')

with open(username_file_path, 'r') as file:
    username = file.read().rstrip('\n')

with open(password_file_path, 'r') as file:
    password = file.read().rstrip('\n')

with open(email_file_path, 'r') as file:
    email = file.read().rstrip('\n')
short_email = email.split("@")

First_name = username.split(" ")[0]
Last_name = username.split(" ")[-1]
class Kilo_Antivirus(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

         #Icon
        photo = PhotoImage(file = icon_path)
        self.iconphoto(False, photo)
        self.resizable(False, False)
        self.geometry("862x519")
        self.configure(bg = "#3A59C7")
        self.title("ShieldXpert Morden Antivirus")
        #self.resizable(False, False)
        self.title_font = tkfont.Font(family='Cursive', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
    
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, minsize=500, weight=1)
        container.grid_columnconfigure(0, minsize=866, weight=1)
        container.grid_columnconfigure(1, weight=1)


        self.frames = {}
        for F in (Feedback, Home, Scan, Settings, Scan_Utility):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        import datetime 
        from datetime import date  
        date_time_obj = datetime.datetime.strptime(pur_date, '%d-%m-%Y').date()
        main_date = date_time_obj + datetime.timedelta(days=365)
        
        remaining_days = (main_date - date.today()).days
      
        from pathlib import Path

        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_settings")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)



        canvas = Canvas(
            self,
            bg = "#3A59C7",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            283.0,
            0.0,
            862.0,
            519.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_1.place(
            x=49.0,
            y=112.0,
            width=213.0,
            height=54.0
        )

        self.button_1.photo = button_image_1

        self.button_1.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_2.place(
            x=49.0,
            y=166.0,
            width=185.86956787109375,
            height=55.0
        )

        self.button_2.photo = button_image_2

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        self.button_3.place(
            x=42.0,
            y=222.0,
            width=213.0,
            height=54.0
        )

        self.button_3.photo = button_image_3

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=49.0,
            y=282.0,
            width=197.0,
            height=44.0
        )
        self.button_4.bind("<Button-1>", lambda e: callback("http://localhost/site1/index.html"))
        self.button_4.photo = button_image_4

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=57.0,
            y=338.0,
            width=197.0,
            height=44.0
        )

        self.button_5.photo = button_image_5

        self.button_5.bind("<Button-1>", lambda e: callback("http://localhost/emails.html"))
        
        canvas.create_text(
            20.0,
            3.0,
            anchor="nw",
            text="ShieldXpert  Menu",
            fill="#FFFFFF",
            font=("ComicSans", 30 * -1)
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        self.button_6.place(
            x=49.0,
            y=422.0,
            width=180.0,
            height=55.0
        )

        self.button_6.photo = button_image_6
        
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_7.place(
            x=642.0,
            y=432.0,
            width=180.0,
            height=55.0
        )

        self.button_7.photo = button_image_7
        self.button_7.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        self.button_8.place(
            x=49.0,
            y=50.0,
            width=180.0,
            height=55.0
        )

        self.button_8.photo = button_image_8

        canvas.create_rectangle(
            307.0,
            42.0,
            539.0,
            84.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            585.0,
            42.0,
            817.0,
            84.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            585.0,
            101.0,
            817.0,
            143.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            307.0,
            102.0,
            539.0,
            144.0,
            fill="#41D147",
            outline="")

        canvas.create_text(
            420.0,
            114.0,
            anchor="nw",
            text=Last_name,
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            662.0,
            52.0,
            anchor="nw",
            text=" "+str(date.today()),
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            759.0,
            114.0,
            anchor="nw",
            text=remaining_days,
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_rectangle(
            307.0,
            162.0,
            539.0,
            204.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            307.0,
            222.0,
            539.0,
            272.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            307.0,
            290.0,
            559.0,
            340.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            307.0,
            358.0,
            539.0,
            408.0,
            fill="#41D147",
            outline="")

        canvas.create_rectangle(
            307.0,
            437.0,
            539.0,
            487.0,
            fill="#41D147",
            outline="")

        canvas.create_text(
            312.0,
            50.0,
            anchor="nw",
            text="Name : ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            609.0,
            50.0,
            anchor="nw",
            text="Date :",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            609.0,
            113.0,
            anchor="nw",
            text="Remaining Days: ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            113.0,
            anchor="nw",
            text="Last Name : ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            170.0,
            anchor="nw",
            text="Password : ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            411.0,
            171.0,
            anchor="nw",
            text=" "+password,
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )
        
        canvas.create_text(
            377.0,
            233.0,
            anchor="nw",
            text=short_email[0],
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            450.0,
            302.0,
            anchor="nw",
            text=" "+pur_date,
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            459.0,
            451.0,
            anchor="nw",
            text="1.2",
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            459.0,
            369.0,
            anchor="nw",
            text=" 1.01",
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            233.0,
            anchor="nw",
            text="Email : ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            301.0,
            anchor="nw",
            text="Purchase Date : ",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            369.0,
            anchor="nw",
            text="Antivirus Version:",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            312.0,
            450.0,
            anchor="nw",
            text="Installer Version:",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            386.0,
            52.0,
            anchor="nw",
            text=First_name,
            fill="#FFFFFF",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            517.0,
            1.0,
            anchor="nw",
            text="Settings",
            fill="#000000",
            font=("Amaranth BoldItalic", 30 * -1)
        )

        

class Scan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        from pathlib import Path

        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_scan")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        canvas = Canvas(
            self,
            bg = "#3A59C7",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            283.0,
            0.0,
            862.0,
            519.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        self.button_1.place(
            x=49.0,
            y=112.0,
            width=213.0,
            height=54.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        self.button_2.place(
            x=58.0,
            y=174.0,
            width=197.0,
            height=44.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        self.button_3.place(
            x=59.0,
            y=228.0,
            width=197.0,
            height=44.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=54.0,
            y=279.0,
            width=192.0,
            height=55.0
        )
        self.button_4.bind("<Button-1>", lambda e: callback("http://localhost/site1/index.html"))


        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_5.place(
            x=57.0,
            y=338.0,
            width=197.0,
            height=44.0
        )
        self.button_5.bind("<Button-1>", lambda e: callback("http://localhost/emails.html"))


        canvas.create_text(
            20.0,
            3.0,
            anchor="nw",
            text="ShieldXpert  Menu",
            fill="#FFFFFF",
            font=("ComicSans", 30 * -1)
        )

        """button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=49.0,
            y=422.0,
            width=180.0,
            height=55.0
        )"""

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Your version is not premium version"),
            relief="flat"
        )
        self.button_7.place(
            x=640.0,
            y=110.0,
            width=195.0,
            height=69.91525268554688
        )
        def run_script():
            subprocess.Popen(["python", r"C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\Antivirusmaster\GUI.py"])
            # root = tk.Tk()

        def on_button_click():
            run_script()

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_click,
            relief="flat"
        )           
        self.button_8.place(
            x=580.0,
            y=224.0,
            width=195.0,
            height=69.91525268554688
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(
            canvas,
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Your version is not premium version"),
            relief="flat"
        )
        self.button_9.place(
            x=355.0,
            y=225.0,
            width=195.0,
            height=69.91525268554688
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_10 = Button(
            canvas,
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Scan_Utility"),
            relief="flat"
        )
        self.button_10.place(
            x=311.0,
            y=110.0,
            width=195.0,
            height=69.91525268554688
        )


        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(
            canvas,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        self.button_12.place(
            x=30.0,
            y=50.0,
            width=180.0,
            height=55.0
        )

        canvas.create_text(
            542.0,
            2.0,
            anchor="nw",
            text="Scan",
            fill="#000000",
            font=("Amaranth BoldItalic", 30 * -1)
        )

        canvas.create_text(
            311.0,
            427.0,
            anchor="nw",
            text="Get Premium to Enable : \n{Web Protection}, {Simple Update}",
            fill="#DB00FF",
            font=("Amaranth Regular", 19 * -1)
        )

        canvas.create_text(
            323.0,
            50.0,
            anchor="nw",
            text="Premium will be free forever. You just need to click button.",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )
        self.button_1.photo = button_image_1
        self.button_2.photo = button_image_2
        self.button_3.photo = button_image_3
        self.button_4.photo = button_image_4
        self.button_5.photo = button_image_5
        self.button_7.photo = button_image_7
        self.button_8.photo = button_image_8
        self.button_9.photo = button_image_9
        self.button_10.photo = button_image_10
        self.button_12.photo = button_image_12
        
        
        
        self.button_1.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))
        

        


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       
        
        # Definations
        

        from pathlib import Path

        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_home")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        
        

        canvas = Canvas(
            self,
            bg = "#3A59C7",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            
            283.0,
            0.0,
            862.0,
            519.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=57.0,
            y=119.0,
            width=197.0,
            height=44.0
        )
        self.button_1.photo = button_image_1
        self.button_1.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        self.button_2.place(
            x=54.0,
            y=178.0,
            width=197.0,
            height=44.0
        )
        self.button_2.photo = button_image_2

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        self.button_3.place(
            x=42.0,
            y=222.0,
            width=213.0,
            height=54.0
        )

        self.button_3.photo = button_image_3

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))

        self.button_4 = Button(
            canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=49.0,
            y=282.0,
            width=197.0,
            height=44.0
        )
        
        self.button_4.bind("<Button-1>", lambda e: callback("http://localhost/site1/index.html"))

        self.button_4.photo = button_image_4

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_5.place(
            x=57.0,
            y=338.0,
            width=197.0,
            height=44.0
        )

        self.button_5.bind("<Button-1>", lambda e: callback("http://localhost/emails.html"))

        self.button_5.photo = button_image_5

        canvas.create_text(
            20.0,
            3.0,
            anchor="nw",
            text="ShieldXpert Menu",
            fill="#FFFFFF",
            font=("ComicSans", 30 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            581.0,
            253.0,
            image=image_image_1
        )
        canvas.photo = image_image_1
        
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            canvas,
            
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        self.button_6.place(
            x=49.0,
            y=422.0,
            width=180.0,
            height=55.0
        )

        self.button_6.photo = button_image_6

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Requeset has been sent to adminstrator"),
            relief="flat"
        )
        self.button_7.place(
            x=750.0,
            y=412.0,
            width=95.0,
            height=38.0
        )
        
        self.button_7.photo = button_image_7

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("You are on same page"),
            relief="flat"
        )
        self.button_8.place(
            x=49.0,
            y=58.0,
            width=180.0,
            height=55.0
        )

        self.button_8.photo = button_image_8

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            740.0,
            470.5,
            image=entry_image_1
        )

        

        entry_1 = Entry(
            canvas,
            bd=0,
            bg="#B9FA2F",
            highlightthickness=0
        )
        entry_1.place(
            x=648.0,
            y=450.0,
            width=184.0,
            height=39.0
        )

        entry_1.photo = entry_image_1


        
        

class Scan_Utility(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        if hasattr(controller, 'title_font') and controller.title_font:
            label = tk.Label(self, text="Scan Utility", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
        else:
            label = tk.Label(self, text="Scan Utility")
            label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))

        from tkinter import ttk
        from tkinter.messagebox import showinfo


        from pathlib import Path

        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_scan")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        canvas = Canvas(
            self,
            bg = "#3A59C7",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            283.0,
            0.0,
            862.0,
            519.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            
            relief="flat"
        )
        button_1.place(
            x=49.0,
            y=112.0,
            width=213.0,
            height=54.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        self.button_2.place(
            x=58.0,
            y=174.0,
            width=197.0,
            height=44.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        self.button_3.place(
            x=59.0,
            y=228.0,
            width=197.0,
            height=44.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=54.0,
            y=279.0,
            width=192.0,
            height=55.0
        )

        self.button_4.bind("<Button-1>", lambda e: callback("http://localhost/site1/index.html"))


        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_5.place(
            x=57.0,
            y=338.0,
            width=197.0,
            height=44.0
        )
        self.button_5.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))


        canvas.create_text(
            20.0,
            3.0,
            anchor="nw",
            text="ShieldXpert Menu",
            fill="#FFFFFF",
            font=("ComicSans", 30 * -1)
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        self.button_6.place(
            x=49.0,
            y=422.0,
            width=180.0,
            height=55.0
        )


        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(
            canvas,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        self.button_12.place(
            x=49.0,
            y=50.0,
            width=180.0,
            height=55.0
        )

        canvas.create_text(
            542.0,
            2.0,
            anchor="nw",
            text="Scan",
            fill="#000000",
            font=("Amaranth BoldItalic", 30 * -1)
        )

        canvas.create_text(
            311.0,
            427.0,
            anchor="nw",
            text="Get Premium to Enable : \n{Web Protection}, {Simple Update}",
            fill="#DB00FF",
            font=("Amaranth Regular", 19 * -1)
        )

        canvas.create_text(
            323.0,
            50.0,
            anchor="nw",
            text="Premium will be free forever. You just need to click button.",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        


        button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        self.button_14 = Button(
            canvas,
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clear(),
            relief="flat"
        )
        self.button_14.place(
            x=730.0,
            y=430.0,
            width=112.0,
            height=54.0
        )

        button_1.photo = button_image_1
        self.button_2.photo = button_image_2
        self.button_3.photo = button_image_3
        self.button_4.photo = button_image_4
        self.button_5.photo = button_image_5
        self.button_6.photo = button_image_6
        self.button_12.photo = button_image_12
        self.button_14.photo = button_image_14


    
        

        
        
        
        button_1.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))





    
        button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        self.button_13 = Button(
            canvas,
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: start_scan(self),
            relief="flat"
        )
        self.button_13.place(
            x=475.0,
            y=80.0,
            width=195.0,
            height=69.91525268554688
        )

        self.button_13.photo = button_image_13

        def start_scan(self):  
            
            def update_progress_label():
                return f"Scanning Progress: {self.pb['value']}%"

            self.pb = ttk.Progressbar(
                self,
                orient='horizontal',
                mode='determinate',
                length=280
            )
            # place the progressbar
            self.pb.place(x=430,y=160)

            # label
            self.value_label = ttk.Label(self, text=update_progress_label())
            self.value_label.place(x=500,y=190)

            
            
            self.percentage = 0
            
            self.load_bar()
        


    def load_bar(self):
        pb = self.pb 
        value_label = self.value_label 

        
        
        def update_progress_label():
            return f"Current Progress: {pb['value']}%"

        pb['value'] += 2
        value_label['text'] = update_progress_label()

        self.percentage +=2 #Edit 2
        

        if self.percentage == 100 and pb['value'] == 100:
            

            # importing required packages 
            import tkinter 
            from PIL import ImageTk, Image 
            import os 

            # creating main self 
            

            # loading the image 
            img = ImageTk.PhotoImage(Image.open(Picture_path)) 

            # reading the image 
            self.panel = tkinter.Label(self, image = img) 

            # setting the application 
            self.panel.place(x=380,y=210)

            
            value_label['text'] = update_progress_label()

            from tkinter import messagebox
            messagebox.showinfo("Congratulations", "Scanned succesfully and Not even a single virus found!")

            # running the application 
            self.mainloop()


            return
        
        else:
            
            self.after(percentage_c,self.load_bar)  # Edit 100

    
    def clear(self):
        try:
            self.panel.destroy()
            self.pb.destroy()
            self.value_label.destroy()
            from tkinter import messagebox
            messagebox.showinfo("Congratulations", "Cleared Succeessfully.")
        
        except:
            from tkinter import messagebox
            messagebox.showerror("Clearing error", "Please first Scan and then press Clear button.")
        

         
                            

        

        


class Feedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Feed Back", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        #String
        def clear_entries():
            entry_2.delete(0, tk.END)  # Clear user_name entry
            entry_3.delete(0, tk.END)  # Clear feedback_subject entry
            entry_1.delete('1.0', tk.END)
                
        #Sumbit Button
        def submit():
            # Get feedback data from Tkinter entry widgets
            user_name = entry_2.get()
            feedback_subject = entry_3.get()
            feedback_text = entry_1.get('1.0', 'end')

        # Replace the placeholder values with your actual database credentials
            host = 'localhost'
            user = 'root'
            password = ''
            database = 'antivirus'

            try:
                # Connect to the MySQL server
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="antivirus"
                )

                if conn.is_connected():
                    print(f"Connected to MySQL database '{database}'")

                    # Create a cursor to execute SQL statements
                    cursor = conn.cursor()

                    # Use placeholders in the SQL statement
                    sql_insert = '''
                        INSERT INTO feedback (Name, Subject, Feedback)
                        VALUES (%s, %s, %s)
                    '''
                    # Execute the SQL statement with actual values
                    cursor.execute(sql_insert, (user_name, feedback_subject, feedback_text))

                    # Commit the changes
                    conn.commit()
                    clear_entries()

            except mysql.connector.Error as e:
                print(f"Error: {e}")

            finally:
                # Close the database connection when done
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()
                    print("MySQL connection closed")




        from pathlib import Path

        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_feedback")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)



        canvas = Canvas(
            self,
            bg = "#3A59C7",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            283.0,
            0.0,
            862.0,
            519.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(
            x=49.0,
            y=112.0,
            width=213.0,
            height=54.0
        )
        
        button_1.photo = button_image_1

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        self.button_2.place(
            x=58.0,
            y=174.0,
            width=197.0,
            height=44.0
        )

        self.button_2.photo = button_image_2

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        self.button_3.place(
            x=54.0,
            y=218.0,
            width=192.0,
            height=55.0
        )

        self.button_3.photo = button_image_3

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=49.0,
            y=282.0,
            width=197.0,
            height=44.0
        )
        self.button_4.bind("<Button-1>", lambda e: callback("http://localhost/site1/index.html"))


        self.button_4.photo = button_image_4

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_5.place(
            x=57.0,
            y=338.0,
            width=197.0,
            height=44.0
        )

        self.button_5.bind("<Button-1>", lambda e: callback("http://localhost/emails.html"))
        self.button_5.photo = button_image_5

        canvas.create_text(
            20.0,
            3.0,
            anchor="nw",
            text="ShieldXpert Menu",
            fill="#FFFFFF",
            font=("ComicSans", 30 * -1)
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        self.button_6.place(
            x=49.0,
            y=422.0,
            width=180.0,
            height=55.0
        )

        self.button_6.photo = button_image_6

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: submit(),
            relief="flat"
        )
        self.button_7.place(
            x=642.0,
            y=449.0,
            width=180.0,
            height=55.0
        )

        self.button_7.photo = button_image_7

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        self.button_8.place(
            x=49.0,
            y=50.0,
            width=180.0,
            height=55.0
        )

        self.button_8.photo = button_image_8

        
        canvas.create_text(
            510.0,
            2.0,
            anchor="nw",
            text="Feedback",
            fill="#000000",
            font=("Amaranth BoldItalic", 30 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            
            570.0,
            324.5,
            image=entry_image_1
        )
        entry_1 = Text(
            canvas,
            bd=0,
            bg="#C4C4C4",
            highlightthickness=0
        )
        entry_1.photo = entry_image_1

        entry_1.place(
            x=330.0,
            y=213.0,
            width=480.0,
            height=221.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            447.5,
            90.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            canvas,
            bd=0,
            bg="#C4C4C4",
            highlightthickness=0
        )
        entry_2.place(
            x=330.0,
            y=69.0,
            width=235.0,
            height=41.0
        )

        entry_2.photo = entry_image_2

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            447.5,
            164.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            canvas,
            bd=0,
            bg="#C4C4C4",
            highlightthickness=0
        )
        entry_3.place(
            x=330.0,
            y=143.0,
            width=235.0,
            height=41.0
        )

        entry_3.photo = entry_image_3

        canvas.create_text(
            321.0,
            35.0,
            anchor="nw",
            text="Name :",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            321.0,
            114.0,
            anchor="nw",
            text="Subject :",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        canvas.create_text(
            321.0,
            187.0,
            anchor="nw",
            text="Feedback :",
            fill="#000000",
            font=("Amaranth Regular", 20 * -1)
        )

        button_1.bind("<Button-1>", lambda e: callback("https://github.com/bishal78441"))
        



        
    
if __name__ == "__main__":
    app = Kilo_Antivirus()
    app.mainloop()
