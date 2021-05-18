from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from config.connect import connection
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

        self.add_St = Button(frame_home, text="Điểm danh", font=("times new roman",18,"bold"))
        self.add_St.place(x=300, y=400,width=170, height=80)

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
        value_inside = StringVar(root)
        value_inside.set("Chọn ngành học")
        self.khoaMenu =  OptionMenu(left_Frame, value_inside, *khoaList)
        self.khoaMenu.config(font=("times new roman",12), bg="#e0dede", bd=0)
        self.khoaMenu.place(x=250, y=260, width=180)

        btn_Submit = Button(left_Frame, text="Lưu vào CSDL", font=("times new roman",13,"bold"))
        btn_Submit.place(x=80, y=350, height=50, width=300)

    
root = Tk()
obj = Student(root)
root.mainloop()