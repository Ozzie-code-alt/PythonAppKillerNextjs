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

frame= Frame(root, width=350, height=350, bg="red")
frame.place(x=480,y=70)


heading = Label(frame, text="Sign In", font=("Arial", 20, "bold"), fg="black", bg="red")

root.mainloop()


