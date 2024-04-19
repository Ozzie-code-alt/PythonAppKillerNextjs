import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from desktopDbRoutes import insertData
import subprocess

proccess = subprocess.Popen(['C:\\Users\\Justin Santos\\Desktop\\Git_Container\\PythonAppKillerNextjs\\Desktop\\venv\\Scripts\\python.exe', 'backend.py'])

def on_close():
    proccess.kill()  # Kill the subprocess
    root.destroy()

root = tk.Tk()
root.title("Desktop GUI Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)
#MARK:Backend Subprocess must me configured to run the backend.py file
image = Image.open("assets/LoginImage.png")
resizedImage = image.resize((450, 300))
img = ImageTk.PhotoImage(resizedImage)
Label(root, image=img).place(x=20, y=70)

frame= Frame(root, width=350, height=350, bg="white")
frame.place(x=480,y=70)


heading = Label(frame, text="Sign In", font=("Microsoft YaHei UI Light", 23, "bold"), fg="#57a1f8", bg="white")
heading.place(x=100, y=5)

#-----------------Username-----------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name= user.get()
    if name == "":
        user.insert(0, 'Username')

user = Entry(frame, width=56, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=0)
user.place(x=30, y=80)
user.insert(0, 'Username')
#-----------------Username Hover-----------------
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

#-----------------Password-----------------
code = Entry(frame, width=56, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=0)
code.place(x=30, y=150)
code.insert(0, 'Password')

#-----------------Password Hover-----------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name= code.get()
    if name == "":
        code.insert(0, 'Password')

        
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)








def openChrome():
    subprocess.Popen(['C:\\Users\\Justin Santos\\Desktop\\Git_Container\\PythonAppKillerNextjs\\Desktop\\venv\\Scripts\\python.exe', 'LocalBrowser.py'])

#-----------------Login Main Window----------------- MARK:MainWindow

def MainWindow():
    root.destroy()
    window = tk.Tk()  # Use Toplevel instead of Tk() here
    window.title("Desktop GUI and Tracker")
    window.geometry("925x500+300+200")
    Label(window, text="Welcome to Desktop GUI and Tracker", font=("Microsoft YaHei UI Light", 23, "bold"), fg="#57a1f8", bg="white").pack()
   # This is Processes Button
    Button(window, text="Send Runnning Processes to Backend", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=insertData).pack()
   # this is Chrome Button
    Button(window, text="Open Chrome Browser", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=openChrome).pack()
    window.mainloop()


#-----------------Login Button-----------------

Button(frame,  width=29, pady=7, text="Sign In", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=MainWindow).place(x=35, y=204)
label =Label(frame, text="Don't have an account?", font=("Microsoft YaHei UI Light", 9), fg="black", bg="white")
label.place(x=75, y=270)

sign_up = Button(frame, text="Sign Up", font=("Microsoft YaHei UI Light", 9), fg="#57a1f8", cursor="hand2", bg="white", border=0)
sign_up.place(x=215, y=270)

root.mainloop()
