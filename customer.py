from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector    #pip install mysql-connector-python



class Customer_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Customer Window")
        self.root.geometry("1310x555+235+225")

         # =================VARIABLE===========================
        self.var_ref = StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        

         # =================TITLE==============================
        label_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 15, "bold"), bg="green", fg="gold", bd=2, relief=RIDGE)
        label_title.place(x=0, y=0, width=1310, height=50)

        #=================LOGO==============================
        img2 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\logo2.jpg")
        img2 = img2.resize((60,50),Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        

        img_label2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        img_label2.place(x=0, y=0, width=60, height=50)

        #=================LABEL FRAME==============================
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Customer Details", font=("times new roman", 14, "bold"))
        label_frame_left.place(x = 0, y = 50, width = 425, height = 490)


        #=================LABEL AND ENTRY==============================
        # customer ref
        label_cust_ref = Label(label_frame_left, text = "Customer Ref:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry( label_frame_left, textvariable=self.var_ref, width=37, font=("arial", 11, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # customer name
        cust_name = Label(label_frame_left, text = "Customer Name:", font=("arial", 10, "bold"), padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)

        entry_name = ttk.Entry( label_frame_left, textvariable=self.var_cust_name, width=37, font=("arial", 11, "bold"))
        entry_name.grid(row=1, column=1)

        # mother name
        mother_name = Label(label_frame_left, text = "Mother Name:", font=("arial", 10, "bold"), padx=2, pady=6)
        mother_name.grid(row=2, column=0, sticky=W)

        entry_mother_name = ttk.Entry( label_frame_left, textvariable=self.var_mother, width=37, font=("arial", 11, "bold"))
        entry_mother_name.grid(row=2, column=1)

        # gender combobox
        gender = Label(label_frame_left, text = "Gender:", font=("arial", 10, "bold"), padx=2, pady=6)
        gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(label_frame_left, textvariable=self.var_gender, font=("arial", 11, "bold"), width=35, state="readonly")
        combo_gender["value"] = ("Male", "Female")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # post code
        post_code = Label(label_frame_left, text = "PostCode:", font=("arial", 10, "bold"), padx=2, pady=6)
        post_code.grid(row=4, column=0, sticky=W)

        entry_post_code = ttk.Entry( label_frame_left, textvariable=self.var_post, width=37, font=("arial", 11, "bold"))
        entry_post_code.grid(row=4, column=1)

        # mobile number
        label_mobile = Label(label_frame_left, text = "Mobile:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_mobile.grid(row=5, column=0, sticky=W)

        entry_label_mobile = ttk.Entry( label_frame_left, textvariable=self.var_mobile, width=37, font=("arial", 11, "bold"))
        entry_label_mobile.grid(row=5, column=1)

        # email
        email_label = Label(label_frame_left, text = "Email:", font=("arial", 10, "bold"), padx=2, pady=6)
        email_label.grid(row=6, column=0, sticky=W)

        entry_email_label = ttk.Entry( label_frame_left, textvariable=self.var_email, width=37, font=("arial", 11, "bold"))
        entry_email_label.grid(row=6, column=1)

        # nationality combobox
        post_nationality = Label(label_frame_left, text = "Nationality:", font=("arial", 10, "bold"), padx=2, pady=6)
        post_nationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(label_frame_left, textvariable=self.var_nationality, font=("arial", 11, "bold"), width=35, state="readonly")
        combo_nationality["value"] = ("Nigeria", "Canada", "USA", "UK", "France", "Australia", "Germany", "Italy")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # id proof type combobox
        id_proof_label = Label(label_frame_left, text = "Id Proof Type:", font=("arial", 10, "bold"), padx=2, pady=6)
        id_proof_label.grid(row=8, column=0, sticky=W)

        combo_id_proof_label = ttk.Combobox(label_frame_left, textvariable=self.var_id_proof, font=("arial", 11, "bold"), width=35, state="readonly")
        combo_id_proof_label["value"] = ("International Passport", "Drivers License", "National Id")
        combo_id_proof_label.current(0)
        combo_id_proof_label.grid(row=8, column=1)

        # id number
        id_number = Label(label_frame_left, text = "Id Number:", font=("arial", 10, "bold"), padx=2, pady=6)
        id_number.grid(row=9, column=0, sticky=W)

        entry_id_number = ttk.Entry( label_frame_left, textvariable=self.var_id_number, width=37, font=("arial", 11, "bold"))
        entry_id_number.grid(row=9, column=1)

        # address
        address_label = Label(label_frame_left, text = "Address:", font=("arial", 10, "bold"), padx=2, pady=6)
        address_label.grid(row=10, column=0, sticky=W)

        entry_address_label = ttk.Entry( label_frame_left, textvariable=self.var_address, width=37, font=("arial", 11, "bold"))
        entry_address_label.grid(row=10, column=1)

        #=================BUTTONS==============================
        btn_frame = Frame(label_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=3, y=400, width=412, height=40)

        add_btn = Button(btn_frame, text="Add",  command=self.add_data, font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        add_btn.grid(row=0, column=0, padx=2, pady=4)

        update_btn = Button(btn_frame, text="Update", command=self.update, font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        update_btn.grid(row=0, column=1, padx=8, pady=4)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_customer, font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        delete_btn.grid(row=0, column=2, padx=8, pady=4)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=8, pady=4)

         #=================TABLE FRAME AND SEARCH SYSTEM==============================
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font=("arial", 10, "bold"))
        table_frame.place(x = 435, y = 50, width = 860, height = 490)

        # search table
        search_label = Label(table_frame, text = "Search:", font=("arial", 10, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, sticky=W, padx=3, pady=5)

        self.search_var=StringVar()
        combo_id_proof_label = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 10, "bold"), width=24, state="readonly")
        combo_id_proof_label["value"] = ("Mobile", "Ref", "Name")
        combo_id_proof_label.current(0)
        combo_id_proof_label.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_search = ttk.Entry( table_frame, textvariable=self.txt_search, width=24, font=("arial", 10, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        search_btn = Button(table_frame, text="Search", command=self.search, font=("arial", 8, "bold"), bg="green", fg="gold", width=15, cursor="hand2")
        search_btn.grid(row=0, column=3, padx=4)

        show_all_btn = Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 8, "bold"), bg="green", fg="gold", width=15, cursor="hand2")
        show_all_btn.grid(row=0, column=4, padx=4)

        #=================SHOW DATA TABLE==============================
        detail_table = Frame(table_frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=35, width=858, height=435)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.Cust_Details_Table =ttk.Treeview(detail_table, column=("ref", "name", "mother", "gender", "post", "mobile", 
                                                "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
         #=========TABLE COLUMNS HEADING================
        self.Cust_Details_Table.heading("ref", text="Customer Ref")
        self.Cust_Details_Table.heading("name", text="Customer Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"
         #=========TO CONTROL THE WIDTH OF THE TABLE COLUMNS===========
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=140)
        self.Cust_Details_Table.column("mother", width=140)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=120)
        self.Cust_Details_Table.column("email", width=200)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=140)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=300)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #=================FUNCTION THAT INSERT DATA TABLE==============================
    def add_data(self):
        if self.var_mobile.get() =="" or self.var_mother.get()=="":
            messagebox.showerror("Error:", "All field are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_mother.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added", parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", "something went wrong: {}".format(e), parent=self.root)
                
    # =================FUNCTION THAT FETCH DATA FROM THE TABLE AND DISPLAYED IT ON THE APP==============================
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =================FUNCTION THAT REFILL THE FIELDS WITH THE CURSOR FOCUS ROW==============================
    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    # =================UPDATE FUNCTION==============================
    def update(self):
        if self.var_mobile.get() =="":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE Ref=%s", (
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent=self.root)

    # =================DELETE FUNCTION==============================
    def delete_customer(self):
        var_delete = messagebox.askyesno("Hotel Management System", "Are you sure you want to delete this customer", parent=self.root)
        if var_delete > 0:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not var_delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Deleted", "Customer details has been deleted successfully", parent=self.root)

    # =================RESET FUNCTION==============================
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # =================SEARCH FUNCTION==============================
    def search(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%' ")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()