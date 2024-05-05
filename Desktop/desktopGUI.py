import tkinter as tk
from tkinter import *
from pymongo import MongoClient 
from PIL import Image, ImageTk
from desktopDbRoutes import insertData
import subprocess
from LocalBrowser import initialize_driver, pass_visited_website
#MARK:Backend Subprocess must me configured to run the backend.py file
proccess = subprocess.Popen(['C:\\Users\\Justin Santos\\Desktop\\Git_Container\\PythonAppKillerNextjs\\Desktop\\venv\\Scripts\\python.exe', 'backend.py'])

def on_close():
    proccess.kill()  # Kill the subprocess
    root.destroy()

root = tk.Tk()
root.title("Desktop GUI Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)
# root.protocol("WM_DELETE_WINDOW", on_close)
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


#-----------------Student ID-----------------
stud_id = Entry(frame, width=56, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=0)
stud_id.place(x=30, y=210)
stud_id.insert(0, 'Student ID')
#-----------------Student ID Hover-----------------
def on_enter(e):
    stud_id.delete(0, 'end')

def on_leave(e):
    name= stud_id.get()
    if name == "":
        stud_id.insert(0, 'Student ID')

stud_id.bind("<FocusIn>", on_enter)
stud_id.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=237)

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




def errorMessagePopup():
    root = tk.Tk()
    root.title("Error")
    root.geometry("300x100")
    root.configure(bg="#fff")
    root.resizable(False, False)
    Label(root, text="Please enter both username and password", font=("Microsoft YaHei UI Bold", 20), fg="red", bg="white",).pack()
    root.mainloop()




def openChrome():
    # subprocess.Popen(['C:\\Users\\Justin Santos\\Desktop\\Git_Container\\PythonAppKillerNextjs\\Desktop\\venv\\Scripts\\python.exe', 'LocalBrowser.py'])
    driver = initialize_driver()
    pass_visited_website(driver)
#-----------------Login Main Window----------------- MARK:MainWindow


def OpenProgam():
    window = tk.Tk()  # Use Toplevel instead of Tk() here
    window.title("Desktop GUI and Tracker")
    window.geometry("925x500+300+200")
    Label(window, text="Welcome to Desktop GUI and Tracker", font=("Microsoft YaHei UI Light", 23, "bold"), fg="#57a1f8", bg="white").pack()
   # This is Processes Button
    Button(window, text="Send Runnning Processes to Backend", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=insertData).pack()
   # this is Chrome Button
    Button(window, text="Open Chrome Browser", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=openChrome).pack()
    window.mainloop()






def MainWindow():
    client = MongoClient('mongodb+srv://justin:justin123@cluster0.lhij5pu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    username = user.get()
    password = code.get()
    student_ID = stud_id.get()
    db = client['thesisDb'] # database name this will be created if not present

    databaseCheck = db.accounts.find({"username": username, "password": password , "stud_ID": student_ID})
    databaseConverted = list(databaseCheck)
    print(databaseConverted)
    if len(databaseConverted) != 0:
        root.destroy()
        OpenProgam()
        print("this is database converted", databaseConverted)
        print("YAY iT Worked account is" , username, password, stud_id)
    else:
        print("Error Login Details are incorrect")
        errorMessagePopup()
    client.close()




def signupConnection(username, password, stud_ID):
    client = MongoClient('mongodb+srv://justin:justin123@cluster0.lhij5pu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['thesisDb'] # database name this will be created if not present
    collection = db['accounts'] # collection name
    document = {"username" : username, "password":  password , "stud_ID": stud_ID }
    try:
        collection.insert_one(document)
        print("Inserted Document Success", )
    except Exception as e:
        print("Error inserting document: ", e)
    client.close()
    


def signUpPop():
    root = tk.Tk()
    root.title("Sign Up")
    root.geometry("300x300")
    root.configure(bg="#fff")
    root.resizable(False, False)
    Label(root, text="Sign Up",  font=("Microsoft YaHei UI Light", 23, "bold"), fg="#57a1f8", bg="white").pack()



    Label(root, text="Username", font=("Microsoft YaHei UI Light", 11), fg="black", bg="white").pack()
    # Create the username entry widget and pack it separately
    username_entry = Entry(root, width=20, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=1)
    username_entry.pack()
    
    Label(root, text="Student ID", font=("Microsoft YaHei UI Light", 11), fg="black", bg="white").pack()
    # Create the username entry widget and pack it separately
    stud_ID_entry = Entry(root, width=20, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=1)
    stud_ID_entry.pack()
    
    Label(root, text="Password", font=("Microsoft YaHei UI Light", 11), fg="black", bg="white").pack()

    # Create the password entry widget and pack it separately
    password_entry = Entry(root, width=20, font=("Microsoft YaHei UI Light", 11), bg="white", fg="black", border=1)
    password_entry.pack()

    def passSignUp():
        passUsername = username_entry.get()
        passPassword = password_entry.get()
        passStudID = stud_ID_entry.get()
        signupConnection(passUsername, passPassword, passStudID)
        root.destroy()
 
    Button(root, text="Sign Up", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=passSignUp).pack()
    root.mainloop() 


#-----------------Login Button-----------------

Button(frame,  width=29, pady=7, text="Sign In", font=("Microsoft YaHei UI Light", 11), bg="#57a1f8", fg="white", border=0, command=MainWindow).place(x=35, y=274)
label =Label(frame, text="Don't have an account?", font=("Microsoft YaHei UI Light", 9), fg="black", bg="white")
label.place(x=75, y=320)

sign_up = Button(frame, text="Sign Up", font=("Microsoft YaHei UI Light", 9), fg="#57a1f8", cursor="hand2", bg="white", border=0, command=signUpPop)
sign_up.place(x=215, y=320)

root.mainloop()



