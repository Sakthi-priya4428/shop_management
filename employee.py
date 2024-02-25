from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector 

class employee_class:
    def __init__(self,root) :
       self.root=root
       root.title("SHOP MANAGEMENT SYSTEM")
       root.geometry("1100x500")
       self.root.focus_force()
       self.var_emp_id=StringVar()
       self.var_emp_name=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_doj=StringVar()
       self.var_contact=StringVar()
       self.var_email=StringVar()
       self.var_address=StringVar()
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()
       self.var_utype=StringVar()

       #search frame
       self.search_frame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold")).place(x=250,y=20,width=600,height=70)
    
       #options
       combo_box=ttk.Combobox(self.search_frame,textvariable=self.var_searchby,values=("Select","Name","Email","Contact","Employee ID"),state='readonly',justify=CENTER)
       combo_box.place(x=280,y=50)
       combo_box.current(0)

       txt_search=Entry(self.search_frame,textvariable=self.var_searchtxt,width=20,bg="Light yellow").place(x=450,y=50)
       search_button=Button(self.search_frame,text="Search",bg="#722F37",fg="white",width=20).place(x=590,y=50)

       title=Label(self.root, text="Employee Details",bg="#722F37",fg="white").place(x=50,y=100,width=1000)
       
       lbl_empid=Label(self.root, text="Emp ID",font=('Times New Roman',14)).place(x=50,y=150)
       lbl_emp_name=Label(self.root, text="Name",font=('Times New Roman',14)).place(x=50,y=200)
       lbl_gender=Label(self.root, text="Gender",font=('Times New Roman',14)).place(x=50,y=250)
       lbl_dob=Label(self.root, text="DOB",font=('Times New Roman',14)).place(x=50,y=300)
       lbl_doj=Label(self.root, text="Date of Joining",font=('Times New Roman',14)).place(x=50,y=350)
       lbl_contact=Label(self.root, text="Contact No",font=('Times New Roman',14)).place(x=600,y=150)
       lbl_email=Label(self.root, text="Email ID",font=('Times New Roman',14)).place(x=600,y=200)
       lbl_address=Label(self.root, text="Address",font=('Times New Roman',14)).place(x=600,y=250)
       lbl_utype=Label(self.root, text="User Type",font=('Times New Roman',14)).place(x=600,y=300)
       
       txt_empid=Entry(self.root,textvariable=self.var_emp_id,bg="light yellow").place(x=170,y=150)
       txt_name=Entry(self.root,textvariable=self.var_emp_name,bg="light yellow").place(x=170,y=200)
       gender_combo_box=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER)
       gender_combo_box.place(x=170,y=250)
       gender_combo_box.current(0)

       txt_dob=Entry(self.root,textvariable=self.var_dob,bg="light yellow").place(x=170,y=300)
       txt_doj=Entry(self.root, textvariable=self.var_doj,bg="light yellow").place(x=190,y=350)
       txt_contact=Entry(self.root, textvariable=self.var_contact,bg="light yellow").place(x=720,y=150)
       txt_email=Entry(self.root, textvariable=self.var_email,bg="light yellow").place(x=720,y=200)
       txt_address=Entry(self.root, textvariable=self.var_address,bg="light yellow").place(x=720,y=250)
       utype_combo_box=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","admin","employee"),state='readonly',justify=CENTER)
       utype_combo_box.place(x=720,y=300)
       utype_combo_box.current(0)

       btn_save=Button(self.root,text="SAVE",command=self.save,cursor="hand1",bg="#722F37",fg="white",width=10).place(x=200,y=400)
       btn_update=Button(self.root,text="UPDATE",command=self.update,cursor="hand1",bg="#722F37",fg="white",width=10).place(x=300,y=400)
       btn_delete=Button(self.root,text="DELETE",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=400,y=400)
       btn_clear=Button(self.root,text="CLEAR",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=500,y=400)

       #Tree View
       emp_frame=Frame(self.root,bd=3,relief=RIDGE)
       emp_frame.place(x=0,y=450,relwidth=1,height=200)
       scrolly=Scrollbar(emp_frame,orient=VERTICAL)
       scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
       self.employeetable=ttk.Treeview(emp_frame,columns=("employeeid","name","gender","dob","doj","contact","email","emplocation","usertype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.employeetable.xview)
       scrolly.config(command=self.employeetable.yview)
       self.employeetable.heading("employeeid",text="EMP ID")
       self.employeetable.heading("name",text="EMP NAME")
       self.employeetable.heading("gender",text="GENDER")
       self.employeetable.heading("dob",text="DOB")
       self.employeetable.heading("doj",text="DOJ")
       self.employeetable.heading("contact",text="CONTACT")
       self.employeetable.heading("email",text="EMAIL")
       self.employeetable.heading("emplocation",text="ADDRESS")
       self.employeetable.heading("usertype",text="USER TYPE")
       self.employeetable["show"]="headings"
       self.employeetable.column("employeeid",width=90)
       self.employeetable.column("name",width=100)
       self.employeetable.column("gender",width=100)
       self.employeetable.column("dob",width=100)
       self.employeetable.column("doj",width=100)
       self.employeetable.column("contact",width=100)
       self.employeetable.column("email",width=100)
       self.employeetable.column("emplocation",width=100)
       self.employeetable.column("usertype",width=100)
       self.employeetable.pack(fill=BOTH,expand=1)
       self.employeetable.bind("<ButtonRelease-1>",self.get_data)
       self.show()
#=======================================================================================================
    def save(self):
       connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="employee",auth_plugin='mysql_native_password'
        )
        
       cursor = connection.cursor()
       try:
          if self.var_emp_id.get()=="" :
              messagebox.showerror("Error","Please enter Employee ID!",parent=root)
          else:
              cursor.execute("Select * from employee_details where employeeid=%s",(self.var_emp_id.get(),))
              row=cursor.fetchone()
              if row!=None:
                   messagebox.showerror("Error","This EmployeeID already exists! Try different one",parent=root)
              else:
                  cursor.execute("Insert into employee_details(employeeid,name,gender,dob,doj,contact,email,emplocation,usertype)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_emp_id.get(),
                    self.var_emp_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_utype.get()
                 ))
                  connection.commit()     
                  messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                  self.show()   
       except Exception as e:
             messagebox.showerror("Error",f"Error due to: {str(e)}")

    def get_data(self,ev):
        f=self.employeetable.focus()
        content=(self.employeetable.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_dob.set(row[3]),
        self.var_doj.set(row[4]),
        self.var_contact.set(row[4]),
        self.var_email.set(row[5]),
        self.var_address.set(row[6]),
        self.var_utype.set(row[7])
        

    def update(self):
       connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="employee",auth_plugin='mysql_native_password'
        )
        
       cursor = connection.cursor()
       try:
          if self.var_emp_id.get()=="" :
              messagebox.showerror("Error","Please enter Employee ID!",parent=root)
          else:
              cursor.execute("Select * from employee_details where employeeid=%s",(self.var_emp_id.get(),))
              row=cursor.fetchone()
              if row==None:
                   messagebox.showerror("Error","Invalid Employee ID",parent=root)
              else:
                  cursor.execute("Update employee_details set employeeid=%s,name=%s,gender=%s,dob=%s,doj=%s,contact=%s,email=%s,emplocation=%s,usertype=%s where employeeid=%s",(
                    self.var_emp_id.get(),
                    self.var_emp_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_utype.get()
                 ))
                  connection.commit()     
                  messagebox.showinfo("Success","Employee Details Updated Successfully",parent=self.root)
                  self.show()   
       except Exception as e:
             messagebox.showerror("Error",f"Error due to: {str(e)}")



  
    def show(self):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="employee",auth_plugin='mysql_native_password'
        )
        
        cursor = connection.cursor()
        try:
            cursor.execute("select * from employee_details")
            rows=cursor.fetchall()
            self.employeetable.delete(*self.employeetable.get_children())
            for row in rows:
                self.employeetable.insert('',END,values=row)
                


        except Exception as e:
             messagebox.showerror("Error",f"Error due to: {str(e)}")


             




if __name__=="__main__" : 
    root=Tk()
    class_obj=employee_class(root)
    root.mainloop()
   

      

