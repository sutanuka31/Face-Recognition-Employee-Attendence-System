from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
from register import Register_window
from main import face_recognition_system
import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine=pyttsx3.init()
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("5000x1000+0+0")
        self.root.title("Login Page")
         # text variables
        self.var_email = StringVar()
        self.var_pass = StringVar()

        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\biometric-digital.png")
        img_three = img_three.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=6, width=1530, height=710)

        # main_frame=Frame(self.root,bg="black")
        # main_frame.place(x=400,y=100,width=450,height=500)

        main_frame=Frame(self.root,bg="black")
        main_frame.place(x=10,y=100,width=500,height=500)

        title_lbl = Label(main_frame, text="Get Started", font=("times new roman", 30, "bold"),
                         fg="white",bg="black")
        title_lbl.place(x=110, y=20)

        # Label
        username=lbl=Label(main_frame,text="Username:",font=("times new roman", 15, "bold"),
                         fg="white",bg="black")
        username.place(x=39,y=155)

        self.txtuser=ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=350)

        # Label
        password=lbl=Label(main_frame,text="Password:",font=("times new roman", 15, "bold"),
                         fg="white",bg="black")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(main_frame,textvariable=self.var_pass,show='*',font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40,y=250,width=350)

         # Login button
        loginbtn=Button(main_frame,command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=150,y=300,width=120,height=50)

        # register button
        registerbtn=Button(main_frame,text="New User Register",command=self.register_button,font=("times new roman", 15, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=60,y=350,width=300)

        # forgot button
        forgotbtn=Button(main_frame,text="Forgot Password",command=self.forgot_password,font=("times new roman", 15, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=60,y=400,width=300)

        # reset button
        forgotbtn=Button(main_frame,text="Reset",command=self.reset_data,font=("times new roman", 15, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=70,y=440,width=300)

    # Login System

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="adminpass":
            messagebox.showinfo("Success","Welcome !!!!",parent=self.root)
        else:
            conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
            (
                self.var_email.get(),
                self.var_pass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                engine.say("Welcome to face recognition attendence system")
                engine.runAndWait()
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_recognition_system(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.reset_data()
            conn.close()


         # Reset function
    def reset_data(self):
        self.var_email.set("")
        self.var_pass.set("")
        


    
    # reset password
    def reset_password(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security question",parent=self.root2)
        elif self.secutity1.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.pass1.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.secutity1.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.pass1.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your Password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()

                self.txtuser.focus()









    # forgot password window
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset Password")
        else:
            conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                

                l=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                  # security question
                security = Label(self.root2, text="Select Security Question:", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security.place(x=50,y=80)


                self.combo_security = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"),state="readonly")
                self.combo_security["values"] = (
                "Select","your childhood nickname","your birth place","your mother last name")
                self.combo_security.current(0)
                self.combo_security.place(x=50,y=110,width=250)

    
                # security answer
                security_a = Label(self.root2, text="Security Answer:", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_a.place(x=50,y=150)

                self.secutity1 = ttk.Entry(self.root2,width=20,font=("times new roman", 15))
                self.secutity1.place(x=50,y=180,width=250)

                # new password
                new_pass = Label(self.root2, text="New Password:", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_pass.place(x=50,y=220)

                self.pass1 = ttk.Entry(self.root2,width=20,show='*',font=("times new roman", 15))
                self.pass1.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman", 15, "bold"), bg="green",fg="white")
                btn.place(x=150,y=290)
                




     # Functions button
    def register_button(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_window(self.new_window)

    def main_button(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition_system(self.new_window)
        

if __name__== "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()