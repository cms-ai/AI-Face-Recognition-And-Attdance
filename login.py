from tkinter import *
from PIL import ImageTk, Image


window = Tk()

window.title("Ứng dụng điểm danh nhân diện")

window.geometry('900x500')
window.resizable(False,False)
#LEFT FRAME
leftFrame = Frame(window,width="500", height="900")
leftFrame.pack(side = LEFT)
lbl = Label(leftFrame,text="Đăng nhập", fg="red", font=("Arial", 18)).place(x=150,y=30)

lblUser = Label(leftFrame,text="Username",fg="green", font=("Arial", 11)).place(x=50,y=120)
entryUser = Entry(leftFrame, font=("Arial", 13)).place(x=50, y=150, height="30",width="300")

lblPass = Label(leftFrame,text="Password",fg="green", font=("Arial", 11)).place(x=50,y=190)
entryPass = Entry(leftFrame, font=("Arial", 13)).place(x=50, y=220, height="30",width="300")

btnLogin = Button(leftFrame, text="Đăng nhập").place(x=50, y=280)
btnRegister = Button(leftFrame, text="Bạn chưa có tài khoản" ).place(x=150, y=280)



# RIGHT FRAME
rightFrame = Frame(window,bg="white", width="400", height=900)
rightFrame.pack(side = RIGHT)

imgLogin = ImageTk.PhotoImage(Image.open("images\login.png"))
imgLoginLabel = Label(rightFrame,image=imgLogin,bg="white").place(x=70,y=100)

window.mainloop()