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
        entry_contact = ttk.Entry( label_frame_left, width=25, font=("arial", 11, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        fetch_data_btn = Button(label_frame_left, text="Fetch Data", font=("arial", 8, "bold"), bg="green", fg="gold", width=10, cursor="hand2")
        fetch_data_btn.place(x=335, y=2)

        # Check In Date
        check_in_date = Label(label_frame_left, text = "Check in date:", font=("arial", 10, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        entry_check_in_date = ttk.Entry( label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_check_in_date.grid(row=1, column=1)

        # Check Out Date
        check_out_date = Label(label_frame_left, text = "Check out date:", font=("arial", 10, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        entry_check_out_date = ttk.Entry( label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_check_out_date.grid(row=2, column=1)

        # Room Type Combobox
        label_roomType = Label(label_frame_left, text = "Room Type:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_roomType.grid(row=3, column=0, sticky=W)

        combo_roomType = ttk.Combobox(label_frame_left, font=("arial", 11, "bold"), width=33, state="readonly")
        combo_roomType["value"] = ("Single", "Double", "Luxury")
        combo_roomType.current(0)
        combo_roomType.grid(row=3, column=1)

        # Available Room
        label_available_room = Label(label_frame_left, text = "Available Room:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_available_room.grid(row=4, column=0, sticky=W)
        entry_available_room = ttk.Entry( label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_available_room.grid(row=4, column=1)

        # Meal
        label_meal = Label(label_frame_left, text = "Meal:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_meal.grid(row=5, column=0, sticky=W)
        entry_meal = ttk.Entry(label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_meal.grid(row=5, column=1)

        # No of Days
        label_no_of_day = Label(label_frame_left, text = "No Of Days:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_no_of_day.grid(row=6, column=0, sticky=W)
        entry_no_of_day = ttk.Entry(label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_no_of_day.grid(row=6, column=1)

        # Paid Tax
        label_paid_tax = Label(label_frame_left, text = "Paid Tax:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_paid_tax.grid(row=7, column=0, sticky=W)
        entry_paid_tax = ttk.Entry(label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_paid_tax.grid(row=7, column=1)

        # Sub Total
        label_sub_total = Label(label_frame_left, text = "Sub Total:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_sub_total.grid(row=8, column=0, sticky=W)
        entry_sub_total = ttk.Entry(label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_sub_total.grid(row=8, column=1)

        # Total Cost
        label_total_cost = Label(label_frame_left, text = "Total Cost:", font=("arial", 10, "bold"), padx=2, pady=6)
        label_total_cost.grid(row=9, column=0, sticky=W)
        entry_total_cost = ttk.Entry(label_frame_left, width=35, font=("arial", 11, "bold"))
        entry_total_cost.grid(row=9, column=1)







if __name__ == "__main__":
    root = Tk()
    obj = Room_window(root)
    root.mainloop()