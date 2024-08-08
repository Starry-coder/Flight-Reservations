import tkinter as tk
from tkinter import *
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox as mBox
from tkinter.constants import END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
import csv
#-------------main window------------------------
ewin = tk.Tk()
ewin.title('Edit Flights')
ewin.resizable(0, 0)
ewin.geometry("1280x720")
ewin.iconbitmap('editflight.ico')
#---------------------------------------------------
bg= PhotoImage(file='Edit1.png')
switchimg= PhotoImage(file='swaparrow2.png')
calendarimg= PhotoImage(file='calendarr.png')
searchbuttonimg= PhotoImage(file='searchbutton4.png')
viewbuttonimg= PhotoImage(file='viewall.png')
editbuttonimg= PhotoImage(file='editbutton.png')
deletebuttonimg= PhotoImage(file='deletebutton.png')
addbuttonimg= PhotoImage(file='addbutton.png')
bgimg= Label(ewin, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)
#---------------------------------------------------
entryfrom =       tk.Entry(ewin,width=13,borderwidth=2,bg='white',font=('Calibri','13','normal'),bd=1)
entryfrom.place(x=145,y=457)
entryto =         tk.Entry(ewin,width=17,borderwidth=3,bg='white',font=('Calibri','13','normal'),bd=1)
entryto.place(x=350,y=457)
entrydeparture =  tk.Entry(ewin,width=7,borderwidth=2,state=DISABLED,bg='white',font=('Calibri','13','normal'),bd=1)
entrydeparture.place(x=182,y=492)
entryarrival =    tk.Entry(ewin,width=10,borderwidth=3,state=DISABLED,bg='white',font=('Calibri','13','normal'),bd=1)
entryarrival.place(x=395,y=492)
#---------------------------------------------------
cbutton1= IntVar(ewin,name='cbutton1')
cbutton1 = Checkbutton(ewin, text = "Check this bok if the flight has a return date", variable = cbutton1,onvalue = 1,
                    offvalue = 0, height = 1, width = 40,bg='#c0fcd4')
cbutton1.place(x=160,y=525)
clicked = StringVar(ewin,name='clicked')
clicked.set('-SELECT-')
#---------------------------------------------------

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


def switchfromto2():
    global dated,monthd,yeard,monthr,dater,yearr,dated
    temp1=entrydeparture.get()
    temp2=entryarrival.get()
    entrydeparture.delete(0, "end")
    entrydeparture.insert(0, temp2)
    entryarrival.delete(0, "end")
    entryarrival.insert(0, temp1)
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
    entrydeparture['state'] = tk.NORMAL
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
    entrydeparture.delete(0,'end')
    entrydeparture.insert(0,inserteddate)
    ddate='20'+yeard+'-'+monthd+'-'+dated
    entrydeparture['state'] = tk.DISABLED
    return temp,u,a,i,temp02,dateee

def insertrdate():
    global dater,monthr,yearr
    entryarrival['state'] = tk.NORMAL
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
    entryarrival.delete(0,'end')
    entryarrival.insert(0,inserteddate)
    dater='20'+yearr+'-'+monthr+'-'+dater
    entryarrival['state'] = tk.DISABLED
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
        insertddate()
        f.close()
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

