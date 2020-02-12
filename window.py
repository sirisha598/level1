# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
user1="Sirisha"
user2="Roy"
password1="123"
password2="891"
def login():
    if ((txt1.get()==user1 and txt2.get()==password1) or (txt1.get()==user2 and txt2.get()==password2)):
        window.destroy()
        window2=tk.Tk()
        window2.configure(width=800,height=400,bg='Green')
        lb3=tk.Label(window2,width=10,height=2,text="User Name",bg="Red",fg="white",font=("times",15,'bold'))
        lb3.place(x=50,y=100)
        txt3=tk.Entry(window2,width=15,bg="Blue",fg="white",font=("times",15,'bold'))
        txt3.place(x=250,y=110)
        button2=tk.Button(window2,width=10,height=2,text="Logout",command=window2.destroy,bg="violet",fg="white",font=("times",15,"bold"),activebackground="Blue")
        button2.place(x=160,y=280)
        window2.mainloop()
    else:
        print("Invalid User or Password")
def clear():
    txt1.delete(first=0,last=len(txt1.get()))
def clear1():
    txt2.delete(first=0,last=len(txt2.get()))
import tkinter as tk
window=tk.Tk()
window.configure(width=800,height=400,bg='Green')
lb1=tk.Label(window,width=10,height=2,text="User Name",bg="Red",fg="white",font=("times",15,'bold'))
lb1.place(x=50,y=100)
txt1=tk.Entry(window,width=15,bg="Blue",fg="white",font=("times",15,'bold'))
txt1.place(x=250,y=110)
lb2=tk.Label(window,width=10,height=2,text="Password",bg="Red",fg="white",font=("times",15,'bold'))
lb2.place(x=50,y=200)
txt2=tk.Entry(window,width=15,bg="Blue",fg="white",font=("times",15,'bold'))
txt2.place(x=250,y=220)
button1=tk.Button(window,width=10,height=2,text="Login",command=login,bg="violet",fg="white",font=("times",15,"bold"),activebackground="Blue")
button1.place(x=160,y=280)
button2=tk.Button(window2,width=10,height=2,text="Clear",command=clear,bg="pink",fg="white",font=("times",15,"bold"),activebackground="Green")
button2.place(x=170,y=240)
window.mainloop()
