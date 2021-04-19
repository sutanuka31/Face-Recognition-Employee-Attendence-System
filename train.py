from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import numpy as np
import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine=pyttsx3.init()
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Training Page")

        title_lbl = Label(self.root, text="TRAIN DATA SET  ", font=("times new roman", 30, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First img
        img_top = Image.open(r"E:\Face_recognition_system\Images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman", 30, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=0, y=350, width=1530, height=90)

        # second img
        img_bottom = Image.open(r"E:\Face_recognition_system\Images\photos.JPG")
        img_bottom = img_bottom.resize((1530, 280), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=280)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   # Grey scale image
            imageNp=np.array(img,'uint8')            # 'uint8'  =  datatype
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13        
        ids=np.array(ids)

        #  Train the classifier and save
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,ids)
        recognizer.write('trainer/trainer.yml')
        cv2.destroyAllWindows()
        engine.say("Training datasets completed")
        messagebox.showinfo("Result","Training datasets completed !!!!")
        engine.runAndWait()

if __name__== "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()