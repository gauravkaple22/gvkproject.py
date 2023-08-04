from tkinter import *
from tkinter import messagebox as tmsg
import mysql.connector


class Project:
    def __init__(self,root):
        self.result_listbox = None
        self.lbl_contact = None
        self.lbl_password = None
        self.lbl_blood_group = None
        self.lbl_address = None
        self.lbl_email = None
        self.lbl_name = None
        self.root = root
        self.root.geometry("700x500")
        self.root.config(bg="grey")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"700x500+{x}+{y}")

        self.button1 = Button(root,text="ADD RECORD",bg="orange",font=("arial",13,"bold"),command=self.Add_Record)
        self.button1.place(x=200,y=50,width=300,height=30)
        self.button2 = Button(root,text="SEARCH RECORD",bg="orange",font=("arial",13,"bold"),command=self.Search)
        self.button2.place(x=200,y=120,width=300,height=30)
        self.button3 = Button(root,text="DELETE RECORD",bg="orange",font=("arial",13,"bold"),command=self.Delete)
        self.button3.place(x=200,y=190,width=300,height=30)
        self.button4 = Button(root,text="SHOW ALL RECORD",bg="orange",font=("arial",13,"bold"),command=self.Show)
        self.button4.place(x=200,y=260,width=300,height=30)
        self.button5 = Button(root,text="EXIT",bg="red",font=("arial",13,"bold"),command=exit)
        self.button5.place(x=275,y=330,width=150,height=30)

    def Add_Record(self):
        self.root = root
        self.root.geometry("700x500")
        self.root.config(bg="grey")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"700x500+{x}+{y}")
        self.frame1 = Frame(root, bg="cyan")
        self.frame1.pack(side="left", fill="both", expand=True)

        self.l = Label(self.frame1,text="Register as New User..",font=("arial",14,"bold"),bg="orange")
        self.l.place(x=20,y=10)

        self.l1 = Label(self.frame1,text="Name",font=("arial",12,"bold"),bg="cyan")
        self.l1.place(x=15,y=70)
        self.e = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",12,"bold"))
        self.e.place(x=200,y=70,width=250,height=25)
        self.l2 = Label(self.frame1,text="Email-id",font=("arial",12,"bold"),bg="cyan")
        self.l2.place(x=15,y=130)
        self.e1 = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",12,"bold"))
        self.e1.place(x=200,y=130,width=250,height=25)
        self.l3 = Label(self.frame1,text="Contact Number",font=("arial",12,"bold"),bg="cyan")
        self.l3.place(x=15,y=190)
        self.e2 = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",12,"bold"))
        self.e2.place(x=200,y=190,width=250,height=25)
        self.l4 = Label(self.frame1,text="Address",font=("arial",12,"bold"),bg="cyan")
        self.l4.place(x=15,y=250)
        self.e3 = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",12,"bold"))
        self.e3.place(x=200,y=250,width=250,height=25)
        self.l5 = Label(self.frame1,text="Blood Group",font=("arial",12,"bold"),bg="cyan")
        self.l5.place(x=15,y=310)
        self.e4 = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",12,"bold"))
        self.e4.place(x=200,y=310,width=250,height=25)
        self.l6 = Label(self.frame1,text="Password",font=("arial",12,"bold"),bg="cyan")
        self.l6.place(x=15,y=370)
        self.e5 = Entry(self.frame1,highlightbackground="black",highlightthickness=1,font=("arial",15,"bold"),show="*")
        self.e5.place(x=200,y=370,width=250,height=25)

        self.btn = Button(self.frame1,text="Register",bg="black",fg="white",font=("arial",13,"bold"),command=self.register)
        self.btn.place(x=360,y=430,width=100)
        self.back_btn_return = Button(self.frame1, text="Back", bg="black",command=self.go_back,fg="white",font=("arial",13,"bold"))
        self.back_btn_return.place(x=200, y=430,width=100)

    def go_back(self):
        self.frame1.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame1.destroy()

    def register(self):
        name = self.e.get()
        email = self.e1.get()
        contact_no = self.e2.get()
        address = self.e3.get()
        blood_group = self.e4.get()
        password = self.e5.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#########",
            database=" Data1"
        )

        cursor = connection.cursor()

        insert_query = "INSERT INTO Records (name, email, contact_no, address, blood_group,password) VALUES (%s, %s, %s, %s, %s,%s)"

        cursor.execute(insert_query, (name, email, contact_no, address, blood_group,password))

        connection.commit()

        cursor.close()
        connection.close()

        tmsg.showinfo("Success", "Record saved successfully!")

    def Search(self):
        self.root = root
        self.root.geometry("700x500")
        self.root.config(bg="grey")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"700x500+{x}+{y}")
        self.frame2 = Frame(root, bg="cyan")
        self.frame2.pack(side="left", fill="both", expand=True)
        self.l11 = Label(self.frame2,text="Search Record",font=("arial",14,"bold"),bg="orange")
        self.l11.place(x=310,y=30)

        self.l12 = Label(self.frame2,text="NAME",font=("arial",12,"bold"),bg="cyan")
        self.l12.place(x=130,y=140)
        self.e12 = Entry(self.frame2,highlightbackground="black",highlightthickness=2,font=("arial",14,"bold"))
        self.e12.place(x=250,y=140,width=250,height=25)
        self.btn1 = Button(self.frame2,text="SEARCH",bg="black",fg="white",font=("arial",13,"bold"),command=self.Search_Record)
        self.btn1.place(x=380,y=220,width=100)
        self.back_btn_return = Button(self.frame2, text="Back", bg="black",command=self.go_back1,fg="white",font=("arial",13,"bold"))
        self.back_btn_return.place(x=250, y=220,width=100)

    def Search_Record(self):
        name_to_search = self.e12.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#########",
            database="Data1"
        )

        cursor = connection.cursor()

        search_query = "SELECT * FROM Records WHERE name = %s"

        cursor.execute(search_query, (name_to_search,))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            self.display_results(results)
        else:
            tmsg.showinfo("Not Found", "Name not found in the database.")

    def go_back2(self):
        self.frame3.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame3.destroy()

    def display_results(self, results):
        self.frame2.destroy()

        self.frame3 = Frame(self.root, bg="cyan")
        self.frame3.pack(side="left", fill="both", expand=True)

        self.l21 = Label(self.frame3, text="Here are Details..", font=("arial", 16, "bold"), bg="yellow")
        self.l21.place(x=10, y=10)

        result_listbox = Listbox(self.frame3, width=100, height=15,bg="cyan",font=("arial",10,"bold"),highlightthickness=0,borderwidth=0)
        result_listbox.place(x=10,y=100)
        self.back_btn_return1 = Button(self.frame3, text="Back", bg="orange",command=self.go_back2,fg="black",font=("arial",13,"bold"))
        self.back_btn_return1.place(x=280, y=220,width=100)

        for result in results:
            result_listbox.insert(END, result)

    def go_back1(self):
        self.frame2.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame2.destroy()

    def Delete(self):
        self.root = root
        self.root.geometry("700x500")
        self.root.config(bg="grey")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"700x500+{x}+{y}")
        self.frame4 = Frame(root, bg="cyan")
        self.frame4.pack(side="left", fill="both", expand=True)
        self.l31 = Label(self.frame4,text="Delete Record",font=("arial",14,"bold"),bg="orange")
        self.l31.place(x=310,y=30)

        self.l32 = Label(self.frame4,text="NAME",font=("arial",12,"bold"),bg="cyan")
        self.l32.place(x=130,y=140)
        self.e32 = Entry(self.frame4,highlightbackground="black",highlightthickness=2,font=("arial",14,"bold"))
        self.e32.place(x=250,y=140,width=250,height=25)
        self.btn31 = Button(self.frame4,text="DELETE",bg="black",fg="white",font=("arial",13,"bold"),command=self.Delete_Record)
        self.btn31.place(x=380,y=220,width=100)
        self.back_btn_return = Button(self.frame4, text="Back", bg="blue",command=self.go_back3,fg="white",font=("arial",13,"bold"))
        self.back_btn_return.place(x=250, y=220,width=100)

    def Delete_Record(self):
        name_to_delete = self.e32.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#########",
            database="Data1"
        )

        cursor = connection.cursor()

        select_query = "SELECT * FROM Records WHERE name = %s"
        values = (name_to_delete,)
        cursor.execute(select_query, values)
        record = cursor.fetchone()

        if record:
            delete_query = "DELETE FROM Records WHERE name = %s"
            cursor.execute(delete_query, values)
            connection.commit()

            cursor.close()
            connection.close()

            tmsg.showinfo("Record Deleted", f"Record for {name_to_delete} has been deleted.")
        else:
            tmsg.showinfo("Record Not Found", f"Record for {name_to_delete} was not found in the database.")

    def go_back3(self):
        self.frame4.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame4.destroy()

    def Show(self):
        self.root = root
        self.root.geometry("700x500")
        self.root.config(bg="grey")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"700x500+{x}+{y}")
        self.frame5 = Frame(root, bg="cyan")
        self.frame5.pack(side="left", fill="both", expand=True)
        self.l31 = Label(self.frame5,text="Show All Record",font=("arial",13,"bold"),bg="orange")
        self.l31.place(x=310,y=30)
        self.l32 = Label(self.frame5,text="Clicked Here TO Get All Records",font=("arial",16,"bold"),bg="cyan",fg="black")
        self.l32.place(x=230,y=130)
        self.btn31 = Button(self.frame5,text="Show all Records",bg="yellow",fg="black",font=("arial",13,"bold"),command=self.Show_Details)
        self.btn31.place(x=250,y=220,width=250)
        self.btn32 = Button(self.frame5,text="BACK",bg="orange",fg="black",font=("arial",14,"bold"),command=self.go_back5)
        self.btn32.place(x=250,y=300,width=250)

    def go_back5(self):
        self.frame5.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame5.destroy()

    def Show_Details(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="##########",
            database="Data1"
        )

        cursor = connection.cursor()

        search_query = "SELECT * FROM Records"

        cursor.execute(search_query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            self.display_results1(results)
        else:
            tmsg.showinfo("Not Found", "Name not found in the database.")

    def display_results1(self, results):
        self.frame5.destroy()

        self.frame6 = Frame(self.root, bg="cyan")
        self.frame6.pack(side="left", fill="both", expand=True)

        self.l21 = Label(self.frame6, text="Here are Details..", font=("arial", 16, "bold"), bg="yellow")
        self.l21.place(x=10, y=10)

        result_listbox = Listbox(self.frame6, width=100, height=15,bg="cyan",font=("arial",10,"bold"),highlightthickness=0,borderwidth=0)
        result_listbox.place(x=10,y=100)
        self.back_btn_return2 = Button(self.frame6, text="Back", bg="orange",command=self.go_back4,fg="black",font=("arial",13,"bold"))
        self.back_btn_return2.place(x=300, y=420,width=100)

        for result in results:
            result_listbox.insert(END, result)

    def go_back4(self):
        self.frame6.pack_forget()
        self.button1.place(x=200, y=50)
        self.button2.place(x=200, y=120)
        self.button3.place(x=200, y=190)
        self.button4.place(x=200, y=260)
        self.button5.place(x=275, y=330)
        self.frame6.destroy()


if __name__ == '__main__':
    root = Tk()
    project = Project(root)
    root.mainloop()

