import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from desktopDbRoutes import insertData


root = tk.Tk()
root.title("Desktop GUI Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

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

#-----------------Login Button-----------------

Button(frame, width=29, pady=7, text="Sign In", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0).place(x=35, y=204)
label =Label(frame, text="Don't have an account?", font=("Microsoft YaHei UI Light", 9), fg="black", bg="white")
label.place(x=75, y=270)

sign_up = Button(frame, text="Sign Up", font=("Microsoft YaHei UI Light", 9), fg="#57a1f8", cursor="hand2", bg="white", border=0)
sign_up.place(x=215, y=270)



root.mainloop()

