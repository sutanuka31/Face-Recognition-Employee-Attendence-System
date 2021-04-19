from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Attendance Details")

        # Variables
        self.var_atten_id=StringVar()
        self.va_atten_name = StringVar()
        self.var_atten_department = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First image
        img = Image.open(r"E:\Face_recognition_system\Images\face.jpg")
        img = img.resize((700, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=200)

        # Second image
        img_one = Image.open(r"E:\Face_recognition_system\Images\Facial-Recognition-1024x483.jpg")
        img_one = img_one.resize((800, 200), Image.ANTIALIAS)
        self.photoimg_one = ImageTk.PhotoImage(img_one)

        f_lbl = Label(self.root, image=self.photoimg_one)
        f_lbl.place(x=660, y=0, width=800, height=200)

        # bg image
        img_three = Image.open(r"E:\Face_recognition_system\Images\detect.jpg")
        img_three = img_three.resize((1500, 500), Image.ANTIALIAS)
        self.photoimg_three = ImageTk.PhotoImage(img_three)

        bg_img = Label(self.root, image=self.photoimg_three)
        bg_img.place(x=0, y=200, width=1500, height=500)

        #   Label
        title_lbl = Label(bg_img, text="ATTENDANCE REPORT", font=("times new roman", 30, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=190, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=9,y=10,width=1330,height=500)

        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Attendance Report",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=8,width=630,height=460)


        # left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        # left_inside_frame.place(x=0,y=20,width=300,height=500)

        # Labels and entry

        # Employee attendance ID
        attendanceId = Label(Left_frame, text="AttendanceID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(Left_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"),state="readonly")
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Employee attendance Name
        attendancename = Label(Left_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        attendancename.grid(row=0, column=2, padx=4,pady=8)

        attendancename_entry = ttk.Entry(Left_frame,width=20,textvariable=self.va_atten_name,font=("times new roman", 12, "bold"),state="readonly")
        attendancename_entry.grid(row=0,column=3,pady=8)

        # Employee attendance Department
        attendancedep = Label(Left_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        attendancedep.grid(row=1, column=0)

        attendancedep_entry = ttk.Entry(Left_frame,width=20,textvariable=self.var_atten_department,font=("times new roman", 12, "bold"),state="readonly")
        attendancedep_entry.grid(row=1,column=1,pady=8)

        # Employee attendance Time
        attendancetime = Label(Left_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        attendancetime.grid(row=2, column=0)

        attendancetime_entry = ttk.Entry(Left_frame,width=20,textvariable=self.var_atten_time,font=("times new roman", 12, "bold"),state="readonly")
        attendancetime_entry.grid(row=2,column=1,pady=8)

         # Employee attendance Date
        attendancedate = Label(Left_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        attendancedate.grid(row=1, column=2)

        attendancedate_entry = ttk.Entry(Left_frame,width=20,textvariable=self.var_atten_date,font=("times new roman", 12, "bold"),state="readonly")
        attendancedate_entry.grid(row=1,column=3,pady=8)

         

         # Employee attendance 
        attendance = Label(Left_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        attendance.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(Left_frame,width=20,textvariable=self.var_atten_attendance,font="bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Buttons frame
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=600,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman", 12, "bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=16, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=16, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",width=16,command=self.reset_data, font=("times new roman", 12, "bold"), bg="black",
                          fg="white")
        reset_btn.grid(row=0, column=3)

        # Second image
        imgbottom = Image.open(r"E:\Face_recognition_system\Images\photo1.jpg")
        imgbottom = imgbottom.resize((800, 200), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(imgbottom)

        f_lbl = Label(Left_frame, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=220, width=800, height=200)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=660,y=16, width=660, height=452)



        # Scrollbar table
        scroll_x=ttk.Scrollbar(Right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Right_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(Right_frame,column=("emp_id","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)  

        self.AttendanceReportTable.heading("emp_id",text="Attendance ID")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("emp_id",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # Fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

     # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to" +os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.va_atten_name.set(rows[1])
        self.var_atten_department.set(rows[2])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[3])
        self.var_atten_attendance.set(rows[5])

    # Reset 
    def reset_data(self):
        self.var_atten_id.set("")
        self.va_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
       
        

                








        


















if __name__== "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()