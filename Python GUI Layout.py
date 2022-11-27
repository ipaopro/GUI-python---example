from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Program layout')
GUI.geometry('500x300')


L1 = Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar() #ตัวแปลพิเศษเอาไว้เก็บค่า
             

E1 = ttk.Entry(GUI, textvariable= v_kilo, width=12, justify='right', font=('digital-7',25))
E1.pack(pady=10)

def Calc(event=None):
    print('Wait Pls')
    kilo = float(v_kilo.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar
    print (kilo * 10)
    calc_result = kilo * 299
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายเงินทั้งหมด: {:,.2f} บาท ' .format(calc_result))
 
B1 = ttk.Button(GUI,text='Click price',command=Calc)
B1.pack(ipadx=35,ipady=25,pady=10)

E1.bind('<Return>',Calc) #ต้องใส่คำว่า event=None ไว้ในฟังชันด้วย

GUI.mainloop() 
