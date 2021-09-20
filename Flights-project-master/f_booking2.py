import tkinter as tk
from tkinter import Canvas, Checkbutton, Frame, Label, OptionMenu, PhotoImage, StringVar, messagebox as mBox
from tkinter.constants import ACTIVE, END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image
import csv





win = tk.Tk()
win.title('Ticket Booking')
win.resizable(0,0)
win.iconbitmap('booking.ico')
win.geometry('1280x720')
#-------------------Images------------------------#
bg= PhotoImage(file='bookingbg.png')
bgimg= Label(win, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)
switchimg= PhotoImage(file='swaparrow.png')
calendarimg= PhotoImage(file='calendarr.png')

#------------------variables----------------------#
one_way= tk.IntVar()
round_trip=tk.IntVar()
multi_city= tk.IntVar()

#-----------------Labels-----------------------#
labelfrom= tk.Label(win,text='From:',font=('Arial','15','normal'))
labelfrom.place(x=450,y=300)

labelto= tk.Label(win,text='To:',font=('Arial','15','normal'))
labelto.place(x=450,y=350)

labeldeparture= tk.Label(win,text='Departure:',font=('Arial','15','normal'))
labeldeparture.place(x=450,y=400)

labeltriptype= tk.Label(win,text='Trip Type:',font=('Arial','15','normal'))
labeltriptype.place(x=450,y=250)

labelreturn= tk.Label(win,text='Return',font=('Arial','15','normal'))
labelreturn.place(x=450,y=450)
#--------------------Entry Boxes-----------------#
entryfrom=       tk.Entry(win,width=50,borderwidth=4,bg='white')
entryfrom.place(x=550,y=300)

entryto    =     tk.Entry(win,width=50,borderwidth=4,bg='white')
entryto.place(x=550,y=350)

entryd     =     tk.Entry(win,width=10,borderwidth=4,bg='white')
entryd.place(x=550,y=400)

#------------------functions-------------------#

def Oneway():

    labelreturn.destroy()



def RoundTrip():
    global labelreturn
    if labelreturn.winfo_exists()==1:
        labelreturn.destroy()
    labelreturn= tk.Label(win,text='Return',font=('Arial','15','normal'))
    labelreturn.place(x=450,y=450)



def displaytype():
    numefro=0
    numeto=0
    eto= entryto.get().strip()
    efro= entryfrom.get().strip()
    if f.get() == 'One Way' or f.get() == 'Round Trip':
        if efro == '':
            mbox.showinfo('Error! ','Please select  a STARTING POINT')
        else:
            numefro=1
        if eto == '':
                mbox.showinfo('Error! ','Please enter your DESTINATION')
        else:
            numeto=1
        if numefro == 1 and numeto ==1:
            #adding to database here
            mbox.showinfo('Booked! ','Your ticket is now booked')

    else:
        mbox.showinfo('Error! ','Please select  a TRIP TYPE')
    return numefro,numeto,eto,efro



def switchfromto():
    temp1= entryfrom.get()
    temp2=entryto.get()
    entryfrom.delete(0, "end")
    entryfrom.insert(0, temp2)
    entryto.delete(0, "end")
    entryto.insert(0, temp1)
    temp1=''
    temp2=''
    return temp1 , temp2



def insertddate():
        temp=[]
        u=open("temp1.csv",'r')
        a=csv.reader(u)
        for i in a:
            temp.append(i)
        temp02=str(temp[-2])
        temp03=temp02[2:-2]
        entryd.insert(0,temp03)
        return temp,u,a,i,temp02,temp03



def calendardateset():
    from tkcalendar import Calendar
    root = tk.Tk()
    root.title('Select a date')
    root.resizable(0,0)
    root.geometry("300x300")
    cal = Calendar(root, selectmode = 'day',
                year = 2020, month = 5,
                day = 22)
    cal.pack(pady = 20)


    def grad_date():
        f=open("temp1.csv", 'a')
        d= cal.get_date()
        l=[d]
        w=csv.writer(f)
        wobj=w.writerow(l)
        f.close()
        root.destroy()
        insertddate()
        return f,w,d,l,root
    tk.Button(root, text = "Set",
        command = grad_date).pack(pady = 20)
    date = Label(root, text = "")
    date.pack(pady = 20)
    root.mainloop()



#---------------------Radiobutton------------#
f= StringVar()
f.set(None)

oway= tk.Radiobutton(win,text='One Way',font=('Arial','15','normal'),variable=f,value='One Way',command=Oneway)
rtrip=tk.Radiobutton(win,text='Round Trip',font=('Arial','15','normal'),variable=f,value='Round Trip',command=RoundTrip)



oway.place(x=550,y=250)
rtrip.place(x=680,y=250)




#--------------------Buttons------------------------#


b2= tk.Button(win,image=calendarimg,command=calendardateset).place(x=630,y=402)
b3= tk.Button(win,text='Book',command=displaytype).place(x=700,y=500)
switch= tk.Button(win,image=switchimg,command=switchfromto).place(x=685,y=326)




win.mainloop()
