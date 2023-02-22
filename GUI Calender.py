from tkinter import*
import datetime
import calendar
root=Tk()
a=Label(root,text="year")
b=Label(root,text="month")
print(a,b)

c=Entry(root)
d=Entry(root)
a.pack()
c.pack()
b.pack()
d.pack()

def submit():
    e=int(c.get())
    g=int(d.get())
    x = calendar.month(e,g)

    z=Label(root, text = x).pack()

i=Button(root,text="submit",bg="green",command=submit).pack()

root.mainloop()
