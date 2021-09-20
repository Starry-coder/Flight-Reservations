#------------------------------IMPORT------------------------------------#
import tkinter as tk
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox as mBox
from tkinter.constants import END
from tkinter import messagebox as mbox
import mysql.connector
from mysql.connector import Error
from PIL  import ImageTk ,Image  #If you dont have it, use "pip install pillow"


#----------------------------Window details------------------------------#
win_login = tk.Tk()
win_login.title('AV Airlines Management')

'''win_login.minsize(720, 405)
win_login.maxsize(720, 405)'''
win_login.resizable(0, 0)
win_login.geometry("1280x720")
win_login.iconbitmap('Flights.ico')
#win_login.wm_attributes('-transparentcolor','hole')





#-----------------Images------------------------------------------------#
loginbgwin= Image.open('Passenger_Airplanes_Sky_500758_1366x768.png')
loginbgcan=ImageTk.PhotoImage(loginbgwin)
l1= Label(win_login, image=loginbgcan)
l1.place(x=0,y=0,relwidth=1,relheight=1)


#-----------------Canvases-----------------------------------------------#
'''canvas_login= Canvas(win_login,width=1280,height=720)
canvas_login.pack(side='top', fill='both', expand='yes')
canvas_login.create_image(0,0,image=loginbgcan,anchor='nw')'''


#-----------------Frames------------------------------------------------#



#------------------LABELS------------------------------------------------#
l_airmgmt= Label(win_login,text='Airlines Management',font=('Algerian','25','bold'),bg='#99d9ea')
l_login= Label(win_login,text='Please Login',font=("Arial", "20", "normal"),bg ='#99d9ea')
l_usr  = Label(win_login,text='Your User ID: ',bg='#99d9ea')

l_psw  =tk.Label(win_login,text='Your Password: ',bg='#99d9ea')

'''
l_login.grid(row=0,column=15)
l_usr.grid(row=1,column=10)
l_psw.grid(row=2,column=10)
'''
l_airmgmt.place(x=820,y=190)
l_login.place(x=958, y=250)
l_usr.place(x=800, y=300)
l_psw.place(x=800, y=350)

#-------------------Entry Boxes------------------------------------------#

usr = tk.Entry(win_login,width=50, fg= 'red',borderwidth=4,bg='#99d9ea')
psw = tk.Entry(win_login,width=50, fg='green',borderwidth=4,bg='#99d9ea')
'''
usr.grid(row=1,column=11)
psw.grid(row=2,column=11)
'''
usr.place(x=900, y=300)
psw.place(x=900, y=350)


#-------------------Defined Functions------------------------------------#
def myclick():

    print(usr.get())
    print(psw.get())


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
        #print('Congrats!', 'Welcome '+str(ls[0][1]))

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

#b1= tk.Button(win, text='Click Me!',padx=50,pady=30,command=login_attempt)
b1=tk.Button(win_login,image=exitimg,borderwidth=0,command=login_attempt,bg='#99d9ea')
#b1.grid(row=4,column=15)
b1.place(x=970, y=375)




#------------------------run---------------------#
win_login.mainloop()

input()

