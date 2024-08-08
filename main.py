import tkinter as tk
from tkinter import Button, Checkbutton, Frame, Label
from tkinter import OptionMenu, PhotoImage, StringVar, messagebox as mBox
from tkinter import messagebox as mbox
import csv

mainwin = tk.Tk()
mainwin.title('AV Airline Management')
mainwin.resizable(0,0)
mainwin.iconbitmap('mainwin.ico')
mainwin.geometry('1280x720')
#-------------------Images------------------------#
bg= PhotoImage(file='mgmthomenew.png')
bgimg= Label(mainwin, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)

button1b= PhotoImage(file='viewticketbutton.png')
button2b= PhotoImage(file='bookticketbutton.png')
button3b= PhotoImage(file='editticketbutton.png')
button4b= PhotoImage(file='editflightbutton.png')
button5b= PhotoImage(file='switchuserbutton.png')
button6b= PhotoImage(file='exitbutton.png')
temp=[]
u=open("temp3.csv",'r')
a=csv.reader(u)
for i in a:
    if len(i)>0:
        temp.append(i)
usrname=temp[-1][0]
u.close()
#-------------------Labels------------------------------#
l1= Label(mainwin,text='You have logged in as '+usrname,
        font=('Comic Sans MS','18','bold'),bg='#a8d4fc')
l1.place(x=0,y=0)
#----------------Functions------------------------#
def viewticket():
    mainwin.destroy()
    import searchticket

def bookticket():
    mainwin.destroy()
    import f_booking2

def updateticket():
    mainwin.destroy()
    import searchticket2

def updateflight():
    mainwin.destroy()
    import editflight

def switchuser():
    mainwin.destroy()
    import login

def exitt():
    mainwin.destroy()

#----------------Buttons-----------------------#
Button(mainwin,image=button1b,command= viewticket ,bd=0,bg='white').place(x=100,y=200)
Button(mainwin,image=button2b,command= bookticket,bd=0,bg='grey' ).place(x=500,y=200)
Button(mainwin,image=button3b,command= updateticket,bd=0,bg='white' ).place(x=900,y=200)
Button(mainwin,image=button4b,command= updateflight,bd=0,bg='cyan' ).place(x=100,y=500)
Button(mainwin,image=button5b,command= switchuser,bd=0 ,bg='white').place(x=500,y=500)
Button(mainwin,image=button6b,command= exitt,bd=0,bg='grey' ).place(x=900,y=500)





mainwin.mainloop()
