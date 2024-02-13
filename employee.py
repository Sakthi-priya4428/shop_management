
from tkinter import *
from tkinter import ttk

class employee_class:
    def __init__(self,root) :
       self.root=root
       root.title("SHOP MANAGEMENT SYSTEM")
       root.geometry("1100x500")
       self.root.focus_force()

       #search frame
       self.search_frame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold")).place(x=250,y=20,width=600,height=70)
    
       #options
       combo_box=ttk.Combobox(self.search_frame,values=("Select","Email","Contact","Name","Employee ID"),state='readonly',justify=CENTER)
       combo_box.place(x=270,y=50)
       combo_box.current(0)

       txt_search=Entry(self.search_frame).place(x=450,y=50)

if __name__=="__main__" :  
   root=Tk()
   class_obj=employee_class(root)
   root.mainloop()
