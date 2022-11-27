print('welcome to you')

from tkinter import *
from tkinter import ttk, messagebox


GUI = Tk ()
GUI.title('Program click button')# ชื่อโปรแกรม
GUI.geometry('500x300')# ปรับขนาดหน้าจอ

def Show():
    messagebox.showinfo('show Box','Helloworld')


B1 = ttk.Button(GUI,text='click button pls',command=Show)
B1.pack(ipadx=50,ipady=30,pady=50) # แปะปุ่มไว้กับโปรแกรม

GUI.mainloop()
