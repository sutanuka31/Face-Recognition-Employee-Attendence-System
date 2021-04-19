from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine=pyttsx3.init()

class Register_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("5000x1000+0+0")
        self.root.title("Register Page")

        # text variables
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # #audio
        # engine=pyttsx3.init()
        

        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\register.jpg")
        img_three = img_three.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=6, width=1530, height=710)

        main_frame=Frame(self.root,bg="white")
        main_frame.place(x=10,y=100,width=700,height=500)

        title_lbl = Label(main_frame, text="Register Here", font=("times new roman", 30, "bold"),
                         fg="black",bg="white")
        title_lbl.place(x=130, y=20)

        # First Name
        attendanceId = Label(main_frame, text="First Name"+"*", font=("times new roman", 14, "bold"), bg="white",fg="red")
        attendanceId.place(x=50,y=100)

        attendanceId_entry = ttk.Entry(main_frame,textvariable=self.var_fname,width=20,font=("times new roman", 15, "bold"))
        attendanceId_entry.place(x=50,y=130)

        # Last name
        lastname = Label(main_frame, text="Last Name"+"*", font=("times new roman", 14, "bold"), bg="white",fg="red")

        lastname.place(x=370,y=100)

        self.l_entry = ttk.Entry(main_frame,textvariable=self.var_lname,width=20,font=("times new roman", 15))
        self.l_entry.place(x=370,y=130)

        # contact no
        contact = Label(main_frame, text="Contact No"+"*", font=("times new roman", 14, "bold"), bg="white",fg="red")
        contact.place(x=50,y=170)

        self.contact1 = ttk.Entry(main_frame,textvariable=self.var_contact,width=20,font=("times new roman", 15))
        self.contact1.place(x=50,y=200)

        # email
        email = Label(main_frame, text="Email"+"*", font=("times new roman", 14, "bold"), bg="white",fg="red")
        email.place(x=370,y=170)

        self.email1 = ttk.Entry(main_frame,textvariable=self.var_email,width=20,font=("times new roman", 15))
        self.email1.place(x=370,y=200)

        # security question
        security = Label(main_frame, text="Security Question:", font=("times new roman", 14, "bold"), bg="white",fg="red")
        security.place(x=50,y=240)


        proof_combo = ttk.Combobox(main_frame,textvariable=self.var_securityQ, font=("times new roman", 14, "bold"),state="readonly")
        proof_combo["values"] = (
        "Select","your childhood nickname","your birth place","your mother last name")
        proof_combo.current(0)
        proof_combo.place(x=50,y=270,width=210)

    
        # security answer
        security_a = Label(main_frame, text="Security Answer:", font=("times new roman", 14, "bold"), bg="white",fg="red")
        security_a.place(x=370,y=240)

        self.secutity1 = ttk.Entry(main_frame,textvariable=self.var_securityA,width=20,font=("times new roman", 15))
        self.secutity1.place(x=370,y=270)

        # password
        password = Label(main_frame, text="Password"+"*", font=("times new roman", 14, "bold"), bg="white",fg="red")
        password.place(x=50,y=310)

        self.password1 = ttk.Entry(main_frame,textvariable=self.var_pass,show='*',width=20,font=("times new roman", 15))
        self.password1.place(x=50,y=340)

        # confirm password
        c_pass = Label(main_frame, text="Confrom Password:", font=("times new roman", 14, "bold"), bg="white",fg="red")
        c_pass.place(x=370,y=310)

        self.c_pass1 = ttk.Entry(main_frame,textvariable=self.var_confpass,show='*',width=20,font=("times new roman", 15))
        self.c_pass1.place(x=370,y=340)

        # check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(main_frame,variable=self.var_check,text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # reset image
        img2 = Image.open(r"E:\Face_recognition_system\Images\unnamed.png")
        img2 = img2.resize((200, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Button(main_frame, image=self.photoimg2,command=self.reset_data,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        f_lbl.place(x=370, y=370, width=200,height=40)

        

        # First image
        img = Image.open(r"E:\Face_recognition_system\Images\register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Button(main_frame, image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        f_lbl.place(x=10, y=420, width=300)

        # second image
        img1 = Image.open(r"E:\Face_recognition_system\Images\login.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Button(main_frame, image=self.photoimg1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        f_lbl1.place(x=330, y=420, width=300)

        # register button function declare

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confrom Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and Conditions",parent=self.root)
        elif self.var_lname.get()=="":
                messagebox.showerror("Error","please enter lastname to proceed",parent=self.root)
        elif self.var_pass.get()=="":
            messagebox.showerror("Error","please enter password to proceed",parent=self.root)
        elif self.var_confpass.get()=="":
            messagebox.showerror("Error","please enter confrompass to proceed",parent=self.root)
        elif len(self.var_contact.get()) !=10:
            messagebox.showerror("Error","please enter 10 digit phone number to proceed",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("Error","please enter email to proceed",parent=self.root)
        else:
            conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                (

                                      self.var_fname.get(),
                                      self.var_lname.get(),
                                      self.var_contact.get(),
                                      self.var_email.get(),
                                      self.var_securityQ.get(),
                                      self.var_securityA.get(),
                                      self.var_pass.get()
                ))
            conn.commit()
            self.reset_data()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
            engine.say("Your Register has been successfully")
            engine.runAndWait()

        # Reset function
    def reset_data(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_securityQ.set("")
        self.var_securityA.set("")
        self.var_pass.set("")
        self.var_confpass.set("")
        self.var_check.set("")
        


    def return_login(self):
        self.root.destroy()

 

        


  




if __name__== "__main__":
    root = Tk()
    obj = Register_window(root)
    root.mainloop()