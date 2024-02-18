
from tkinter import *
from tkinter import ttk

class employee_class:
    def __init__(self,root) :
       self.root=root
       root.title("SHOP MANAGEMENT SYSTEM")
       root.geometry("1100x500")
       self.root.focus_force()
       self.var_emp_id=StringVar()
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
       combo_box=ttk.Combobox(self.search_frame,textvariable=self.var_searchby,values=("Select","Email","Contact","Name","Employee ID"),state='readonly',justify=CENTER)
       combo_box.place(x=280,y=50)
       combo_box.current(0)

       txt_search=Entry(self.search_frame,textvariable=self.var_searchtxt,width=20,bg="Light yellow").place(x=450,y=50)
       search_button=Button(self.search_frame,text="Search",bg="#722F37",fg="white",width=20).place(x=590,y=50)

       title=Label(self.root, text="Employee Details",bg="#722F37",fg="white").place(x=50,y=100,width=1000)
       
       lbl_empid=Label(self.root, text="Emp ID",font=('Times New Roman',14)).place(x=50,y=150)
       lbl_gender=Label(self.root, text="Gender",font=('Times New Roman',14)).place(x=50,y=200)
       lbl_dob=Label(self.root, text="DOB",font=('Times New Roman',14)).place(x=50,y=250)
       lbl_doj=Label(self.root, text="Date of Joining",font=('Times New Roman',14)).place(x=50,y=300)
       lbl_contact=Label(self.root, text="Contact No",font=('Times New Roman',14)).place(x=600,y=150)
       lbl_email=Label(self.root, text="Email ID",font=('Times New Roman',14)).place(x=600,y=200)
       lbl_address=Label(self.root, text="Address",font=('Times New Roman',14)).place(x=600,y=250)
       lbl_utype=Label(self.root, text="User Type",font=('Times New Roman',14)).place(x=600,y=300)
       
       txt_empid=Entry(self.root,textvariable=self.var_emp_id,bg="light yellow").place(x=170,y=150)
       gender_combo_box=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER)
       gender_combo_box.place(x=170,y=200)
       gender_combo_box.current(0)

       txt_dob=Entry(self.root,textvariable=self.var_dob,bg="light yellow").place(x=170,y=250)
       txt_doj=Entry(self.root, textvariable=self.var_doj,bg="light yellow").place(x=190,y=300)
       txt_contact=Entry(self.root, textvariable=self.var_contact,bg="light yellow").place(x=720,y=150)
       txt_email=Entry(self.root, textvariable=self.var_email,bg="light yellow").place(x=720,y=200)
       txt_address=Entry(self.root, textvariable=self.var_address,bg="light yellow").place(x=720,y=250)
       utype_combo_box=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","admin","employee"),state='readonly',justify=CENTER)
       utype_combo_box.place(x=720,y=300)
       utype_combo_box.current(0)

       btn_save=Button(self.root,text="SAVE",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=200,y=370)
       btn_update=Button(self.root,text="UPDATE",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=300,y=370)
       btn_delete=Button(self.root,text="DELETE",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=400,y=370)
       btn_clear=Button(self.root,text="CLEAR",cursor="hand1",bg="#722F37",fg="white",width=10).place(x=500,y=370)

       

       save_button=Button(self.root,)
       
if __name__=="__main__" :  
   root=Tk()
   class_obj=employee_class(root)
   root.mainloop()
