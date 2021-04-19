from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Page")

        # Label
        title_lbl = Label(self.root, text="DEVELOPER PAGE", font=("times new roman", 30, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=150, y=0, width=1000, height=45)

        # Second image
        img_one = Image.open(r"E:\Face_recognition_system\Images\image7.png")
        img_one = img_one.resize((2000, 800), Image.ANTIALIAS)
        self.photoimg_one = ImageTk.PhotoImage(img_one)

        f_lbl = Label(self.root, image=self.photoimg_one)
        f_lbl.place(x=0, y=45, width=2000, height=800)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=100,y=10,width=1100,height=60)


        # Developer info
        dev_label = Label(main_frame, text="Hello my name is Sutanuka Das.In this project I use Opencv,Pillow,Tkinter,speech_recognition and backend Mysql database.", font=("times new roman", 15, "bold"), bg="white")
        dev_label.place(x=0,y=5)
        




if __name__== "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()