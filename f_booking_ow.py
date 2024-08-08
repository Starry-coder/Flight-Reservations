from tkinter import Button, Entry
def booking_oneway():
    import tkinter as tk
    from tkinter import Canvas, Checkbutton, Frame, Label, OptionMenu, PhotoImage, StringVar, messagebox as mBox
    from tkinter.constants import ACTIVE, END
    from tkinter import messagebox as mbox
    import mysql.connector
    from mysql.connector import Error
    from PIL  import ImageTk ,Image
    import csv
    import pandas as pd
    import time

    #---------------------------------------------------------------
    owwin = tk.Tk()
    owwin.title('One Way Ticket Booking')
    owwin.resizable(0,0)
    owwin.iconbitmap('oneway.ico')
    owwin.geometry('1280x720')

    #--------------------------------------------------------------
    owbg= PhotoImage(file='onewaybgneww.png')
    owbgimg= Label(owwin, image=owbg)
    owbgimg.place(x=0,y=0,relwidth=1,relheight=1)
    bookkbtimg= PhotoImage(file='booknow.png')

    #--------------------------------------------------------------
    otemp=[]
    ou=open("temp7.csv",'r')
    oa=csv.reader(ou)
    for i in oa:
        otemp.append(i)
    ou.close()
    otemp2= otemp[-2]
    if otemp2[0]=='O':
        flighttype='One Way'
    else:
        flighttype='RounD Trip'
    my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="flights"
    )
    temp=[]
    u=open("temp2.csv",'r')
    a=csv.reader(u)
    for i in a:
        temp.append(i)
    u.close()
    temp2= temp[-2]
    print(temp2)
    my_conn = my_connect.cursor()
    if flighttype=='One Way':
        my_conn.execute("SELECT f_id,f_company,f_startdate,f_starttime,f_reachtime,f_enddate,f_price,f_startloc,f_endloc FROM flights where f_startdate='"+
                        temp2[0]+"'and f_startloc='"+temp2[1]+"' and f_endloc='"+temp2[2]+"';")
        i=0
        Label(owwin,text='Available Flights',fg='black',font=('Comic Sans MS','18','bold'),bg='white').place(x=560,y=47)
        Label(owwin,text='Flight ID',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=107)
        Label(owwin,text='Company',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=261,y=107)
        Label(owwin,text='Starting Date',fg='black',font=('Roboto Mono','9','bold'),bg='white').place(x=356,y=107)
        Label(owwin,text='Departure',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=495,y=107)
        Label(owwin,text='Arrival',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=620,y=107)
        Label(owwin,text='Ending Date',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=720,y=107)
        Label(owwin,text='Price',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=865,y=107)
        Label(owwin,text='Starts From',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=958,y=107)
        Label(owwin,text='Destination',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=1080,y=107)
        flightids=[]
        flightids.append('-SELECT-')
        flightstarttimes=[]
        for student in my_conn:
            
            for j in range(len(student)):
                e = Label(owwin,text=student[j], width=10, fg='black',font=('Roboto Mono','10','normal'),bg='white')
                e.place(y=150+i*43, x=130+j*120)
                if j%9==0:
                    print(student[j])
                    flightids.append(student[j])
                if j%9==3:
                    flightstarttimes.append(student[j])
            i=i+1
        seatslist=['Economy','Business Class']
        f_id = StringVar()
        seattype = StringVar()
        f_id.set( flightids[0])
        seattype.set(seatslist[0])
        drop = OptionMenu( owwin , f_id , *flightids )
        drop2 = OptionMenu(owwin,seattype,*seatslist)
        Label(owwin,text='Passenger Details',fg='black',font=('Comic Sans MS','14','bold'),bg='white').place(x=460,y=525)
        Label(owwin,text='Full Name:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=600)
        Label(owwin,text='Flight ID:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=560)
        Label(owwin,text='Phone Number:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=400,y=600)
        Label(owwin,text='Seat Type:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=700,y=600)
        p_fullname = tk.Entry(owwin,font=('Roboto Mono','10','normal'),width=16,borderwidth=2,bd=2)
        p_fullname.place(x=240,y=600)
        p_phno = tk.Entry(owwin,font=('Roboto Mono','10','normal'),width=16,borderwidth=2,bd=2)
        p_phno.place(x=540,y=600)
        drop.place(x=240,y=560)
        drop2.place(x=800,y=600)
    else:
        my_conn.execute("SELECT f_id,f_company,f_startdate,f_starttime,f_reachtime,f_enddate,f_price,f_startloc,f_endloc FROM flights where f_startdate='"+
                        temp2[0]+"'and f_startloc='"+temp2[1]+"' and f_endloc='"+temp2[2]+"' and f_returndate='"+temp2[3]+"';")
        i=0
        Label(owwin,text='Available Flights',fg='black',font=('Comic Sans MS','18','bold'),bg='white').place(x=560,y=47)
        Label(owwin,text='Flight ID',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=107)
        Label(owwin,text='Company',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=261,y=107)
        Label(owwin,text='Starting Date',fg='black',font=('Roboto Mono','9','bold'),bg='white').place(x=356,y=107)
        Label(owwin,text='Departure',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=495,y=107)
        Label(owwin,text='Arrival',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=620,y=107)
        Label(owwin,text='Ending Date',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=720,y=107)
        Label(owwin,text='Price',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=865,y=107)
        Label(owwin,text='Starts From',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=958,y=107)
        Label(owwin,text='Destination',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=1080,y=107)
        flightids=[]
        flightids.append('-SELECT-')
        flightstarttimes=[]
        for student in my_conn:
            for j in range(len(student)):
                e = Label(owwin,text=student[j], width=10, fg='black',font=('Roboto Mono','10','normal'),bg='white')
                e.place(y=150+i*43, x=130+j*120)
                if j%9==0:
                    flightids.append(student[j])
                if j%9==3:
                    flightstarttimes.append(student[j])
            i+=1
        seatslist=['Economy','Business Class']
        f_id = StringVar()
        seattype = StringVar()
        f_id.set( flightids[0])
        seattype.set(seatslist[0])
        drop = OptionMenu( owwin , f_id , *flightids )
        drop2 = OptionMenu(owwin,seattype,*seatslist)
        Label(owwin,text='Passenger Details',fg='black',font=('Comic Sans MS','14','bold'),bg='white').place(x=460,y=525)
        Label(owwin,text='Full Name:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=600)
        Label(owwin,text='Flight ID:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=130,y=560)
        Label(owwin,text='Phone Number:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=400,y=600)
        Label(owwin,text='Seat Type:',fg='black',font=('Roboto Mono','10','bold'),bg='white').place(x=700,y=600)
        p_fullname = tk.Entry(owwin,font=('Roboto Mono','10','normal'),width=16,borderwidth=2,bd=2)
        p_fullname.place(x=240,y=600)
        p_phno = tk.Entry(owwin,font=('Roboto Mono','10','normal'),width=16,borderwidth=2,bd=2)
        p_phno.place(x=540,y=600)
        drop.place(x=240,y=560)
        drop2.place(x=800,y=600)
        
    global tempindex
    tempindex= 0
    def bookticketow():
        global tempindex
        tempindex= 0
        my_conn2 = my_connect.cursor()
        for i in range(0,len(flightstarttimes)):
            if flightids[i]==f_id.get():
                tempindex+=i
        pfullname=p_fullname.get()
        pphno=p_phno.get()
        if len(pfullname)>0 and len(pphno)>0:
            print(tempindex)
            my_conn2.execute("insert into passengers(fullname,phno,f_id,f_startdate,f_starttime,f_startloc,f_endloc,seattype,tripytpe) values('"+pfullname+
                             "','"+pphno+"','"+f_id.get()+"','"+temp2[0]+"','"+flightstarttimes[tempindex]+"','"+temp2[1]+"','"+temp2[2]+"','"+seattype.get()+    
                             "','One Way');")
            my_connect.commit()
            mbox.showinfo('Success!','Your ticket has been booked!')
            owwin.destroy()
            import main
        else:
            mBox.showinfo('Error','Please Fill all the Entries!')
        #
    def bookticketrt():
        global tempindex
        tempindex= 0
        my_conn2 = my_connect.cursor()
        for i in range(0,len(flightstarttimes)):
            if flightids[i]==f_id.get():
                tempindex+=i
        pfullname=p_fullname.get()
        pphno=p_phno.get()
        if len(pfullname)>0 and len(pphno)>0:
            my_conn2.execute("insert into passengers(fullname,phno,f_id,f_startdate,f_starttime,f_startloc,f_endloc,seattype,tripytpe) values('"+pfullname+"','"+pphno+"','"+f_id.get()+"','"+temp2[0]+"','"+flightstarttimes[tempindex]+"','"+temp2[1]+"','"+temp2[2]+"','"+seattype.get()+"','One Way');")
            my_connect.commit()
            mbox.showinfo('Success!','Your ticket has been booked!')
            owwin.destroy()
            import main
        else:
            mBox.showinfo('Error','Please Fill all the Entries!')
        #
    def bookticket():
        if otemp2=='One Way':
            bookticketow()
        else:
            bookticketrt()

    bthome= PhotoImage(file='homebutton2.png')
    def homebt():
        owwin.destroy()
        import main
    Button(owwin,image=bthome,command=homebt,bd=0,bg='white').place(x=1215,y=0)
    Button(owwin,image=bookkbtimg,bd=0,bg='white',command=bookticket).place(x=500,y=650)

    #--------mainloop-----------------#
    owwin.mainloop()

booking_oneway()
