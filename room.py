from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector    #pip install mysql-connector-python


class Room_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1310x555+235+225")


         # =====================VARIABLES======================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_availableroom=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_totalcost=StringVar()
        
         # =================TITLE==============================
        label_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 15, "bold"), bg="green", fg="gold", bd=2, relief=RIDGE)
        label_title.place(x=0, y=0, width=1310, height=50)

        #=================LOGO==============================
        img2 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\logo2.jpg")
        img2 = img2.resize((60,50),Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_label2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        img_label2.place(x=0, y=0, width=60, height=50)

        #=================LABEL FRAME==============================
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "room booking", font=("times new roman", 14, "bold"))
        label_frame_left.place(x = 0, y = 50, width = 425, height = 490)

        #=================LABEL AND ENTRY==============================
        # Customer Contact
        label_cust_contact = Label(label_frame_left, text = "Customer Contact:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry( label_frame_left,  textvariable=self.var_contact, width=25, font=("arial", 11, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        fetch_data_btn = Button(label_frame_left, command=self.fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        fetch_data_btn.place(x=335, y=2)

        # Check In Date
        check_in_date = Label(label_frame_left, text = "Check in date:", font=("arial", 10, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        entry_check_in_date = ttk.Entry( label_frame_left, textvariable=self.var_checkin, width=35, font=("arial", 11, "bold"))
        entry_check_in_date.grid(row=1, column=1)

        # Check Out Date
        check_out_date = Label(label_frame_left, text = "Check out date:", font=("arial", 10, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        entry_check_out_date = ttk.Entry( label_frame_left, textvariable=self.var_checkout, width=35, font=("arial", 11, "bold"))
        entry_check_out_date.grid(row=2, column=1)

        # Room Type Combobox
        label_roomType = Label(label_frame_left, text = "Room Type:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_roomType.grid(row=3, column=0, sticky=W)

        combo_roomType = ttk.Combobox(label_frame_left, textvariable=self.var_roomtype, font=("arial", 11, "bold"), width=33, state="readonly")
        combo_roomType["value"] = ("Single", "Double", "Luxury")
        combo_roomType.current(0)
        combo_roomType.grid(row=3, column=1)

        # Available Room
        label_available_room = Label(label_frame_left, text = "Available Room:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_available_room.grid(row=4, column=0, sticky=W)
        entry_available_room = ttk.Entry( label_frame_left, textvariable=self.var_availableroom, width=35, font=("arial", 11, "bold"))
        entry_available_room.grid(row=4, column=1)

        # Meal
        label_meal = Label(label_frame_left, text = "Meal:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_meal.grid(row=5, column=0, sticky=W)
        entry_meal = ttk.Entry(label_frame_left, textvariable=self.var_meal, width=35, font=("arial", 11, "bold"))
        entry_meal.grid(row=5, column=1)

        # No of Days
        label_no_of_day = Label(label_frame_left, text = "No of Days:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_no_of_day.grid(row=6, column=0, sticky=W)
        entry_no_of_day = ttk.Entry(label_frame_left, textvariable=self.var_noofdays, width=35, font=("arial", 11, "bold"))
        entry_no_of_day.grid(row=6, column=1)

        # Paid Tax
        label_paid_tax = Label(label_frame_left, text = "Paid Tax:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_paid_tax.grid(row=7, column=0, sticky=W)
        entry_paid_tax = ttk.Entry(label_frame_left, textvariable=self.var_paidtax, width=35, font=("arial", 11, "bold"))
        entry_paid_tax.grid(row=7, column=1)

        # Sub Total
        label_sub_total = Label(label_frame_left, text = "Sub Total:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_sub_total.grid(row=8, column=0, sticky=W)
        entry_sub_total = ttk.Entry(label_frame_left, textvariable=self.var_subtotal, width=35, font=("arial", 11, "bold"))
        entry_sub_total.grid(row=8, column=1)

        # Total Cost
        label_total_cost = Label(label_frame_left, text = "Total Cost:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_total_cost.grid(row=9, column=0, sticky=W)
        entry_total_cost = ttk.Entry(label_frame_left, textvariable=self.var_totalcost, width=35, font=("arial", 11, "bold"))
        entry_total_cost.grid(row=9, column=1)

         # =================BILL BUTTON=========================
        add_btn = Button(label_frame_left, text="Bill",  font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        add_btn.grid(row=10, column=0, padx=2, pady=4, sticky=W)

        # =================BUTTONS==============================
        btn_frame = Frame(label_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=3, y=400, width=412, height=40)

        add_btn = Button(btn_frame, text="Add",  font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        add_btn.grid(row=0, column=0, padx=2, pady=4)

        update_btn = Button(btn_frame, text="Update", font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        update_btn.grid(row=0, column=1, padx=8, pady=4)

        delete_btn = Button(btn_frame, text="Delete", font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        delete_btn.grid(row=0, column=2, padx=8, pady=4)

        reset_btn = Button(btn_frame, text="Reset", font=("arial", 10, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=8, pady=4)

        # =====================RIGHT SIDE IMAGE==========================
        img3 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\image6.jpg")
        img3 = img3.resize((594,240),Image.Resampling.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        img_label3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        img_label3.place(x=700, y=52, width=594, height=240)

        # =================TABLE FRAME AND SEARCH SYSTEM==================
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font=("arial", 10, "bold"))
        table_frame.place(x = 435, y = 280, width = 860, height = 260)

        # search table
        search_label = Label(table_frame, text = "Search:", font=("arial", 10, "bold"), bg="black", fg="white")
        search_label.grid(row=0, column=0, sticky=W, padx=3, pady=5)

        self.search_var=StringVar()
        combo_id_proof_label = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 10, "bold"), width=24, state="readonly")
        combo_id_proof_label["value"] = ("Contact", "Room", "Name")
        combo_id_proof_label.current(0)
        combo_id_proof_label.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_search = ttk.Entry( table_frame, textvariable=self.txt_search, width=24, font=("arial", 10, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        search_btn = Button(table_frame, text="Search", font=("arial", 8, "bold"), bg="green", fg="gold", width=15, cursor="hand2")
        search_btn.grid(row=0, column=3, padx=4)

        show_all_btn = Button(table_frame, text="Show All", font=("arial", 8, "bold"), bg="green", fg="gold", width=15, cursor="hand2")
        show_all_btn.grid(row=0, column=4, padx=4)

        # =================SHOW DATA TABLE==============================
        detail_table = Frame(table_frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=35, width=858, height=180)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.room_table =ttk.Treeview(detail_table, column=("contact", "checkin", "checkout", "roomtype", "availableroom", "meal", 
                                                "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
         #=========TABLE COLUMNS HEADING================
        self.room_table.heading("contact", text="Customer Contact")
        self.room_table.heading("checkin", text="Check in Date")
        self.room_table.heading("checkout", text="Check out Date")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("availableroom", text="Available Room")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No of Days")

        self.room_table["show"] = "headings"
         #=========TO CONTROL THE WIDTH OF THE TABLE COLUMNS===========
        self.room_table.column("contact", width=140)
        self.room_table.column("checkin", width=140)
        self.room_table.column("checkout", width=140)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("availableroom", width=120)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:

            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="admin123", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("SELECT Name FROM customer WHERE Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This Number is not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE)
                showDataframe.place(x=430, y=60, width=260, height=210)

                label_name = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                label_name.place(x=0, y=0)





if __name__ == "__main__":
    root = Tk()
    obj = Room_window(root)
    root.mainloop()