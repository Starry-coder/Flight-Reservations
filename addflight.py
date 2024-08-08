import tkinter as tk
from tkinter import *
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox as mBox
from tkinter.constants import END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image  #If you dont have it, use "pip install pillow"
import csv
from pandas import notnull
#-----------------------------------------------------------------------------------------------------------------------
#import
eewin = tk.Tk()
eewin.title('Add Flight')
eewin.resizable(0, 0)
eewin.geometry("1280x720")
eewin.iconbitmap('editflight.ico')
#-----------------------------------------------------------------------------------------------------------------------
#background image / button images source
bg= PhotoImage(file='addflightbg.png')
updatebuttonimg= PhotoImage(file='updatebutton2.png')
addbuttonimg= PhotoImage(file='addbutton.png')
calendarimg= PhotoImage(file='calendarr.png')
bgimg= Label(eewin, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)
#-----------------------------------------------------------------------------------------------------------------------

fid= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0,state=NORMAL)
fco= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0)
fsd= Entry(eewin,width=20,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0,state=NORMAL)
fed= Entry(eewin,width=20,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0,state=NORMAL)
frdentry= Entry(eewin,width=20,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0,state=NORMAL)
fst= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0)
frt= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0)
f_o= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0)
f_d= Entry(eewin,width=23,borderwidth=2,bg='WHITE',font=('Calibri','13','normal'),bd=0)
f_p= Entry(eewin,width=25,borderwidth=2,bg='WHITE',font=('Calibri','12','normal'),bd=0)
fid.place(x=292,y=214)
fco.place(x=292,y=247)
fsd.place(x=292,y=282)
fed.place(x=292,y=317)
frdentry.place(x=292,y=351)
fst.place(x=292,y=385)
frt.place(x=292,y=419)
f_o.place(x=292,y=453)
f_d.place(x=292,y=485)
f_p.place(x=294,y=518)
#-----------------------------------------------------------------------------------------------------------------------
returndate=StringVar()
returndate.set('yes')

def showreturndate():
    frdentry.config(state= "disabled")
    b6.config(state= "normal")

def hidereturndate():
    frdentry.config(state= "normal")
    b6.config(state= "disabled")
    frdentry.delete(0,'end')
    frdentry.insert(0,'~ NULL ~')
    frdentry.config(state= "disabled")

def Addflight():
    if fid.get()=='' or fco.get()=='' or fsd.get()=='' or fed.get()=='' or fst.get()=='' or frt.get()=='' or f_o.get()=='' or f_d.get()=='' or f_p.get()=='':
        mbox.showerror('Error', 'Please fill all the fields')
    else:
        if len(fst.get())==8 and len(frt.get())==8:
            my_connect = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="flights")
            my_conn = my_connect.cursor()
            if frdentry.get()=='~ NULL ~':
                my_conn.execute("INSERT INTO FLIGHTS VALUES('"+fid.get()+"','"+fco.get()+"','"+ddate+"','"+fst.get()+"','"+frt.get()+"','"+edate+"','"+
                                f_p.get()+"','"+f_o.get()+"','"+f_d.get()+"',NULL);")
            else:
                my_conn.execute("INSERT INTO FLIGHTS VALUES('"+fid.get()+"','"+fco.get()+"','"+ddate+"','"+fst.get()+"','"+frt.get()+"','"+edate+"','"+
                                f_p.get()+"','"+f_o.get()+"','"+f_d.get()+"','"+dater+"');")
            my_connect.commit()
            mbox.showinfo('Success', 'Flight added successfully')
            eewin.destroy()
            import main
        else:
            mbox.showerror('Error', 'Please enter valid time in the format (hh:mm:ss)')
    #

def insertddate():
    global dated,monthd,yeard,ddate
    fsd['state'] = tk.NORMAL
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
    fsd.delete(0,'end')
    fsd.insert(0,inserteddate)
    ddate='20'+yeard+'-'+monthd+'-'+dated
    fsd['state'] = tk.DISABLED
    return temp,u,a,i,temp02,dateee

def insertedate():
    global dater,monthr,yearr,edate
    fed['state'] = tk.NORMAL
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
    fed.delete(0,'end')
    fed.insert(0,inserteddate)
    edate='20'+yearr+'-'+monthr+'-'+dater
    fed['state'] = tk.DISABLED
    return temp,u,a,i,temp02,edate

def insertretdate():
    global dater,monthr,yearr
    frdentry['state'] = tk.NORMAL
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
    frdentry.delete(0,'end')
    frdentry.insert(0,inserteddate)
    dater='20'+yearr+'-'+monthr+'-'+dater
    frdentry['state'] = tk.DISABLED
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
        insertretdate()
        root.destroy()
        return f,w,d,l,root
    tk.Button(root, text = "Set",
        command = grad_date).pack(pady = 20)
    date = Label(root, text = "")
    date.pack(pady = 20)
    root.mainloop()
    return root,date,cal

def calendardatesete():
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
        insertedate()
        root.destroy()
        return f,w,d,l,root
    tk.Button(root, text = "Set",
        command = grad_date).pack(pady = 20)
    date = Label(root, text = "")
    date.pack(pady = 20)
    root.mainloop()
    return root,date,cal

bthome= PhotoImage(file='homebutton2.png')
def homebt():
    eewin.destroy()
    import main
Button(eewin,image=bthome,command=homebt,bd=0,bg='white').place(x=1215,y=0)
#-----------------------------------------------------------------------------------------------------------------------

queyes= tk.Radiobutton(eewin,text='Yes',font=('Comic Sans MS','9','normal'),variable=returndate,value='yes',command=showreturndate,bg='#fee9d0').place(x=590,y=385)
queno=  tk.Radiobutton(eewin,text='No',font=('Comic Sans MS','9','normal'),variable=returndate,value='no',command=hidereturndate,bg='#fee9d0').place(x=660,y=385)

#-----------------------------------------------------------------------------------------------------------------------

b1= tk.Button(eewin,image=addbuttonimg,command=Addflight,bd=0,bg='#fee9d0').place(x=350,y=550)
b4= tk.Button(eewin,image=calendarimg,command=calendardatesetd,bg='#fee9d0').place(x=480,y=282)
b5= tk.Button(eewin,image=calendarimg,command=calendardatesete,bg='#fee9d0').place(x=480,y=317)
b6= tk.Button(eewin,image=calendarimg,command=calendardatesetr,bg='#fee9d0')
b6.place(x=480,y=352)


eewin.mainloop()