from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2

class Help_desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("5000x1000+0+0")
        self.root.title("Help Desk")

        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\help.png")
        img_three = img_three.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=6, width=1530, height=710)







if __name__== "__main__":
    root = Tk()
    obj = Help_desk(root)
    root.mainloop()