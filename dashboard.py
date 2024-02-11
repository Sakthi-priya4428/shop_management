from tkinter import *
from employee import employee_class


class SMS:
    def __init__(self,root) :
       self.root=root
       self.root.title("SHOP MANAGEMENT SYSTEM")
       self.root.geometry("1350x700")
       title=Label(root,text="Shop Management System",font=('Sans-serif',25,'bold'),bg="#722F37",fg="#FFFFFF").place(x=0,y=0,relwidth=1,height=90)
       # Create a frame for the sidebar
       self.sidebar_frame = Frame(self.root, bg="#722F37", width=190,height=40)
       self.sidebar_frame.pack(side=LEFT, fill=Y)

      # Create buttons in the sidebar
       
       home_button=Button(self.sidebar_frame,text="HOME",bg="#722F37",fg="#FFFFFF",width=25,height=2).place(x=0,y=130)
     
       products_button=Button(self.sidebar_frame,text="PRODUCTS",bg="#722F37",fg="#FFFFFF",width=25,height=2).place(x=0,y=200)
       employee_button=Button(self.sidebar_frame,text="EMPLOYEES",command=self.employee,bg="#722F37",fg="#FFFFFF",width=25,height=2).place(x=0,y=270)
       salesreport_button=Button(self.sidebar_frame,text="SALES REPORT",bg="#722F37",fg="#FFFFFF",width=25,height=2).place(x=0,y=340)
       

       #Sign in and Log out button
       signin_button=Button(self.root,text="Sign In",fg="#FFFFFF",bg="#b2b200",width=20,height=2).place(x=900,y=25)
       signup_button=Button(self.root,text="Sign Up",fg="#FFFFFF",bg="#b2b200",width=20,height=2).place(x=1090,y=25)

       welcome_label=Label(self.sidebar_frame,text="WELCOME!!!",bg="#722F37",fg="white",font=("Arial",20,'bold')).place(x=15,y=25)
       
          



    def employee(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=employee_class(self.new_win)
   
    
       

       
       
      
        
if __name__=="__main__" :  
   root=Tk()
   class_obj=SMS(root)
   root.mainloop()

