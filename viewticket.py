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
winview.title('Boarding Pass')
winview.resizable(0,0)
winview.iconbitmap('mainwin.ico')
winview.geometry('1280x720')
#-------------------Images------------------------#
bg= PhotoImage(file='viewticketbg.png')
bgimg= Label(winview, image=bg)
bgimg.place(x=0,y=0,relwidth=1,relheight=1)

temp=[]
u=open("temp5.csv",'r')
a=csv.reader(u)
for i in a:
    temp.append(i)
u.close()
temp2= temp[-2]

if temp2[2]=='AI01':
    f_co='Air India'
if temp2[2]=='AA01':
    f_co='Air Asia'
if temp2[2]=='SJ01':
    f_co='Spice Jet'
if temp2[2]=='VT01':
    f_co='Vistara'
if temp2[2]=='IG01':
    f_co='IndiGo'

name=temp2[0]
phno=temp2[1]
f_id=temp2[2]
fstartdate=temp2[3]
fstarttime=temp2[4]
seattype=temp2[5]
i=0
Label(winview,text=name,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=277)
Label(winview,text=phno,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=305)
Label(winview,text=f_id,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=360)
Label(winview,text=f_co,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=388)
Label(winview,text=fstartdate,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=443)
Label(winview,text=fstarttime,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=473)
Label(winview,text=seattype,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=525)
i=785
Label(winview,text=name,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=264)
Label(winview,text=phno,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=291)
Label(winview,text=f_id,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=342)
Label(winview,text=f_co,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=373)
Label(winview,text=fstartdate,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=428)
Label(winview,text=fstarttime,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=458)
Label(winview,text=seattype,font=('Comic Sans MS','14','normal'),bg='white',bd=2).place(x=200+i,y=510)

bthome=PhotoImage(file='homebutton2.png')
def homebt():
    winview.destroy()
    import main
Button(winview,image=bthome,command=homebt,bd=0,bg='#085c74').place(x=1215,y=0)
def Deletetk():
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="flights")
    my_conn = my_connect.cursor()
    que=mbox.askquestion('Delete Ticket','Are you sure you want to delete this ticket?',icon='warning')
    if que=='yes':
        my_conn.execute("DELETE FROM passengers WHERE fullname='"+name+"' AND phno='"+phno+"' AND f_id='"+f_id+"';")
        my_connect.commit()
        mbox.showinfo('Success','Ticket Cancelled')
        winview.destroy()
        import main
    else:
        pass
Button(winview,text='Cancel Ticket',command=Deletetk,bg='red',fg='white',font=('Comic Sans MS','14','bold')).place(x=1100,y=600)
winview.mainloop()
