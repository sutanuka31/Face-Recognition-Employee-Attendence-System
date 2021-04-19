from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
import os
from train import Train
from face_recognizer import Face_recognization
from attendance import Attendance
from developer import Developer
# from password import Change_password
import tkinter
from time import strftime
from datetime import datetime
from helpdesk import Help_desk





class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img=Image.open(r"E:\Face_recognition_system\Images\facial-recognition-101-promo.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second image
        img_one = Image.open(r"E:\Face_recognition_system\Images\facialrecognition.png")
        img_one = img_one.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_one = ImageTk.PhotoImage(img_one)

        f_lbl = Label(self.root, image=self.photoimg_one)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # Third image
        img_two = Image.open(r"E:\Face_recognition_system\Images\Facial-Recognition-1024x483.jpg")
        img_two = img_two.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_two = ImageTk.PhotoImage(img_two)

        f_lbl = Label(self.root, image=self.photoimg_two)
        f_lbl.place(x=1000, y=0, width=500, height=130)
        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\BestFacialRecognition-1024x595.jpg")
        img_three = img_three.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Show current time
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl= Label(title_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
        lbl.place(x=8,y=0,width=110,height=50)
        time()


        # Employee button
        img_four = Image.open(r"E:\Face_recognition_system\Images\employee.jpg")
        img_four = img_four.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_four = ImageTk.PhotoImage(img_four)

        b1=Button(bg_img,image=self.photoimg_four,cursor="hand2",command=self.employee_details)
        b1.place(x=200, y=100, width=100, height=100)

        b1_1 = Button(bg_img,text="Employee Details", command=self.employee_details,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=200, y=200, width=100, height=30)

        # Detect face button
        img_five = Image.open(r"E:\Face_recognition_system\Images\FaceAnalysis.png")
        img_five = img_five.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_five = ImageTk.PhotoImage(img_five)

        b1 = Button(bg_img, image=self.photoimg_five, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=100, height=100)

        b1_1 = Button(bg_img, text="Face Recognizer", cursor="hand2",command=self.face_data, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=500, y=200, width=100, height=30)

        # Attendence button
        img_six = Image.open(r"E:\Face_recognition_system\Images\ATTENDANCE.png")
        img_six = img_six.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_six = ImageTk.PhotoImage(img_six)

        b1 = Button(bg_img, image=self.photoimg_six, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=100, height=100)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=800, y=200, width=100, height=30)

        # Help Desk button
        img_seven = Image.open(r"E:\Face_recognition_system\Images\help.jpg")
        img_seven = img_seven.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_seven = ImageTk.PhotoImage(img_seven)

        b1 = Button(bg_img, image=self.photoimg_seven, cursor="hand2",command=self.helpDesk)
        b1.place(x=1100, y=100, width=100, height=100)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.helpDesk, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=1100, y=200, width=100, height=30)

        # Train face button
        img_eight = Image.open(r"E:\Face_recognition_system\Images\detect.jpg")
        img_eight = img_eight.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_eight = ImageTk.PhotoImage(img_eight)

        b1 = Button(bg_img, image=self.photoimg_eight, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=100, height=100)

        b1_1 = Button(bg_img, text="Train System", cursor="hand2",command=self.train_data, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=200, y=480, width=100, height=30)

        # Photos button
        img_nine = Image.open(r"E:\Face_recognition_system\Images\photos.jpg")
        img_nine = img_nine.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_nine = ImageTk.PhotoImage(img_nine)

        b1 = Button(bg_img, image=self.photoimg_nine, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=100, height=100)

        b1_1 = Button(bg_img, text="Photo Samples", cursor="hand2",command=self.open_img, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=500, y=480, width=100, height=30)

        # Developer button
        img_ten = Image.open(r"E:\Face_recognition_system\Images\developer.jpg")
        img_ten = img_ten.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_ten = ImageTk.PhotoImage(img_ten)

        b1 = Button(bg_img, image=self.photoimg_ten, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=100, height=100)

        b1_1 = Button(bg_img, text="About Developer", cursor="hand2",command=self.developer_data,font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=800, y=480, width=100, height=30)

        # Exit button
        img_eleven = Image.open(r"E:\Face_recognition_system\Images\exit.jpeg")
        img_eleven = img_eleven.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_eleven = ImageTk.PhotoImage(img_eleven)

        b1 = Button(bg_img, image=self.photoimg_eleven, cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=100, height=100)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.exit, font=("times new roman", 10, "bold"), bg="black",
                      fg="white")
        b1_1.place(x=1100, y=480, width=100, height=30)

    def open_img(self):
        os.startfile("data")


    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return

    # Functions button
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)



    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognization(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def helpDesk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_desk(self.new_window)



if __name__== "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()