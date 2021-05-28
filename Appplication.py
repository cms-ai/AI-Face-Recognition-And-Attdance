from tkinter import*
from PIL import ImageTk
from tkinter import messagebox, filedialog, ttk
import pandas as pd
import mysql.connector
import numpy as np
from config.connect import connection
import os
import cv2
import face_recognition
from datetime import datetime
import shutil

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # BG Images
        self.bg = ImageTk.PhotoImage(file="images/login1.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame

        Frame_Login = Frame(self.root, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        titleLabel = Label(Frame_Login, text="Login Here",font=("Impact",32,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_user = Label(Frame_Login, text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
        self.txt_user = Entry(Frame_Login, font=("times new roman",15), bg="lightgray")
        self.txt_user.place(x=90, y= 140, width=350, height=35)

        lbl_pass = Label(Frame_Login, text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=180)
        self.txt_pass = Entry(Frame_Login, font=("times new roman",15), bg="lightgray")
        self.txt_pass.place(x=90, y= 210, width=350, height=35)

        forget = Button(Frame_Login, text="Forget Password?", bg="white",bd=0, fg="#d77337", font=("times new roman", 12)).place(x=90, y=250)
        Login_btn = Button(self.root, command=self.login_vertify, text="Login", fg="white", bg="#d77337", font=("times new roman", 18,"bold")).place(x=300, y=440, width=180, height=40)

    
    def login_vertify(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        sql = "SELECT * FROM users WHERE username = %s and password = %s"
        val = (username, password)

        mydb = connection()
        mycursor = mydb.cursor()
            # messagebox.showerror("Welcome", f"Welcome {self.txt_user}\nYour Password: {self.txt_pass}", parent=self.root)
            # self.root.withdraw()
            # topLevel = Toplevel(self.root)
            # app = Register(topLevel)
        
        if username != "":
            if password != "":
                mycursor.execute(sql,val)
            else:
                print("Vui lòng nhập mật khẩu")
        else:
            messagebox.showerror("Error", "All field are required")
    
        result = mycursor.fetchall()
        if result:
            # messagebox.showinfo("Welcome",f"Username: {username}\nPassword:{password}")
            self.root.withdraw()
            topLevel = Toplevel(self.root)
            app = Home(topLevel)
        else:
            print("Đăng nhập thất bại") 
            
class Home:
    def __init__(self,root):
        self.root = root
        self.root.title("Trang chủ-Author Trần Công Ái")
        self.root.geometry("1000x600+100+50")
        self.root.resizable(False, False)
        # BG Images
        frame_home = Frame(self.root,bg="white")
        frame_home.place(x=0,y=0, width=1000, height=600)

        self.lbl_ad = Label(frame_home, text="Admin", fg="black", bg ="white",font=("Goudy old style",12,"bold")).place(x=0, y=0)
        self.logout = Button(frame_home, text="Đăng xuất", bg="white", bd=0)
        self.logout.place(x=80, y=5)

        self.add_St = Button(frame_home, command=self.add_student_window, text="Thêm sinh viên", font=("times new roman",18,"bold"))
        self.add_St.place(x=100, y=400,width=170, height=80)

        self.add_St1 = Button(frame_home,command=self.add_attandance_window, text="Điểm danh", font=("times new roman",18,"bold"))
        self.add_St1.place(x=300, y=400,width=170, height=80)

        self.add_St = Button(frame_home, text="Quản lý", font=("times new roman",18,"bold"))
        self.add_St.place(x=500, y=400,width=170, height=80)

        self.add_St = Button(frame_home, text="Báo cáo", font=("times new roman",18,"bold"))
        self.add_St.place(x=700, y=400,width=170, height=80)
        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = Label(frame_home, image=self.bg1, bg="white").place(x=0, y=100, relwidth=1)
    def add_student_window(self):
        self.root.withdraw()
        topLevel = Toplevel(self.root)
        app = Student(topLevel)
    
    def add_attandance_window(self):
        self.root.withdraw()
        topLevel1 =  Toplevel(self.root)
        app1 = Attandance(topLevel1)

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm sinh viên-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=500, height=600)


        lbl_1 = Label(left_Frame, text="Thêm sinh viên",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = Label(left_Frame, text="Họ và tên", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=50, y=150)

        self.nameEntry = Entry(left_Frame,bg="#e0dede", bd=1, font=("times new roman",12))
        self.nameEntry.place(x=50, y=180, height=30, width=180)

        lbl_3 = Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=250, y=150)

        self.MSVEntry = Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.MSVEntry.place(x=250, y=180, height=30, width=180)

        lbl_4 = Label(left_Frame, text="Lớp", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_4.place(x=50, y=230)

        self.gradeEntry = Entry(left_Frame,bg="#e0dede",  font=("times new roman",12))
        self.gradeEntry.place(x=50, y=260, height=30, width=180)

        lbl_5 = Label(left_Frame, text="Khoa", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_5.place(x=250, y=230)
        khoaList = ["Khoa khoa học máy tính","Quản trị kinh doanh", "Công nghệ kỹ thuật máy tính"]
        self.value_inside = StringVar(root)
        self.value_inside.set("Chọn ngành học")
        self.khoaMenu =  OptionMenu(left_Frame, self.value_inside, *khoaList)
        self.khoaMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.khoaMenu.place(x=250, y=260, width=180)
        
        self.addPhoto = Button(left_Frame,command=self.addImage, text="Thêm hình ảnh", padx=30, pady=10) 
        self.addPhoto.place(x=150, y= 350)

        self.valueImage = StringVar()

        self.txtImg = Label(left_Frame,textvariable=self.valueImage)
        self.txtImg.place(x=150, y=400)
        
        btn_Submit = Button(left_Frame, command=self.addStudent, text="Lưu vào CSDL", font=("times new roman",13,"bold"))
        btn_Submit.place(x=80, y=450, height=50, width=300)

        #Right Frame
        right_frame = Frame(self.root,bg="lightgray")
        right_frame.place(x=500, y=0, width=500, height=600)

        self.bg1 = ImageTk.PhotoImage(file="images/vku.png")
        self.bg_image1 = Label(right_frame, image=self.bg1, bg="white").place(x=1, y=0, height=600, width=500)



    def addImage(self):
        filename = filedialog.askopenfilename(filetypes=(("image files","*.jpg"),("All files","*.*")))
        self.valueImage.set(filename)
        return filename
    def saveImage(self, filename,name):

        head_tail = os.path.split(filename)
        new_head = name + "-" + head_tail[1] 
        targetFolder = "F:/Tài liệu/tutorial/ai-recogation/ImagesAttandance/" + new_head 
        # print(targetFolder)


        try:
            shutil.copyfile(filename, targetFolder)    
            print(f"Thành công {new_head}")   

        except:
            print("Lỗi thất bại") 
    
        return new_head
    def addStudent(self):
        # ten, mssv, lop, khoa
        ten = self.nameEntry.get()
        mssv = self.MSVEntry.get()
        lop = self.gradeEntry.get()
        khoa = self.value_inside.get()
        filename = self.valueImage.get()
        print(filename)
        images = self.saveImage(filename,mssv)
        # images
        if ten == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập tên")
        elif mssv == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập mã sinh viên")
        elif lop == "":
            messagebox.showerror("Thông báo", "Vui lòng nhập lớp")
        elif mssv == "" or khoa=="Chọn ngành học":
            messagebox.showerror("Thông báo", "Vui lòng chọn khoa")
        else:
            try:
                mydb = connection()
                mycursor = mydb.cursor()

                sql = "INSERT INTO students (ten, mssv, lop, khoa, hinhanh) VALUES (%s, %s, %s, %s, %s)"
                val = (ten, mssv, lop, khoa, images)

                mycursor.execute(sql, val)

                result = mydb.commit()

                messagebox.showinfo("Thành công", "Thêm sinh viên thành công")   
            except mysql.connector.Error as error:
                messagebox.showerror("Thất lại", "Không thể thêm dữ liệu vào DB")  
                print(error)   
        # GUI


class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang điểm danh-Author Trần Công Ái")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False, False)

        left_Frame = Frame(self.root, bg="white")
        left_Frame.place(x=0,y=0,width=1000, height=350)

        lbl_1 = Label(left_Frame, text="Điểm danh",fg="red", bg="white", font=("times new roman",28,"bold"))
        lbl_1.place(x=0, y=30, relwidth=1)

        lbl_2 = Label(left_Frame, text="Họ và tên", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_2.place(x=80, y=100)

        self.nameEntry = Label(left_Frame, bd=1, font=("times new roman",12))
        self.nameEntry.place(x=80, y=130, height=40, width=180)

        lbl_3 = Label(left_Frame, text="MSSV", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_3.place(x=280, y=100)

        self.MSVEntry = Label(left_Frame,  font=("times new roman",12))
        self.MSVEntry.place(x=280, y=130, height=40, width=180)

        lbl_4 = Label(left_Frame, text="Lớp", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_4.place(x=480, y=100)

        self.gradeEntry = Label(left_Frame,  font=("times new roman",12))
        self.gradeEntry.place(x=480, y=130, height=40, width=180)

        lbl_5 = Label(left_Frame, text="Khoa", bg="white",fg="gray", font=("times new roman",12,"bold"))
        lbl_5.place(x=680, y=100)

        self.khoaEntry = Label(left_Frame,  font=("times new roman",12))
        self.khoaEntry.place(x=680, y=130, height=40, width=180)
        
        self.btnDiemDannh = Button(left_Frame, command=self.Attendance, text="Bắt đầu điểm danh", font=("times new roman",12))
        self.btnDiemDannh.place(x=0,y=280, width=400, height=50, relx=0.5, anchor=CENTER)


        right_Frame = Frame(self.root, bg="white")
        right_Frame.place(x=0,y=352,width=1000, height=248)

        self.tv = ttk.Treeview(right_Frame, columns=(1,2,3,4), show="headings", height=5)
        self.tv.place(x=0, y=0, relwidth=1)

        self.tv.heading(1, text="Name")
        self.tv.heading(2, text="Current Time")
        self.tv.heading(3, text="Current Time")
        self.tv.heading(4, text="Current Time")
        self.tv.heading(5, text="Current Time")

    def findEncode(self,images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(self,name):
        with open('Attendance.csv', 'r+', encoding='utf8') as f:
            myDataList = f.readlines()
            nameList = []
            newList =  []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[1])
            print(nameList)
            
            infoAttList = []
            newInfoArray = []
            newInfoArray =name.upper().split('-')

            mssv = newInfoArray[0]
            # print("mảng thông tin ")
            mydb = connection()
            mycursor = mydb.cursor()
            sql = "SELECT * FROM students WHERE mssv = %s"
            val = (mssv, )
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                i =0 
                while i < len(x):
                    newList.append(x[i])
                    i+=1
            
            print(nameList, mssv)
            if mssv  not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{newList[1]},{newList[2]},{newList[3]},{newList[4]},{dtString}')
            

    def Attendance(self):
        path = 'ImagesAttandance'
        images = []
        classNames = []
        myList = os.listdir(path)

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            # print(curImg)
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        encodeListKnown = self.findEncode(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1,x2,y2,x1 = faceLoc
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, name, (x1 + 6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    self.markAttendance(name)

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)

    


        

root = Tk()
obj = Home(root)
root.mainloop()