def Searchflight():
    global flightlist,clicked
    numefro=0
    numeto=0
    numearr=0
    numedep=0
    eto= entryto.get().strip()
    efro= entryfrom.get().strip()
    earr= entryarrival.get().strip()
    edep= entrydeparture.get().strip()
    #print(ewin.getvar(name ="cbutton1"))
    if efro == '':
        mbox.showinfo('Error! ','Please select  a STARTING POINT')
    else:
        numefro=1
        if eto == '':
                mbox.showinfo('Error! ','Please enter your DESTINATION')
        else:
            numeto=1
            if edep == '':
                mbox.showinfo('Error! ','Please enter your departure date')
            else:
                numedep=1
                if ewin.getvar(name ="cbutton1")==1:
                    if earr == '':
                        mbox.showinfo('Error! ','Please enter your arrival date')
                    else:
                        numearr=1
    if ewin.getvar(name='cbutton1')==1: #if arrival date is selected
        print(dater,ddate)
        if numefro == 1 and numeto ==1 and numearr ==1 and numedep ==1:
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="flights")
            my_conn = my_connect.cursor()
            my_conn.execute("SELECT * FROM flights where f_startdate='"+ddate+"'and f_returndate ='"+dater+
                            "' and f_startloc='"+entryfrom.get()+"' and f_endloc='"+entryto.get()+"' ;")
            ls = my_conn.fetchall()
            ls=list(ls)
            flightlist=['-SELECT-']
            for i in range(len(ls)):
                flightlist.append([str(ls[i][0]),'|',str(ls[i][1]),'|',str(ls[i][2]),str(ls[i][3]),'|',str(ls[i][4]),'|',str(ls[i][5]),str(ls[i][6]),'|',str(ls[i][7]),'|',str(ls[i][8])])
            clicked = StringVar(ewin,name='clicked')
            clicked.set('-SELECT-')
            print(flightlist)
            dropall = OptionMenu( ewin , clicked , *flightlist )
            dropall.place(x=93,y=570)
            dropall.config(width=65,height=1,bg='#c0fcd4')
            b6.place(x=260,y=600)
            b7.place(x=350,y=600)
            return dropall,clicked,ls,my_connect,my_conn,flightlist
    else: #if only departure date is selected
        if numefro == 1 and numeto ==1 and  numedep ==1:
            my_connect = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="root",
                    database="flights")
            my_conn = my_connect.cursor()
            my_conn.execute("SELECT * FROM flights where f_startdate='"+ddate+"' and f_startloc='"+entryfrom.get()+"' and f_endloc='"+entryto.get()+"' ;")
            ls = my_conn.fetchall()
            ls=list(ls)
            flightlist=['-SELECT-']
            for i in range(len(ls)):
                flightlist.append([str(ls[i][0]),'|',str(ls[i][1]),'|',str(ls[i][2]),str(ls[i][3]),'|',str(ls[i][4]),'|',str(ls[i][5]),str(ls[i][6]),'|',str(ls[i][7])])
            clicked = StringVar(ewin,name='clicked')
            clicked.set('-SELECT-')
            dropall = OptionMenu( ewin , clicked , *flightlist )
            dropall.place(x=93,y=570)
            dropall.config(width=65,height=1,bg='#c0fcd4')
            b6.place(x=260,y=600)
            b7.place(x=350,y=600)
            return dropall,clicked,ls,my_connect,my_conn,flightlist

def Searchallflight():
    global flightlist,clicked
    my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="flights")
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT f_id,f_startloc,f_endloc,f_startdate,f_enddate FROM flights;")
    ls = my_conn.fetchall()
    ls=list(ls)
    flightlist=['-SELECT-']
    for i in range(len(ls)):
        flightlist.append(ls[i])
    clicked = StringVar(ewin,name='clicked')
    clicked.set('-SELECT-')
    dropall = OptionMenu( ewin , clicked , *flightlist )
    dropall.place(x=93,y=570)
    dropall.config(width=65,height=1,bg='#c0fcd4')
    b6.place(x=260,y=600)
    b7.place(x=350,y=600)
    return dropall,clicked,ls,my_connect,my_conn,flightlist

def Editflight():
    g=open("temp6.csv", 'a')
    gotofid=clicked.get().split(",")[0].replace("(", "").replace("'", "")
    w=csv.writer(g)
    wobj=w.writerow(str(gotofid))#
    g.close()
    ewin.destroy()
    import editflight2

def Deleteflight():
    global flightlist,clicked
    res = mbox.askquestion('Delete Flight', 'Are you sure you want to delete this flight?', icon='warning')
    if res == 'yes' :
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="flights")
        my_conn = my_connect.cursor()
        my_conn.execute("DELETE FROM flights WHERE f_id = '"+str(ewin.getvar(name ="clicked")[0])+"';")
        my_connect.commit()

def Addflight():
    ewin.destroy()
    import addflight

bthome= PhotoImage(file='homebutton2.png')
def homebt():
    ewin.destroy()
    import main
Button(ewin,image=bthome,command=homebt,bd=0,bg='white').place(x=1215,y=0)
switch= tk.Button(ewin,image=switchimg,command=switchfromto,bg='#c0fcd4',bd=0).place(x=285,y=461)
switch2= tk.Button(ewin,image=switchimg,command=switchfromto2,bg='#c0fcd4',bd=0).place(x=285,y=497)
b1= tk.Button(ewin,image=calendarimg,command=calendardatesetd).place(x=250,y=494)
b2= tk.Button(ewin,image=viewbuttonimg,command=Searchallflight,bd=0,bg='#c0fcd4').place(x=220,y=545)
b3= tk.Button(ewin,image=searchbuttonimg,command=Searchflight,bd=0,bg='#c0fcd4').place(x=310,y=545)
b4= tk.Button(ewin,image=calendarimg,command=calendardatesetr).place(x=490,y=494)
b6= tk.Button(ewin,image=editbuttonimg,command=Editflight,bd=0,bg='#c0fcd4')
b7= tk.Button(ewin,image=deletebuttonimg,command=Deleteflight,bd=0,bg='#c0fcd4')
b8= tk.Button(ewin,image=addbuttonimg,command=Addflight,bd=0,bg='#c0fcd4')
b8.place(x=170,y=600)

ewin.mainloop()