from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import numpy as np
from config.connect import connection
import os

def register():
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
    lbl = Label(leftFrame,text="Đăng ký", fg="red", font=("Arial", 18)).place(x=150,y=30)

    lblUser = Label(leftFrame,text="Username",fg="green", font=("Arial", 11)).place(x=50,y=120)
    entryUser1 = Entry(leftFrame, font=("Arial", 13), textvariable=username_vertify)
    entryUser1.place(x=50, y=150, height="30",width="300")

    lblPass = Label(leftFrame,text="Password",fg="green", font=("Arial", 11)).place(x=50,y=190)
    entryPass1 = Entry(leftFrame, font=("Arial", 13), textvariable=password_vertify)
    entryPass1.place(x=50, y=220, height="30",width="300")

    btnRegister = Button(leftFrame, text="Đăng ký", command=register_vertify)
    btnRegister.place(x=50, y=280)


    # RIGHT FRAME
    rightFrame = Frame(window,bg="white", width="400", height=900)
    rightFrame.pack(side = RIGHT)

    imgRegister = ImageTk.PhotoImage(Image.open("images/vku.png"))
    imgRegisterLabel = Label(rightFrame,image=imgRegister,bg="white").place(x=50,y=150)

    window.mainloop()


def register_vertify():
    username =  username_vertify.get()
    password =  password_vertify.get()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
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
    
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
        
if __name__ == "__main__":
    register()

    






