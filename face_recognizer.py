from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognization:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        # Label
        title_lbl = Label(self.root, text="FACE RECOGNIZATION", font=("times new roman", 30, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First img
        img_top = Image.open(r"E:\Face_recognition_system\Images\image1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

         # second img
        img_bottom = Image.open(r"E:\Face_recognition_system\Images\image3.jpg")
        img_bottom = img_bottom.resize((720, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=720, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman", 18, "bold"), bg="darkgreen",
                      fg="white")
        b1_1.place(x=250, y=590, width=200, height=40)

    # Attendence
    def mark_attendance(self,e,n,d):
        with open("admin.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((e not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{e},{n},{d},{dtString},{d1},Present")


    # face recognization
    def face_recog(self):
        # def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,recognizer):
        #     gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        #     coord=[]

        #     for (x,y,w,h) in features:
        #         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #         id,predict=recognizer.predict(gray_image[y:y+h,x:x+w])
        #         confidence=int((100*(1-predict/300)))


        #         conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
        #         my_cursor = conn.cursor()


        #         my_cursor.execute("Select emp_id from emp_table where emp_id="+str(id))
        #         e=my_cursor.fetchone()
        #         e="+".join(e)

        #         my_cursor.execute("Select Name from emp_table where emp_id="+str(id))
        #         n=my_cursor.fetchone()
        #         n="+".join(n)

        #         my_cursor.execute("Select Department from emp_table where emp_id="+str(id))
        #         d=my_cursor.fetchone()
        #         d="+".join(d)

        #         if confidence>77:
        #             cv2.putText(img,f"emp_id:{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             # self.mark_attendance(e,n,d)
        #         else:
        #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        #             cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

        #         coord=[x,y,w,h]
        #     return coord

        # def recognise(img,recognizer,faceCascade):
        #     coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",recognizer)
        #     return img

        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # recognizer = cv2.face.LBPHFaceRecognizer_create()
        # recognizer.read("trainer/trainer.yml")

        # video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # while True:
        #     ret,img = video_cap.read()
        #     img=recognise(img,recognizer,faceCascade)
        #     cv2.imshow("Welcome To Face Recognition",img)

        #     if cv2.waitKey(1)==13:
        #         break
        #     video_cap.release()
        #     cv2.destroyAllWindows()


        
            
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read('trainer/trainer.yml')   #load trained model
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascadePath);

            font = cv2.FONT_HERSHEY_SIMPLEX

            #iniciate id counter, the number of persons you want to include
            id = 2  #two persons



            names = ['','Arpita','sutanuka','unknown']  #key in names, start from the second place, leave first empty

            # Initialize and start realtime video capture
            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cam.set(3, 640)  # set video width
            cam.set(4, 480)  # set video height

            # Define min window size to be recognized as a face
            minW = 0.1*cam.get(3)
            minH = 0.1*cam.get(4)

            while True:

                ret, img = cam.read()

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int(minW), int(minH)),
                )
                i=0
                for(x, y, w, h) in faces:

                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    i += 1
                    id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

                    conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("Select emp_id from emp_table where emp_id="+str(id))
                    e=my_cursor.fetchone()
                    e="+".join(e)

                    my_cursor.execute("Select Name from emp_table where emp_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("Select Department from emp_table where emp_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)


                    # Check if confidence is less them 100 ==> "0" is perfect match
                    if i <= 1:
                        if (confidence < 100):
                            # id = names[id]
                            # confidence = "  {0}%".format(round(100 - confidence))
                            cv2.putText(img,f"emp_id:{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(6,4,78),3)
                            cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(6,4,78),3)
                            cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(6,4,78),3)
                            self.mark_attendance(e,n,d)
                        else:
                            id = "unknown"
                            confidence = "  {0}%".format(round(100 - confidence))
                    else:
                        cv2.putText(img, 'more then one face was detector' + str(i), (x + 50, y + w + 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
                    cv2.putText(img, 'face num' + str(i), (x + 50, y+w+20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                cv2.imshow('camera', img)

                if cv2.waitKey(1)==13:  # Press 'ESC' for exiting video
                # if k == 27:
                    break

            # Do a bit of cleanup
            print("\n [INFO] Exiting Program and cleanup stuff")
            cam.release()
            cv2.destroyAllWindows()


if __name__== "__main__":
    root = Tk()
    obj = Face_recognization(root)
    root.mainloop()