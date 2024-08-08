#------------------------------IMPORT------------------------------------#
import tkinter as tk
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox as mBox
from tkinter.constants import END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image  #If you dont have it, use "pip install pillow"
import csv
#----------------------------Window details------------------------------#
win_login = tk.Tk()
win_login.title('AV Airlines Management')
win_login.resizable(0, 0)
win_login.geometry("1280x720")
win_login.iconbitmap('Flights.ico')
#-----------------Images------------------------------------------------#
loginbgwin= Image.open('loginbg.png')
loginbgcan=ImageTk.PhotoImage(loginbgwin)
l1= Label(win_login, image=loginbgcan)
l1.place(x=0,y=0,relwidth=1,relheight=1)

#------------------LABELS------------------------------------------------#
l_airmgmt= Label(win_login,text='Airlines Management',font=('Algerian','25','bold'),bg='#99d9ea')
l_login= Label(win_login,text='Please Login',font=("Arial", "20", "normal"),bg ='#99d9ea')
l_usr  = Label(win_login,text='Your User ID: ',bg='#99d9ea')
l_psw  =tk.Label(win_login,text='Your Password: ',bg='#99d9ea')
l_airmgmt.place(x=820,y=190)
l_login.place(x=958, y=250)
l_usr.place(x=800, y=300)
l_psw.place(x=800, y=350)
#-------------------Entry Boxes------------------------------------------#
usr = tk.Entry(win_login,width=50, fg= 'red',borderwidth=4,bg='#99d9ea')
psw = tk.Entry(win_login,width=50, fg='green',borderwidth=4,bg='#99d9ea', show='*')
usr.place(x=900, y=300)
psw.place(x=900, y=350)
#-------------------Defined Functions------------------------------------#
def login_attempt():
    conn = mysql.connector.connect(host='localhost',
                            database='flights',
                            user='root',
                            password='root',
                            charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login where usr_id='"+usr.get()+"' and pas='"+psw.get()+"'")
    ls = cursor.fetchall()
    ls=list(ls)
    if(len(ls)>0):
        mbox.showinfo('Congrats!', 'Welcome '+str(ls[0][1]))
        ls22=[str(ls[0][1])]
        g=open("temp3.csv", 'a')
        w=csv.writer(g)
        wobj=w.writerow(ls22)
        g.close()
        win_login.destroy()
        import main

    else:
        mbox.showinfo('Error!', 'Enter correct user id or password')
        #print('Error!', 'Enter correct user id or password')
        usr.delete(0,END)
        psw.delete(0,END)
#--------------------------Images-------------------------------#
exitimage=Image.open("loginbutton.png")
exitimgresize=exitimage.resize((155,50),Image.ANTIALIAS)
exitimg=ImageTk.PhotoImage(exitimgresize)
#--------------------------Buttons------------------------------#
b1=tk.Button(win_login,image=exitimg,borderwidth=0,command=login_attempt,bg='#99d9ea')
b1.place(x=970, y=375)
#------------------------run---------------------#
win_login.bind('<Return>',lambda event:login_attempt())
#-------------------------mainloop--------------------#
win_login.mainloop()