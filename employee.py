from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import speech_recognition as sr
import pyttsx3
from tkcalendar import Calendar,DateEntry


listener=sr.Recognizer()
engine=pyttsx3.init()

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Details")

        # variables create
        self.var_emp_Department=StringVar()
        self.va_Emp_Id = StringVar()
        self.var_emp_Name = StringVar()
        self.var_emp_Dob = StringVar()
        self.var_emp_Doj = StringVar()
        self.var_emp_Gender = StringVar()
        self.var_emp_Proof_Number = StringVar()
        self.var_emp_Address = StringVar()
        self.var_emp_Email = StringVar()
        self.var_emp_Contact_No = StringVar()
        self.var_emp_Proof_type = StringVar()
        # self.var_PhotoSample = StringVar()



        # First image
        img = Image.open(r"E:\Face_recognition_system\Images\photo1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second image
        img_one = Image.open(r"E:\Face_recognition_system\Images\photo3.jpg")
        img_one = img_one.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_one = ImageTk.PhotoImage(img_one)

        f_lbl = Label(self.root, image=self.photoimg_one)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # Third image
        img_two = Image.open(r"E:\Face_recognition_system\Images\photo2.jpg")
        img_two = img_two.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_two = ImageTk.PhotoImage(img_two)

        f_lbl = Label(self.root, image=self.photoimg_two)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\face.jpg")
        img_three = img_three.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="EMPLOYEE ATTENDANCE SYSTEM  ", font=("times new roman", 30, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1335,height=600)

        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Manage Employee",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=630,height=500)

        # Manage employee
        manage_employee = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        manage_employee.place(x=15, y=30, width=620, height=100)

        # Department
        emp_label=Label(manage_employee,text="Department",font=("times new roman",12,"bold"),bg="white")
        emp_label.grid(row=0,column=0,padx=10,sticky=W)

        emp_combo=ttk.Combobox(manage_employee,textvariable=self.var_emp_Department,font=("times new roman",12,"bold"),state="read only",width=20)
        emp_combo["values"]=("Select Department","IT","Sales","HR","Manager","Software Engineer","Software Devleloper","Application Developer")
        emp_combo.current(0)
        emp_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Gender
        gender_label = Label(manage_employee, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=0, column=2, padx=10,sticky=W)

        gender_combo = ttk.Combobox(manage_employee,textvariable=self.var_emp_Gender, font=("times new roman", 12, "bold"), state="read only",width=20)
        gender_combo["values"] = (
        "Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Proof Type
        proof_label = Label(manage_employee, text="Proof Type", font=("times new roman", 12, "bold"), bg="white")
        proof_label.grid(row=1, column=0, padx=10,sticky=W)

        proof_combo = ttk.Combobox(manage_employee,textvariable=self.var_emp_Proof_type, font=("times new roman", 12, "bold"), state="read only",width=20)
        proof_combo["values"] = (
        "Proof Type", "Pan Card", "Adhar Card", "Voter Card")
        proof_combo.current(0)
        proof_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # middile image
        img_left = Image.open(r"E:\Face_recognition_system\Images\facialrecognition.png")
        img_left = img_left.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_img = Label(Left_frame,image=self.photoimg_left)
        left_img.place(x=4, y=100, width=620, height=100)


        # Manage employee - 1
        manage_employee_one = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                     font=("times new roman", 12, "bold"))
        manage_employee_one.place(x=15, y=200, width=620, height=300)

        # Employee ID
        employeeId_label = Label(manage_employee_one, text="EmployeeID", font=("times new roman", 12, "bold"), bg="white")
        employeeId_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        employeeId_entry = ttk.Entry(manage_employee_one,textvariable=self.va_Emp_Id,width=20,font=("times new roman", 12, "bold"))
        employeeId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        name_label = Label(manage_employee_one, text="Name", font=("times new roman", 12, "bold"),
                                 bg="white")
        name_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        Name_entry = ttk.Entry(manage_employee_one,textvariable=self.var_emp_Name, width=20, font=("times new roman", 12, "bold"))
        Name_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        # Email
        email_label = Label(manage_employee_one, text="Email", font=("times new roman", 12, "bold"),
                           bg="white")
        email_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        email_entry = ttk.Entry(manage_employee_one,textvariable=self.var_emp_Email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)

        # Contact no
        contact_label = Label(manage_employee_one, text="Contact No", font=("times new roman", 12, "bold"),
                           bg="white")
        contact_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        contact_entry = ttk.Entry(manage_employee_one,textvariable=self.var_emp_Contact_No, width=20, font=("times new roman", 12, "bold"))
        contact_entry.grid(row=1, column=3, padx=10,pady=5, sticky=W)

        # D.O.B
        dob_label = Label(manage_employee_one, text="D.O.B", font=("times new roman", 12, "bold"),
                           bg="white")
        dob_label.grid(row=2, column=0, padx=10,pady=5, sticky=W)

        dob_entry =DateEntry(manage_employee_one,textvariable=self.var_emp_Dob,bg="darkblue",fg="white",year=2021, width=18, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)
        
        # cal = DateEntry(manage_employee_one,width=30,bg="darkblue",fg="white",year=2020)
        # cal.grid()

        # D.O.J
        doj_label = Label(manage_employee_one, text="D.O.J", font=("times new roman", 12, "bold"),
                           bg="white")
        doj_label.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        doj_entry =DateEntry(manage_employee_one,textvariable=self.var_emp_Doj,bg="darkblue",fg="white",year=2021, width=18, font=("times new roman", 12, "bold"))
        doj_entry.grid(row=2, column=3, padx=10,pady=5, sticky=W)

        # Proof Number
        proof_number_label = Label(manage_employee_one, text="Proof Number", font=("times new roman", 12, "bold"),
                           bg="white")
        proof_number_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        proof_number_entry = ttk.Entry(manage_employee_one,textvariable=self.var_emp_Proof_Number, width=20, font=("times new roman", 12, "bold"))
        proof_number_entry.grid(row=3, column=1, padx=10,pady=5, sticky=W)

        # Address
        address_label = Label(manage_employee_one, text="Address", font=("times new roman", 12, "bold"),
                           bg="white")
        address_label.grid(row=3, column=2, padx=10,pady=5, sticky=W)

        address_entry = ttk.Entry(manage_employee_one,textvariable=self.var_emp_Address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=3, padx=10,pady=5, sticky=W)


        # Radio buttons
        self.var_radio1 = StringVar()
        radiobutton1=ttk.Radiobutton(manage_employee_one,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobutton1.grid(row=5,column=0)

        radiobutton2 = ttk.Radiobutton(manage_employee_one,variable=self.var_radio1, text="No photo sample", value="No")
        radiobutton2.grid(row=5, column=1)

        # Buttons frame
        btn_frame=Frame(manage_employee_one,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=600,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman", 12, "bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=16, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=16, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=16, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        reset_btn.grid(row=0, column=3)

        # Buttons frame - 1
        btn_frame1 = Frame(manage_employee_one, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=220, width=600, height=35)
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=32, font=("times new roman", 12, "bold"), bg="black",
                           fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=32, font=("times new roman", 12, "bold"), bg="black",
                           fg="white")
        update_photo_btn.grid(row=1, column=1)


        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee Details",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=660,y=10, width=660, height=500)

        # Right label image
        img_right = Image.open(r"E:\Face_recognition_system\Images\facialrecognition.png")
        img_right = img_right.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        left_img = Label(Right_frame, image=self.photoimg_right)
        left_img.place(x=4, y=3, width=650, height=100)

        # Search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=4, y=110, width=650, height=50)
        # Search bar
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"),
                              bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        # Search combo
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="read only", width=15)
        search_combo["values"] = (
            "Select", "Proof Number", "Contact number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # search entry
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Search button
        search_btn = Button(search_frame, text="Search", width=15, font=("times new roman", 10, "bold"), bg="black",
                            fg="white")
        search_btn.grid(row=0, column=3,padx=4)

        showall_btn = Button(search_frame, text="Show All", width=15, font=("times new roman", 10, "bold"), bg="black",
                            fg="white")
        showall_btn.grid(row=0, column=4,padx=4)

        # table frame
        table_frame =Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=4, y=165, width=650, height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_data=ttk.Treeview(table_frame,column=("emp_id","name","department","dob","doj","gender","proof_type","proof_number","address","email","contact_no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_data.xview)
        scroll_y.config(command=self.employee_data.yview)  

        self.employee_data.heading("emp_id",text="EmployeeID")
        self.employee_data.heading("name", text="Name")
        self.employee_data.heading("department", text="Department")
        self.employee_data.heading("dob", text="D.O.B")
        self.employee_data.heading("doj", text="D.O.J")
        self.employee_data.heading("gender", text="Gender")
        self.employee_data.heading("proof_type", text="Proof Type")
        self.employee_data.heading("proof_number", text="Proof Number")
        self.employee_data.heading("address", text="Address")
        self.employee_data.heading("email", text="Email")
        self.employee_data.heading("contact_no", text="Contact No")
        self.employee_data.heading("photo", text="Photo Sample status")
        self.employee_data["show"]="headings"

        self.employee_data.column("emp_id", width=100)
        self.employee_data.column("name", width=100)
        self.employee_data.column("department", width=100)
        self.employee_data.column("dob", width=100)
        self.employee_data.column("doj", width=100)
        self.employee_data.column("gender", width=100)
        self.employee_data.column("proof_type", width=150)
        self.employee_data.column("proof_number", width=100)
        self.employee_data.column("address", width=100)
        self.employee_data.column("email", width=150)
        self.employee_data.column("contact_no", width=100)
        self.employee_data.column("photo", width=100)

        self.employee_data.pack(fill=BOTH,expand=1)
        self.employee_data.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # Function declration
    def add_data(self):
        if self.var_emp_Department.get()=="Select Department" or self.var_emp_Name.get()=="" or self.va_Emp_Id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            # messagebox.showinfo("success","welcome")
            try:
                conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into emp_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.va_Emp_Id.get(),
                                      self.var_emp_Name.get(),
                                      self.var_emp_Department.get(),
                                      self.var_emp_Dob.get(),
                                      self.var_emp_Doj.get(),
                                      self.var_emp_Gender.get(),
                                      self.var_emp_Proof_type.get(),
                                      self.var_emp_Proof_Number.get(),
                                      self.var_emp_Address.get(),
                                      self.var_emp_Email.get(),
                                      self.var_emp_Contact_No.get(),
                                      self.var_radio1.get(),   
                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","employee details has been added successfully",parent=self.root)
                engine.say("employee details has been added successfully")
                engine.runAndWait()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    # Fetch data
    def fetch_data(self):
        conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from emp_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_data.delete(*self.employee_data.get_children())
            for i in data:
                self.employee_data.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # Get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.employee_data.focus()
        content=self.employee_data.item(cursor_focus)
        data=content["values"]

        self.va_Emp_Id.set(data[0]),
        self.var_emp_Name.set(data[1]),
        self.var_emp_Department.set(data[2]),
        self.var_emp_Dob.set(data[3]),
        self.var_emp_Doj.set(data[4]),
        self.var_emp_Gender.set(data[5]),
        self.var_emp_Proof_type.set(data[6]),
        self.var_emp_Proof_Number.set(data[7]),
        self.var_emp_Address.set(data[8]),
        self.var_emp_Email.set(data[9]),
        self.var_emp_Contact_No.set(data[10]),
        self.var_radio1.set(data[11])

    # Update function
    def update_data(self):
        if self.var_emp_Department.get()=="Select Department" or self.var_emp_Name.get()=="" or self.va_Emp_Id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this employee details",parent=self.root)
                if update>0:
                    conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update emp_table set Name=%s,Department=%s,DOB=%s,DOJ=%s,Gender=%s,Proof_type=%s,Proof_number=%s,Address=%s,Email=%s,Contact_no=%s,PhotoSample=%s where emp_id=%s",
                    (
                                      self.var_emp_Name.get(),
                                      self.var_emp_Department.get(),
                                      self.var_emp_Dob.get(),
                                      self.var_emp_Doj.get(),
                                      self.var_emp_Gender.get(),
                                      self.var_emp_Proof_type.get(),
                                      self.var_emp_Proof_Number.get(),
                                      self.var_emp_Address.get(),
                                      self.var_emp_Email.get(),
                                      self.var_emp_Contact_No.get(),
                                      self.var_radio1.get(),  
                                      self.va_Emp_Id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Employee details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    # Delete function
    def delete_data(self):
        if self.va_Emp_Id.get()=="":
            messagebox.showerror("Error","Employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee delete page","Do you want to delete this employee",parent=self.root)
                if delete>0:
                    conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from emp_table where emp_id=%s"
                    val=(self.va_Emp_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    # Reset function
    def reset_data(self):
        self.va_Emp_Id.set("")
        self.var_emp_Name.set("")
        self.var_emp_Department.set("Select Department")
        self.var_emp_Dob.set("")
        self.var_emp_Doj.set("")
        self.var_emp_Gender.set("Select Gender")
        self.var_emp_Proof_type.set("Select Proof Type")
        self.var_emp_Proof_Number.set("")
        self.var_emp_Address.set("")
        self.var_emp_Email.set("")
        self.var_emp_Contact_No.set("")
        self.var_radio1.set("")

    # Generate data set or take photo samples
    def generate_dataset(self):
        if self.var_emp_Department.get()=="Select Department" or self.var_emp_Name.get()=="" or self.va_Emp_Id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from emp_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update emp_table set Name=%s,Department=%s,DOB=%s,DOJ=%s,Gender=%s,Proof_type=%s,Proof_number=%s,Address=%s,Email=%s,Contact_no=%s,PhotoSample=%s where emp_id=%s",
                     (
                                      self.var_emp_Name.get(),
                                      self.var_emp_Department.get(),
                                      self.var_emp_Dob.get(),
                                      self.var_emp_Doj.get(),
                                      self.var_emp_Gender.get(),
                                      self.var_emp_Proof_type.get(),
                                      self.var_emp_Proof_Number.get(),
                                      self.var_emp_Address.get(),
                                      self.var_emp_Email.get(),
                                      self.var_emp_Contact_No.get(),
                                      self.var_radio1.get(),  
                                      self.va_Emp_Id.get()== id+1
                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load Predefined data on frontal face from opencv

                
                # Initializing the face and eye cascade classifiers from xml files
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
                eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                train_dataset = recognizer.read('trainer/trainer.yml') 
               

                id = 2  #two persons
                names = ['','unknownone','unknown','abc','xyz']  #key in names, start from the second place, leave first empty
                font = cv2.FONT_HERSHEY_SIMPLEX
                face_id = input('\n enter user id end press <return> ==>  ')

                # face_id = sys.argv[1]
                # Variable store execution state
                first_read = True

                # Starting the video capture
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                ret, img = cap.read()
                count =0
                while (ret):
                    ret, img = cap.read()
                    # Coverting the recorded image to grayscale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # Applying filter to remove impurities
                    gray = cv2.bilateralFilter(gray, 5, 1, 1)

                    # Detecting the face for region of image to be fed to eye classifier
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))
                  
                    if (len(faces) > 0):
                        for (x, y, w, h) in faces:
                            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                            # roi_face is face which is input to eye classifier
                            roi_face = gray[y:y + h, x:x + w]
                            roi_face_clr = img[y:y + h, x:x + w]
                            eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))

                            conn = mysql.connector.Connect(host="localhost",username="root",password="@Sutanuka123",database="face_recognizer")
                            my_cursor = conn.cursor()

                            # Examining the length of eyes object for eyes
                            if (len(eyes) >= 2):
                                # Check if program is running for detection
                                if (first_read):
                                    cv2.putText(img,
                                            "Eye detected press s",
                                            (70, 70),
                                            cv2.FONT_HERSHEY_PLAIN, 3,
                                            (0, 255, 0), 2)

                                else:
                                    count += 1
                                    cv2.putText(img,
                                            "Eyes open!", (70, 70),
                                            cv2.FONT_HERSHEY_PLAIN, 2,
                                            (255, 255, 255), 2)
                                    # print('click ' + str(count) + ' photo' + ' new face')
                                    if (train_dataset)and train_dataset!= False:
                                        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                                        if (confidence > "30%"):
                                            cv2.putText(img, 'Already in the dataset', (x + 50, y + w + 20), font, 1, (255, 255, 0), 2)
                                        else:
                                            print('click ' + str(count) + ' photo' + confidence +' new face' + id)
                                            print(confidence)
                                            cv2.imwrite("data/User." + str(face_id) + '.' + str(count) + ".jpg",
                                                gray[y:y + h, x:x + w])
                                    else:
                                        cv2.putText(img, 'New face was detected', (x + 50, y + w + 20), font, 1,
                                                (255, 255, 0), 1)
                                        print('click ' + str(count) + ' photo' + ' new face',confidence,id)
                                        cv2.imwrite("data/User." + str(face_id) + '.' + str(count) + ".jpg",
                                                            gray[y:y + h, x:x + w])

                            else:
                                if (first_read):
                                    # To ensure if the eyes are present before starting
                                    cv2.putText(img,
                                            "No eyes detected", (70, 70),
                                            cv2.FONT_HERSHEY_PLAIN, 3,
                                            (0, 0, 255), 2)
                                else:
                                    cv2.waitKey(30)
                                    first_read = True

                    else:
                        cv2.putText(img,
                                "No face detected", (100, 100),
                                cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 255, 0), 2)

                    # Controlling the algorithm with keys
                    cv2.imshow('img', img)
                    a = cv2.waitKey(1)
                    if (a == ord('q')):
                        break
                    elif (a == ord('s') and first_read):
                        # This will start the detection
                        first_read = False
                    elif count >= 100:  # Take 30 face sample and stop video
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set complted !!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

if __name__== "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()