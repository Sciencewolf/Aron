'''
Creator: Aron Marton
IG: _aron.marton
Beginner Python programmer
'''

#pip install win10toast
from win10toast import ToastNotifier
from tkinter import messagebox
from tkinter import *
import tkinter as tk

wn = Tk()
wn.geometry('450x300')
wn.configure(bg='black')
wn.title('App')

#using while to repeat the code
while 1:
    messagebox.askyesnocancel('Notification', 'Close the window?')
    messagebox.showerror('Alert', 'Error!')
    toaster = ToastNotifier()
    toaster.show_toast('Notification', 'Retry', threaded=True,
                        icon_path=None, duration=2)

wn.mainloop()

# 'wn' you can change to other attribute for example 'window' or 'root'
