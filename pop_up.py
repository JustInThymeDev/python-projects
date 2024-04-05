import customtkinter as ctk
import tkinter.messagebox as tkmb
import pandas as pd
import csv
from csv import writer
app = ctk.CTk()
app2 = ctk.CTk()
width= app.winfo_screenwidth()
height= app.winfo_screenheight()
app.geometry("%dx%d" % (width/2, height/2))
app2.geometry("%dx%d" % (width/2, height/2))
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")
app.title("User Login")
app2.title("New User")

def info_scraper(first_name, last_name, username_conf, user_pass_in, user_pass_conf):
    headerList = ['First Name', 'Last Name', 'User Name', 'User Password']
    db=pd.read_csv("User_Login_Info.csv", usecols=['User Name'])
    users=db['User Name'].tolist()
    if user_pass_in.get() != user_pass_conf.get():
        tkmb.showwarning(title=" ", message="Passwords do not match.")
    #if user_pass_conf.get()
    if username_conf.get() in users:
        tkmb.showwarning(title=" ", message="Username already taken.")
    elif (username_conf not in db) and (user_pass_in.get() == user_pass_conf.get()):
        with open("User_Login_Info.csv", 'a', newline='') as f:
            writer_obj= writer(f)
            writer_obj.writerow([str(first_name.get()), str(last_name.get()), str(username_conf.get()), str(user_pass_conf.get())])
            f.close()
def login():
    db=pd.read_csv("User_Login_Info.csv", usecols=['User Name', 'User Password'])
    users=db['User Name'].tolist()
    password=db['User Password'].tolist()
    print(users, password)
    print(users.index(user_entry.get()))
    print(password.index(str(user_pass.get())))
    if (user_entry.get() in users) and (user_pass.get() in password) and (users.index(user_entry.get()) == password.index(user_pass.get())):
        tkmb.showinfo(title=" ", message="Login Successful")

    elif (user_entry.get() not in users) or (user_pass.get() not in password):
        tkmb.showwarning(title=" ", message="Invalid Username or Password")
    else:
        tkmb.showerror(title=" ", message="Login Failure")
def new_user():
    label2 = ctk.CTkLabel(app, text="Welcome to Jadens TKInter Login System")
    label2.pack(pady=10)

    frame2 = ctk.CTkFrame(master=app2)
    frame2.pack(pady=20, padx=60, fill='both', expand=True)

    label2 = ctk.CTkLabel(master=frame2, text='Please fill out all boxes and click Submit')
    label2.pack(pady=12, padx=10)

    first_name=ctk.CTkEntry(master=frame2, placeholder_text="First Name")
    first_name.pack(pady=12, padx=10)

    last_name=ctk.CTkEntry(master=frame2, placeholder_text="Last Name")
    last_name.pack(pady=12, padx=10)

    username_conf=ctk.CTkEntry(master=frame2, placeholder_text="Username")
    username_conf.pack(pady=12, padx=10)

    user_pass_in=ctk.CTkEntry(master=frame2, placeholder_text="Enter password")
    user_pass_in.pack(pady=12, padx=10)

    user_pass_conf=ctk.CTkEntry(master=frame2, placeholder_text="Confirm password")
    user_pass_conf.pack(pady=12, padx=10)

    button2 = ctk.CTkButton(master=frame2, text="Submit", command=lambda: info_scraper(first_name, last_name, username_conf, user_pass_in, user_pass_conf))
    button2.pack(pady=12, padx=10)

    app2.mainloop()

#TKInter Main Login

label = ctk.CTkLabel(app, text="Welcome to Jadens TKInter Login System")
label.pack(pady=10)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Please Login')
label.pack(pady=12, padx=10)

user_entry=ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass=ctk.CTkEntry(master=frame, placeholder_text="Password")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Create Account", command=new_user)
button.pack(pady=12, padx=10)

checkbox= ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

app.mainloop()
