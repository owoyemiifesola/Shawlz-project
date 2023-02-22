import mysql.connector
from tkinter import*
'''con=mysql.connector.connect(host="localhost",user="root",password="",database="StudentReport")

mycursor=con.cursor()'''

def Login():
    root.destroy()
    def new():
        a.destroy()
        x=Tk()
        x.geometry('400x170')
        j=Button(x,text="Upload Results",command=None).pack()
        #g=Button(x,text="NEW RESULTS",command=new).pack()
        con=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor=con.cursor()
        mycursor.execute("DROP DATABASE IF EXISTS NEWRESULTS")

        """mycursor.execute("CREATE DATABASE NEWRESULTS")
        mycursor.execute("USE NEWRESULTS")
        mycursor.execute("CREATE TABLE NEWRESULTSINFO(NAME VARCHAR(30),SURNAME VARCHAR(20),CLASS VARCHAR(4),MATHSMARKS CHAR(3),ENGMARKS CHAR(3),GOVTMARKS CHAR(3),LITMARKS CHAR(3),CRSMARKS CHAR(3),ECONOMICSMARKS CHAR(3))")
        sql="""INSERT INTO NEWRESULTSINFO(NAME,SURNAME,CLASS,MATHSMARKS,ENGMARKS,GOVTMARKS,LITMARKS,CRSMARKS,ECONOMICSMARKS)VALUES(%s,%s,%s,%d,%d,%d,%d,%d,%d)"""
        rows=[('JAMES','AFOLABI','SS4',70,60,80,75,80,75),('TURAYO','COKER','SS4',79,80,85,90,78,87),('JANE','DANIELS','SS3',70,68,87,89,79,80),('VICTOR','OWONIKOKO','SS3',65,76,79,86,90,75)]
        mycursor.executemany(sql,rows)
        con.commit()
        con.close()"""

        a.mainloop()
    def create():
        a.destroy()
        y=Tk()
        y.geometry('400x170')
        k=Label(y,text="Username",bg="blue",fg="white").pack()
        l=Entry(y,text="Username").pack()
        m=Label(y,text="Password",bg="pink",fg="white").pack()
        n=Entry(y,text="password").pack()

        h=Button(y,text="LOGIN",command=create).pack()
        y.mainloop()

    def delete():
        a.destroy()
        z = Tk()
        z.geometry('400x170')
        p = Label(a, text="Delete User").pack()
        z.mainloop()

    a = Tk()
    a.geometry('400x170')
    f=Label(a,text="Admin").pack()
    g = Button(a, text="NEW RESULTS", command=new).pack()
    h = Button(a, text="CREATE USER", command=create).pack()
    i = Button(a, text="DELETE USER", command=delete).pack()

    a.mainloop()



root=Tk()
root.geometry('400x170')
a=Label(root,text="Username",bg="blue",fg="white").pack(pady=10)
b=Entry(root,text="username").pack()
d=Label(root,text="Password",bg="red",fg="white").pack(pady=10)
e=Entry(root,text="password").pack()
f=Button(root,text="Login",command=Login).pack(pady=10)

root.mainloop()


