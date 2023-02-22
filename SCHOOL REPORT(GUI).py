from tkinter import*
root=Tk()
a=Label(root,text="Username",bg="blue",fg="white").pack()
b=Entry(root,text="username").pack()
d=Label(root,text="Password",bg="red",fg="white").pack()
e=Entry(root,text="password").pack()
def Login():
    a = Tk()


    f=Label(a,text="Admin").pack()
    def new():
        x=Tk()
        j=Label(a,text="Upload Results").pack()
        #g=Button(x,text="NEW RESULTS",command=new).pack()
        '''x.mainloop()
        root.destroy()'''

    def create():
        y=Tk()
        k=Label(a,text="Username",bg="blue",fg="white").pack()
        l=Entry(a,text="Username").pack()
        m=Label(a,text="Password",bg="pink",fg="white")

        #h=Button(y,text="CREATE USER",command=create).pack()
        '''y.mainloop()
        root.destroy()'''

    def delete():
        z=Tk()
        p=Label(a,text="Delete User").pack()
        #i=Button(root,text="DELETE USER",command=delete).pack()
        '''z.mainloop()
        root.destroy()'''

    g = Button(a, text="NEW RESULTS",command=new).pack()
    h = Button(a, text="CREATE USER",command=create).pack()
    i = Button(a, text="DELETE USER",command=delete).pack()

    a.mainloop()
    #root.destroy()

f=Button(root,text="Login",command=Login).pack()

root.mainloop()

