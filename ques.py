#student name,id and password; when clicking on submit button,messagebox should be appeared
from tkinter import*
from tkinter import messagebox
parent=Tk()
name=Label(parent,text='Student Name: ').grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)
stid=Label(parent,text='Student ID').grid(row=1,column=0)
e2=Entry(parent).grid(row=1,column=1)
password=Label(parent,text='Password').grid(row=2,column=0)
e3=Entry(parent).grid(row=2,column=1)
def onclick():
    messagebox.showinfo('askquestion','Are you Sure ?')
submit=Button(parent,text='Submit',command=onclick).grid(row=3,column=0)
parent.mainloop()