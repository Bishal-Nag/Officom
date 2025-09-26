from tkinter import messagebox
from customtkinter import *
from PIL import Image

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR', 'Please fill all fields')
    elif usernameEntry.get().strip().lower()=='bishal'and passwordEntry.get()=='12345':
        messagebox.showinfo('SUCCESS', 'You are logged in')
        root.destroy()
        import ems
    elif usernameEntry.get().strip().lower()=='sauvik' and passwordEntry.get()=='54321':
        messagebox.showinfo('SUCCESS', 'You are logged in')
        root.destroy()
        import ems
    else:
        messagebox.showerror('ERROR', 'Wrong username or password')

root=CTk()
root.geometry("930x478")
root.resizable(0,0)
root.title("Login Page")
image=CTkImage(Image.open("loginpage.jpg"),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color="white",font=('lemon milk',25,'bold'),text_color="dark blue")
headingLabel.place(x=20,y=100)

usernameEntry=CTkEntry(root,placeholder_text="Name",width=180,bg_color="white",fg_color="white",font=('avenir next',15),text_color="dark blue")
usernameEntry.place(x=100,y=170,)

passwordEntry=CTkEntry(root,placeholder_text="Password",width=180,show='*',bg_color="white",fg_color="white",font=('avenir next',15),text_color="dark blue")
passwordEntry.place(x=100,y=220,)

loginButton=CTkButton(root,text="Login",font=('lemon milk',17),cursor='hand2',command=login,corner_radius=15,bg_color="white")
loginButton.place(x=117,y=300)

root.mainloop()