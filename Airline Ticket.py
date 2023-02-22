from tkinter import*
import tkinter.messagebox as messagebox

root=Tk()
a=Label(root,text="Welcome to Shawlz airlines",bg="blue",fg="white").pack()
b=Label(root,text='''Choose a service
1.Book a flight
2.Reshedule a flight
3.Get a seat number
4.Track ticket''',bg="blue",fg="white").pack()
w=Entry(root)
w.pack()
def nxt():
    x=int(w.get())

    if x == 1:
        root.destroy()
        new = Tk()
        az = Label(new, text = "Shawlz Airlines,Lagos",bg="blue",fg="white")
        az.pack()
        bz = Label(new, text = """Choose an option:
        1.Local Flight
        2.International Flight""",bg="blue",fg="white")
        bz.pack()
        ab = Entry(new)
        ab.pack()

        def book():
            ax = int(ab.get())
            new.destroy()
            rootz = Tk()
            if ax == 1:
                b=Label(rootz,text= """Select State:
                1.LAGOS
                2.OSUN
                3.BENUE
                4.PORT HARCOURT
                5.FCT ABUJA""",bg="blue",fg="white")
                b.pack()
                c=Entry(rootz)
                c.pack()
                def locl():
                    x=int(c.get())
                    rootz.destroy()
                    if x==1 or x==2 or x==3 or x==4 or x==5:
                        messagebox.showinfo("THANK YOU.","You have successfully booked a Flight Ticket to your destination."
"Your date of flight and booking reference number will be sent to you via email.")
                dk=Button(rootz,text="Next",command=locl).pack()
            elif ax==2:
                b = Label(rootz, text="Select Country",bg="blue",fg="white").pack()
                c = Entry(rootz)
                c.pack()
                def inter():
                    x=c.get()
                    rootz.destroy()
                    messagebox.showinfo("THANK YOU.","You have successfully booked a Flight Ticket to your destination."
"Your date of flight and booking reference number will be sent to you via email.")
                dk=Button(rootz,text="Next",command=inter).pack()
                rootz.mainloop()
        dk = Button(new,text="NXT",command= book).pack()
    elif x==2:
        root.destroy()
        new=Tk()
        a = Label(new, text="Shawlz Airline,Lagos",bg="blue",fg="white").pack()
        b = Label(new, text="Flight number").pack()
        ab = Entry(new)
        ab.pack()
        ba=Label(new,text="New Date:DD-MM-YYYY",bg="blue",fg="white").pack()
        aa=Entry(new)
        aa.pack()
        def reshedule():
            x=int(ab.get())
            y=int(aa.get())
            new.destroy()
            messagebox.showinfo("THANK YOU.You have successfully resheduled your flight.","Your new date of flight will be sent via E-Mail.")
            
        d=Button(new,text="Next",command=reshedule).pack()
        new.mainloop()
        
    elif x==3:
        root.destroy()
        new = Tk()
        a = Label(new, text="Shawlz Airlines,Lagos",bg="blue",fg="white").pack()
        b = Label(new, text="Seating chart online",bg="blue",fg="white").pack()
        c = Label(new, text="Airline:e.g American Airlines",bg="blue",fg="white").pack()
        ac = Entry(new)
        ac.pack()
        d = Label(new, text="Date",bg="blue",fg="white").pack()
        ad = Entry(new)
        ad.pack()
        e = Label(new, text="Flight:e.g 101",bg="blue",fg="white").pack()
        ae = Entry(new)
        ae.pack()
        def find():
            x=ac.get()
            y=int(ad.get())
            y=int(ae.get())
            new.destroy()
            messagebox.showinfo("THANKS FOR USING THIS SERVICE","Your seat number will be shown on the boarding pass upon completion of check in.")
        d = Button(new,text="Next", command=find).pack()
        new.mainloop()
    elif x==4:
        root.destroy()
        new=Tk()
        a = Label(new, text="Shawlz Airlines,Lagos",bg="blue",fg="white").pack()
        b = Label(new, text="Flight status; Enter your departing and arriving destination :",bg="blue",fg="white").pack()
        ab= Entry(new)
        ab.pack() 
        c = Label(new, text="Date of travel",bg="blue",fg="white").pack()
        ac= Entry(new)
        ac.pack()
        d = Label(new, text="Booking reference number:",bg="blue",fg="white").pack()
        ad= Entry(new)
        ad.pack()
        e = Label(new, text="Flight number",bg="blue",fg="white").pack()
        ae= Entry(new)
        ae.pack() 
     
        f=Label(new,text="E-Mail",bg="blue",fg="white").pack()
        af=Entry(new)
        af.pack()
        def track():
            w=ab.get() 
            x=ac.get()
            y=ad.get()
            z=ae.get()
            new.destroy()
            messagebox.showinfo("THANKS FOR YOUR PATIENCE.","Your flight details will be sent to your E-Mail shortly")
            
        g=Button(new,text="Search Flight",command=track).pack()
        new.mainloop()


d=Button(root,text="Next",command=nxt).pack()

root.mainloop()
