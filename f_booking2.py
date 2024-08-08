import tkinter as tk
from tkinter import Button, Canvas, Checkbutton, Frame, Label, OptionMenu, PhotoImage, StringVar, messagebox as mBox
from tkinter.constants import ACTIVE, END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image
import csv

#------------------------------------------------------
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
delarrowimg= PhotoImage(file='delarrow.png')
searchbuttonimg= PhotoImage(file='searchbutton.png')
#------------------variables----------------------#
one_way= tk.IntVar()
round_trip=tk.IntVar()
multi_city= tk.IntVar()
#-----------------Labels-----------------------#
labelfrom= tk.Label(win,text='From:',font=('Comic Sans MS','17','normal'),bg='white')
labelfrom.place(x=370,y=322)
labelto= tk.Label(win,text='To:',font=('Comic Sans MS','17','normal'),bg='white')
labelto.place(x=670,y=322)
labeldeparture= tk.Label(win,text='Departure',font=('Comic Sans MS','16','normal'),bg='white')
labeldeparture.place(x=370,y=420)
labeltriptype= tk.Label(win,text='Trip Type',font=('Comic Sans MS','20','normal'),bg='white')
labeltriptype.place(x=380,y=227)
labelreturn= tk.Label(win,text='Return',font=('Comic Sans MS','16','normal'),bg='white')
#--------------------Entry Boxes-----------------#
entryfrom=       tk.Entry(win,width=16,borderwidth=2,bg='white',font=('Calibri','14','normal'),bd=1)
entryfrom.place(x=445,y=325)
entryto    =     tk.Entry(win,width=18,borderwidth=2,bg='white',font=('Calibri','14','normal'),bd=1)
entryto.place(x=715,y=325)
entryd     =     tk.Entry(win,width=9,borderwidth=3,bg='white',font=('Calibri','14','normal'),bd=1)
entryd.place(x=490,y=424)
entryr     =     tk.Entry(win,width=9,borderwidth=3,bg='white',font=('Calibri','14','normal'),bd=1)

#------------------functions-------------------#

def Oneway():
    global b4label
    global noswitchlabel
    labelreturn.destroy()
    entryr.destroy()
    if b4label.winfo_exists()==1:
        b4label.destroy()
    if noswitchlabel.winfo_exists()==1:
        noswitchlabel.destroy()
    b4label=      tk.Button(win,text='        ',height=2,bg='white',bd=0,activebackground='white')
    b4label.place(x=860,y=425)
    noswitchlabel=tk.Button(win,text='        ',height=1,bg='white',bd=0,activebackground='white')
    noswitchlabel.place(x=628,y=426)

def RoundTrip():
    global labelreturn
    global entryr
    global b4label
    global noswitchlabel
    if b4label.winfo_exists()==1:
        b4label.destroy()
    if noswitchlabel.winfo_exists()==1:
        noswitchlabel.destroy()
    if labelreturn.winfo_exists()==1:
        labelreturn.destroy()
    if entryr.winfo_exists()==1:
        entryr.destroy()
    labelreturn= tk.Label(win,text='Return',font=('Comic Sans MS','16','normal'),bg='white')
    labelreturn.place(x=670,y=420)
    entryr     =     tk.Entry(win,width=10,borderwidth=4,bg='white')
    entryr.place(x=760,y=424)

def Searchflight():
    global f,ddate,dater
    numefro=0
    numeto=0
    eto= entryto.get().strip()
    efro= entryfrom.get().strip()
    if efro == '':
        mbox.showinfo('Error! ','Please select  a STARTING POINT')
    else:
        numefro=1
    if eto == '':
            mbox.showinfo('Error! ','Please enter your DESTINATION')
    else:
        numeto=1
    if numefro == 1 and numeto ==1:
        if f.get() == 'One Way':
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="flights")
            my_conn = my_connect.cursor()
            my_conn.execute("SELECT f_id,f_company,f_startdate,f_starttime,f_reachtime,f_enddate,f_price,f_startloc,f_endloc FROM flights where f_startdate='"+ddate+"'and f_startloc='"+entryfrom.get()+"' and f_endloc='"+entryto.get()+"';")
            ls = my_conn.fetchall()
            ls=list(ls)
            if(len(ls)>0):
                searchdata=[ddate,entryfrom.get(),entryto.get()]
                g=open("temp2.csv", 'a')
                w=csv.writer(g)
                wobj=w.writerow(searchdata)
                g.close()
                g=open("temp7.csv", 'a')
                w=csv.writer(g)
                wobj=w.writerow(f.get())
                g.close()
                win.destroy()
                import f_booking_ow
            else:
                mbox.showinfo('Error','No Flights found!')
        elif f.get() == 'Round Trip':
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="flights")
            my_conn = my_connect.cursor()
            my_conn.execute("SELECT * FROM flights where f_startdate='"+ddate+"'and f_startloc='"+entryfrom.get()+"' and f_endloc='"+entryto.get()+"' and f_returndate = '"+dater+"';")
            ls = my_conn.fetchall()
            ls=list(ls)
            if(len(ls)>0):
                searchdata=[ddate,entryfrom.get(),entryto.get(),dater]
                g=open("temp2.csv", 'a')
                w=csv.writer(g)
                wobj=w.writerow(searchdata)
                g.close()
                g=open("temp7.csv", 'a')
                w=csv.writer(g)
                wobj=w.writerow(f.get())
                g.close()
                win.destroy()
                import f_booking_ow
            else:
                mbox.showinfo('Error','No Flights found!')
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

