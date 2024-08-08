import csv
import tkinter as tk
from tkinter import Button, Canvas, Checkbutton, Frame, Label, OptionMenu, PhotoImage, StringVar, messagebox as mBox
from tkinter.constants import ACTIVE, END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image
import csv


winview = tk.Tk()
winview.title('Search Ticket')
winview.resizable(0,0)
winview.iconbitmap('mainwin.ico')
winview.geometry('1280x720')
#-------------------Images------------------------#
bg= PhotoImage(file='searchticketbg.png')
bgimg= Label(winview, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)
bt33= PhotoImage(file='searchbutton3.png')


psngrname= tk.Entry(winview,font=('Roboto Mono','14','normal'),width=21,borderwidth=2,bd=2)
psngrname.place(x=550,y=390)
psngrphno= tk.Entry(winview,font=('Roboto Mono','14','normal'),width=20,borderwidth=2,bd=2)
psngrphno.place(x=561,y=442)

def searchtk():

    my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flights"
    )
    my_conn = my_connect.cursor()
    
    #
    my_conn.execute("select fullname,phno,f_id,f_startdate,f_starttime,seattype from passengers where fullname='"+psngrname.get()+"' and phno='"+psngrphno.get()+"'")
    print(my_conn)
    ls = my_conn.fetchall()
    if len(ls)==0:
        mBox.showinfo('Error!','No ticket Found')
    else:
        name=ls[0][0]
        phno=ls[0][1]
        flightid=ls[0][2]
        flightstartdate=ls[0][3]
        flightstarttime=ls[0][4]
        seattype=ls[0][5]
        values=[name,phno,flightid,flightstartdate,flightstarttime,seattype]
        g=open("temp5.csv", 'a')
        w=csv.writer(g)
        wobj=w.writerow(values)
        g.close()
        winview.destroy()
        import viewticket

bthome=PhotoImage(file='homebutton.png')
def homebt():
    winview.destroy()
    import main
Button(winview,image=bthome,command=homebt,bd=0,bg='#085c74').place(x=1100,y=0)

Button(winview,image=bt33,command=searchtk,bd=0,bg='#085c74').place(x=577,y=487)

winview.mainloop()
