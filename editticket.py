import tkinter as tk
from tkinter import *
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox as mBox
from tkinter.constants import END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
import csv
from pandas import notnull

temp=[]
u=open("temp8.csv",'r')
a=csv.reader(u)
for i in a:
    temp.append(i)
u.close()
psngrid=temp[-2][0]
psngrname=temp[-2][1]
psngrphno=temp[-2][2]
psngrseat=temp[-2][3]
#-----------------------------------------------------------------------------------------------------------------------
#import
etwin = tk.Tk()
etwin.title('Edit Flight')
etwin.resizable(0, 0)
etwin.geometry("1280x720")
etwin.iconbitmap('editflight.ico')
#-----------------------------------------------------------------------------------------------------------------------
#background image / button images source
bg= PhotoImage(file='editticketbg.png')
updatebuttonimg= PhotoImage(file='updatebutton2.png')
calendarimg= PhotoImage(file='calendarr.png')
bgimg= Label(etwin, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)
#-----------------------------------------------------------------------------------------------------------------------
pid= Label(etwin,text=psngrid,width=20,borderwidth=2,font=('Calibri','21','normal'),bd=0,state=NORMAL,bg='#fff1e2')
pname= Entry(etwin,width=20,borderwidth=2,font=('Calibri','21','normal'),bd=0,bg='#fff1e2',justify=CENTER)
pphno= Entry(etwin,width=20,borderwidth=2,font=('Calibri','21','normal'),bd=0,state=NORMAL,bg='#fff1e2',justify=CENTER)
pseat= Entry(etwin,width=15,borderwidth=2,font=('Calibri','21','normal'),bd=0,state=NORMAL,bg='#fff1e2',justify=CENTER)
pid.place(x=662,y=212)
pname.place(x=662,y=267)
pphno.place(x=662,y=322)
pseat.place(x=662,y=379)
pname.insert(0,psngrname)
pphno.insert(0,psngrphno)
if psngrseat=='Economy':
    pseat.insert(0,'E')
elif psngrseat=='Business Class':
    pseat.insert(0,'B')
#-----------------------------------------------------------------------------------------------------------------------
def UpdateTicket():
    my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="flights")
    my_conn = my_connect.cursor()
    if len(pname.get())==0 or len(pphno.get())==0 or len(pseat.get())==0:
        mbox.showerror('Error','Please fill all the fields')
    else:
        if pseat.get()=='E' or pseat.get()=='B' or pseat.get()=='e' or pseat.get()=='b':
            if pseat.get()=='E' or pseat.get()=='e':
                finalseat='Economy'
            elif pseat.get()=='B' or pseat.get()=='b':
                finalseat='Business Class'
            my_conn.execute("update passengers set fullname='"+pname.get()+"',phno='"+pphno.get()+"',seattype='"+finalseat+"' where pid='"+psngrid+"';")
            my_connect.commit()
            mbox.showinfo('Success','Ticket Updated Successfully')
            etwin.destroy()
            import main
        else:
            mbox.showerror('Error!','Please enter valid seat type (E/B)')
#-----------------------------------------------------------------------------------------------------------------------
bthome=PhotoImage(file='homebutton2.png')
def homebt():
    etwin.destroy()
    import main
Button(etwin,image=bthome,command=homebt,bd=0,bg='#a29680').place(x=1220,y=0)
b1= tk.Button(etwin,image=updatebuttonimg,command=UpdateTicket,bd=0,bg='#fee9d0').place(x=580,y=450)

etwin.mainloop()
