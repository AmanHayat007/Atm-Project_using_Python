from tkinter import *
import random as r
from tkinter import messagebox
top = Tk()
top.title("ATM")
top.geometry('800x600')
top.config(bg = 'ORANGE')
def window1():
    
    win1 = Toplevel(top)
    win1.geometry('800x600')
    win1.config(bg = 'ORANGE')
    bal = r.randrange(9999, 999999)
        
    def ChangePin():
        win2 = Toplevel(win1)
        win2.geometry('800x600') 
        win2.config(bg = 'ORANGE')  
        
        def change():
            if New_pin.get() == Re_pin.get():
                messagebox.showinfo('PIN changed', 'Your PIN was changed successfully')
            elif New_pin.get() == '' or Re_pin.get() == '':
                messagebox.showerror('Error 404', 'Please Enter a Valid PIN')
            else:
                messagebox.showinfo('Error', 'Entered PIN did not matched')
        label6 = Label(win2, text = 'Enter Old PIN', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 50)
        OldPin = Entry(win2, textvariable = pin, bg = 'white').place(x= 350, y = 60)
        
        label7 = Label(win2, text = 'Enter New PIN', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 100)
        New_pin = StringVar()
        NewPin = Entry(win2, textvariable = New_pin, bg = 'white').place(x= 350, y = 110)
        
        label8 = Label(win2, text = 'Re-Enter New PIN ', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 150)
        Re_pin = StringVar()
        Re_enter = Entry(win2, textvariable = Re_pin, bg = 'white').place(x= 350, y = 160)
        btn4 = Button(win2, text = 'Continue', command = change).place(x = 400, y = 210)
        
    def DPP():
        messagebox.showinfo('Successfully Deposited','Your Amount of ' + Dep.get() + ' was Deposited to your Bank Account ') 

    label3 = Label(win1, text = 'Balance Enquiry', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 50)
    Bal = StringVar(value = bal)
    balance = Entry(win1, textvariable = Bal , bg = 'white').place(x= 350, y = 60)
    
    label4 = Label(win1, text = 'Deposit', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 100)
    Dep = StringVar()
    deposit = Entry(win1, textvariable = Dep, bg = 'white').place(x= 350, y = 110)
    
    def WDD():
        messagebox.showinfo('Successfully Withdrawn', 'Your Amount of ' + Wid.get() + ' was Withdrawn from your Bank Account') 
    label5 = Label(win1, text = 'Withdraw', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x = 100, y= 150)
    Wid = StringVar()
    withdraw = Entry(win1, textvariable = Wid, bg = 'white').place(x= 350, y = 160)
    
    btn1 = Button(win1, text = 'Change Pin', command = ChangePin).place(x = 400, y = 210)
    
    btn2 = Button(win1, text = 'Deposit', command = DPP).place(x = 600, y = 100)
    
    btn3 = Button(win1, text = 'Withdraw', command = WDD).place(x = 600, y = 150)

top.resizable(width=False,height=False)



label1 = Label(top, text = 'Welcome to BANK OF LPU', bg = 'black', fg = 'white', font =('Comic Sans', 26)).place(x =200, y = 20)

label2 = Label(top, text = 'Enter 4 digit PIN', bg = 'black', fg = 'white', font = ('Comic Sans', 20)).place(x=300, y =200)
pin = StringVar()
Pin = Entry(top, textvariable = pin, bg = 'white').place(x = 350, y =280)

btn = Button(top, text='SUBMIT', command= window1).place(x=380, y=320)


top.mainloop()

    