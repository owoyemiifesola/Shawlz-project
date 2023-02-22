from tkinter import *
import tkinter.messagebox as messagebox
def login():
    code=d.get()
    passwd=f.get()
    if code=="" or password=="":
        messagebox.showerror("ERROR","Enter your username and password")
    elif code!= logincode or passwd!=password:
        messagebox.showerror("ERROR","Incorrect logincode or password")
    else:
        messagebox.showinfo("WELCOME","login successful!!!")
        root.destroy()
        new=Tk()
        h=Label(new,text="Product Name",bg="purple",fg="white").grid(pady=10,padx=15,row=0,column=0)
        i=Label(new,text="Price",bg="purple",fg="white").grid(pady=10,padx=15,row=1,column=0)
        j=Entry(new)
        k=Entry(new)
        j.grid(row=0,column=1)
        k.grid(row=1,column=1)
        def cal():
            x=j.get()
            y=int(k.get())
            z=y*0.15
            l=y-z
            m=Label(new,text=f"For your product{x}",bg="purple",fg="white").grid(pady=10,padx=15,row=3,column=1)
            n=Label(new,text=f"your bill is ${l}",bg="purple",fg="white").grid(pady=10,padx=15,row=4,column=2)

        o=Button(new,text="CALCULATE",command=cal).grid(row=2,column=1)




        new.mainloop()
root=Tk()
'''a="logincode"
b="password"'''
logincode="shawlzfashion815"
password="09876"
c=Label(root,text="Logincode",bg="green",fg="white").pack()
d=Entry(root)
d.pack()
e=Label(root,text="Password",bg="green",fg="white").pack()
f=Entry(root)
f.pack()
g=Button(root,text="Login",command=login).pack()

root.mainloop()
