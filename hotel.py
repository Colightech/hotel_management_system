from tkinter import *
from PIL import Image, ImageTk   #pip3 install pillow
from customer import Customer_window


class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #=================FIRST IMAGE=====================
        img1 = Image.open("images\image7.jpg")
        img1 = img1.resize((1550,140),Image.Resampling.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        

        img_label1 = Label(self.root, image=self.photoimg1, bd=2, relief=RIDGE)
        img_label1.place(x=0, y=0, width=1550, height=140)

        
        #=================LOGO==============================
        img2 = Image.open("images\logo2.jpg")
        img2 = img2.resize((200,140),Image.Resampling.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        

        img_label2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        img_label2.place(x=0, y=0, width=200, height=140)

        # =================TITLE==============================
        label_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="green", fg="gold", bd=2, relief=RIDGE)
        label_title.place(x=0, y=140, width=1550, height=50)

        # =================MAIN FRAME========================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # =================MAIN FRAME========================
        label_menu = Label( main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="green", fg="gold", bd=2, relief=RIDGE)
        label_menu.place(x=0, y=0, width=230)

        # =================BUTTON FRAME========================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=229, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command = self.customer_details, width=20, font=("times new roman", 14, "bold"), bg="green", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=20, font=("times new roman", 14, "bold"), bg="green", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        detail_btn = Button(btn_frame, text="DETAILS", width=20, font=("times new roman", 14, "bold"), bg="green", fg="gold", bd=0, cursor="hand2")
        detail_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=20, font=("times new roman", 14, "bold"), bg="green", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=20, font=("times new roman", 14, "bold"), bg="green", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # =================RIGHT SIDE IMAGE========================
        img3 = Image.open("images\image5.jpg")
        img3 = img3.resize((1310,590),Image.Resampling.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        

        img_label3 = Label(main_frame, image=self.photoimg3, bd=2, relief=RIDGE)
        img_label3.place(x=230, y=0, width=1310, height=590)

        # =================LEFT DOWN IMAGES========================
        img4 = Image.open("images\image2.jpg")
        img4 = img4.resize((230,190),Image.Resampling.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        

        img_label4 = Label(main_frame, image=self.photoimg4, bd=2, relief=RIDGE)
        img_label4.place(x=0, y=240, width=230, height=190)
        
        img5 = Image.open("images\image1.jpg")
        img5 = img5.resize((230,190),Image.Resampling.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        

        img_label5 = Label(main_frame, image=self.photoimg5, bd=2, relief=RIDGE)
        img_label5.place(x=0, y=430, width=230, height=190)

        # =====================CUSTOMER WINDOW FUNCTION=======================
    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_window(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()