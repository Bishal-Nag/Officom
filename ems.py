from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

#Functions

def delete_all():
    result=messagebox.askyesno("CONFIRM","Delete all employees?")
    if result:
        database.deleteall_records()
        messagebox.showinfo("SUCCESS", "All employees deleted")
    else:
        messagebox.showinfo("SUCCESS","No employees deleted")

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Select Search')
def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror("ERROR","Please enter employee details")
    elif searchBox.get()=='Select Search':
        messagebox.showerror("ERROR","Please select an option")
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("ERROR","Select data to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("SUCCESS","Data deleted")

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('ERROR','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('SUCCESS','Data updated')

def selection(event):
    selected_item=tree.selection()

    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='' or nameEntry.get()=='' :
        messagebox.showerror("ERROR","Please fill all fields")
    elif database.id_exists(idEntry.get()):
          messagebox.showerror("ERROR","Employee Id already exists")
    else :
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("SUCCESS","Employee Added")

#GUI
window = CTk()
window.geometry('930x580+100+100')
window.resizable(0,0)
window.title("Employee Management System")
window.configure(fg_color='white')

logo=CTkImage(Image.open('bg.jpg'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='white')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text="Id",font=("Arial",18,"bold"),text_color='darkblue')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')
idEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text="Name",font=("Arial",18,"bold"),text_color='darkblue')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')
nameEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text="Phone",font=("Arial",18,"bold"),text_color='darkblue')
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')
phoneEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text="Role",font=("Arial",18,"bold"),text_color='darkblue')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['Web Developer','Cloud Architect','Network Engineer','Business Analyst','UI/UX Designer',
              'Data Science','IT Consultent']
roleBox=CTkComboBox(leftFrame,values=role_options,font=("Arial",15,"bold"),width=180,state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set('Web Developer')

genderLabel=CTkLabel(leftFrame,text="Gender",font=("Arial",18,"bold"),text_color='darkblue')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options=['Male','Female','Others']
genderBox=CTkComboBox(leftFrame,values=gender_options,font=("Arial",15,"bold"),width=180,state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')

salaryLabel=CTkLabel(leftFrame,text="Salary",font=("Arial",18,"bold"),text_color='darkblue')
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')
salaryEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)


rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Select Search')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1,)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2,pady=5)

showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.configure(show='headings')

tree.column('Id',width=50)
tree.column('Name',width=150)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=80)
tree.column('Salary',width=140)

style=ttk.Style()
style.configure('Treeview.Heading',font=("Arial",15,"bold"),text_color='dark blue')
style.configure('Treeview',font=("Arial",15,"bold"),text_color='dark blue')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='white')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('ariel',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5,padx=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('ariel',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('ariel',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('ariel',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('ariel',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

#treeview

window.bind('<ButtonRelease>',selection)

window.mainloop()