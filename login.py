from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import numpy as np
from config.connect import connection
import os, sys
def login():
    global window
    window = Tk()

    window.title("Ứng dụng điểm danh nhân diện")

    window.geometry('900x500')
    window.resizable(False,False)

    global username_vertify
    global password_vertify
    username_vertify = StringVar()
    password_vertify = StringVar()

    #LEFT FRAME
    leftFrame = Frame(window,width="500", height="900")
    leftFrame.pack(side = LEFT)
    lbl = Label(leftFrame,text="Đăng nhập", fg="red", font=("Arial", 18)).place(x=150,y=30)

    lblUser = Label(leftFrame,text="Username",fg="green", font=("Arial", 11)).place(x=50,y=120)
    entryUser1 = Entry(leftFrame, font=("Arial", 13), textvariable=username_vertify)
    entryUser1.place(x=50, y=150, height="30",width="300")

    lblPass = Label(leftFrame,text="Password",fg="green", font=("Arial", 11)).place(x=50,y=190)
    entryPass1 = Entry(leftFrame, font=("Arial", 13), textvariable=password_vertify)
    entryPass1.place(x=50, y=220, height="30",width="300")

    btnLogin = Button(leftFrame, text="Đăng nhập", command=login_vertify)
    btnLogin.place(x=50, y=280)


    # RIGHT FRAME
    rightFrame = Frame(window,bg="white", width="400", height=900)
    rightFrame.pack(side = RIGHT)

    imgLogin = ImageTk.PhotoImage(Image.open("images/vku.png"))
    imgLoginLabel = Label(rightFrame,image=imgLogin,bg="white").place(x=50,y=150)

    window.mainloop()


def login_vertify():
    username =  username_vertify.get()
    password =  password_vertify.get()
    sql = "SELECT * FROM users WHERE username = %s and password = %s"
    val = (username, password)

    mydb = connection()
    mycursor = mydb.cursor()

    if username != "":
        if password != "":
               mycursor.execute(sql,val)
        else:
            print("Vui lòng nhập mật khẩu")
    else:
        print("Vui lòng nhập tài khoản")
    
    result = mycursor.fetchall()
    if result:
        print("Đăng nhập thành công")
        os.system('python Home.py')
        window.quit()
    else:
        print("Đăng nhập thất bại")
       
        
if __name__ == "__main__":
    login()

    






