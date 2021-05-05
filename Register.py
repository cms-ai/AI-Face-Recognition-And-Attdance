from tkinter import *
from PIL import ImageTk, Image

import mysql.connector


window = Tk()

window.title("Ứng dụng điểm danh nhân diện")

window.geometry('900x500')
window.resizable(False,False)


def registerAccount():
    # print(entryUser1.get(), entryPass1.get())
    username =  entryUser1.get()
    password =  entryPass1.get()

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="test"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, pass) VALUES (%s, %s)"
    val = (username, password)

    if username != "" and password != "":
        mycursor.execute(sql, val)
    else:
        print("Không được để trống")

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


#LEFT FRAME
leftFrame = Frame(window,width="500", height="900")
leftFrame.pack(side = LEFT)
lbl = Label(leftFrame,text="Đăng ký", fg="red", font=("Arial", 18)).place(x=150,y=30)

lblUser1 = Label(leftFrame,text="Username",fg="green", font=("Arial", 11)).place(x=50,y=120)
entryUser1 = Entry(leftFrame,font=("Arial", 13))
entryUser1.place(x=50, y=150, height="30",width="300")

    
lblPass1 = Label(leftFrame,text="Password",fg="green", font=("Arial", 11)).place(x=50,y=190)
entryPass1= Entry(leftFrame, font=("Arial", 13))
entryPass1.place(x=50, y=220, height="30",width="300")



btnReg1 = Button(leftFrame, text="Đăng ký", command=registerAccount).place(x=50, y=280)
btnLogin1 = Button(leftFrame, text="Đăng nhập" ).place(x=150, y=280)



# RIGHT FRAME
rightFrame = Frame(window,bg="white", width="400", height=900)
rightFrame.pack(side = RIGHT)

imgLogin = ImageTk.PhotoImage(Image.open("images\login.png"))
imgLoginLabel = Label(rightFrame,image=imgLogin,bg="white").place(x=70,y=100)





window.mainloop()