dated=''
yeard=''
monthd=''
dater=''
monthr=''
yearr=''
def switchfromto2():
    global dated,monthd,yeard,monthr,dater,yearr
    temp1=entryd.get()
    temp2=entryr.get()
    entryd.delete(0, "end")
    entryd.insert(0, temp2)
    entryr.delete(0, "end")
    entryr.insert(0, temp1)
    tempd=dated
    tempm=monthd
    tempy=yeard
    dated=dater
    monthd=monthr
    yeard=yearr
    dater=tempd
    monthr=tempm
    yearr=tempy
    return temp1,temp2,tempm,tempy,tempd

def insertddate():
    global dated,monthd,yeard,ddate
    temp=[]
    u=open("temp1.csv",'r')
    a=csv.reader(u)
    for i in a:
        temp.append(i)
    temp02=str(temp[-2])
    dateee=temp02[2:-2]
    if dateee[1:2]=='/':
        monthd=dateee[0:1]
        if dateee[4:5]=='/':
            dated=dateee[2:4]
        else:
            dated=dateee[2:3]
    else:
        monthd=dateee[0:2]
        if dateee[5:6]=='/':
            dated=dateee[3:5]
        else:
            dated=dateee[3:4]
    yeard=dateee[-2:]
    inserteddate=(dated,'/',monthd,'/',yeard)
    entryd.delete(0,'end')
    entryd.insert(0,inserteddate)
    ddate='20'+yeard+'-'+monthd+'-'+dated
    return temp,u,a,i,temp02,dateee

def insertrdate():
    global dater,monthr,yearr
    temp=[]
    u=open("temp1.csv",'r')
    a=csv.reader(u)
    for i in a:
        temp.append(i)
    temp02=str(temp[-2])
    dateee=temp02[2:-2]
    if dateee[1:2]=='/':
        monthr=dateee[0:1]
        if dateee[4:5]=='/':
            dater=dateee[2:4]
        else:
            dater=dateee[2:3]
    else:
        monthr=dateee[0:2]
        if dateee[5:6]=='/':
            dater=dateee[3:5]
        else:
            dater=dateee[3:4]
    yearr=dateee[-2:]
    inserteddate=(dater,'/',monthr,'/',yearr)
    entryr.delete(0,'end')
    entryr.insert(0,inserteddate)
    dater='20'+yearr+'-'+monthr+'-'+dater
    return temp,u,a,i,temp02,dateee

def calendardatesetd():
    from tkcalendar import Calendar
    root = tk.Tk()
    root.title('Select a date')
    root.resizable(0,0)
    root.geometry("300x300")
    cal = Calendar(root, selectmode = 'day',
                year = 2021, month = 9,
                day = 22)
    cal.pack(pady = 20)
    def grad_date():
        f=open("temp1.csv", 'a')
        d= cal.get_date()
        l=[d]
        w=csv.writer(f)
        wobj=w.writerow(l)
        f.close()
        insertddate()
        root.destroy()
        return f,w,d,l,root
    tk.Button(root, text = "Set",
        command = grad_date).pack(pady = 20)
    date = Label(root, text = "")
    date.pack(pady = 20)
    root.mainloop()
    return date,cal,root

def calendardatesetr():
    from tkcalendar import Calendar
    root = tk.Tk()
    root.title('Select a date')
    root.resizable(0,0)
    root.geometry("300x300")
    cal = Calendar(root, selectmode = 'day',
                year = 2021, month = 9,
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
        insertrdate()
        return f,w,d,l,root
    tk.Button(root, text = "Set",
        command = grad_date).pack(pady = 20)
    date = Label(root, text = "")
    date.pack(pady = 20)
    root.mainloop()
    return root,date,cal

bthome=PhotoImage(file='homebutton2.png')
def homebt():
    win.destroy()
    import main
Button(win,image=bthome,command=homebt,bd=0,bg='white').place(x=1215,y=0)
#---------------------Radiobutton------------#
f= StringVar()
f.set(None)
oway= tk.Radiobutton(win,text='One Way',font=('Comic Sans MS','13','normal'),variable=f,value='One Way',command=Oneway,bg='white')
rtrip=tk.Radiobutton(win,text='Round Trip',font=('Comic Sans MS','13','normal'),variable=f,value='Round Trip',command=RoundTrip,bg='white')
oway.place(x=550,y=228)
rtrip.place(x=742,y=228)
#--------------------Buttons------------------------#
b2= tk.Button(win,image=calendarimg,command=calendardatesetd).place(x=590,y=425)
b4= tk.Button(win,image=calendarimg,command=calendardatesetr).place(x=860,y=425)
b3= tk.Button(win,image=searchbuttonimg,command=Searchflight,bd=0,bg='white').place(x=500,y=470)
switch= tk.Button(win,image=switchimg,command=switchfromto,bg='white',bd=0).place(x=630,y=328)
switch2= tk.Button(win,image=switchimg,command=switchfromto2,bg='white',bd=0).place(x=630,y=427)
b4label=      tk.Button(win,text='        ',height=2,bg='white',bd=0,activebackground='white')
b4label.place(x=860,y=425)
noswitchlabel=tk.Button(win,text='        ',height=1,bg='white',bd=0,activebackground='white')
noswitchlabel.place(x=628,y=426)
#---------------------mainloop-----------------------#
win.mainloop()
