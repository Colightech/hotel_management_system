from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk



class Customer_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Customer Window")
        self.root.geometry("1310x555+235+225")

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
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Customer Details", font=("times new roman", 15, "bold"))
        label_frame_left.place(x = 0, y = 50, width = 425, height = 490)

         #=================LABEL AND ENTRY==============================
        # customer ref
        label_cust_ref = Label(label_frame_left, text = "Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        label_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_ref.grid(row=0, column=1)

        # customer name
        cust_name = Label(label_frame_left, text = "Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)

        entry_name = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_name.grid(row=1, column=1)

        # mother name
        mother_name = Label(label_frame_left, text = "Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        mother_name.grid(row=2, column=0, sticky=W)

        entry_mother_name = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_mother_name.grid(row=2, column=1)

        # gender combobox
        gender = Label(label_frame_left, text = "Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        gender.grid(row=3, column=0, sticky=W)



        # post code
        post_code = Label(label_frame_left, text = "PostCode", font=("arial", 12, "bold"), padx=2, pady=6)
        post_code.grid(row=4, column=0, sticky=W)

        entry_post_code = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_post_code.grid(row=4, column=1)

        # mobile number
        post_code = Label(label_frame_left, text = "Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        post_code.grid(row=5, column=0, sticky=W)

        entry_post_code = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_post_code.grid(row=5, column=1)

        # email
        email = Label(label_frame_left, text = "Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_email.grid(row=6, column=1)

        # nationality
        post_nationality = Label(label_frame_left, text = "Nationality", font=("arial", 12, "bold"), padx=2, pady=6)
        post_nationality.grid(row=7, column=0, sticky=W)

        

        # idproof type combobox
        post_code = Label(label_frame_left, text = "Id Proof Type", font=("arial", 12, "bold"), padx=2, pady=6)
        post_code.grid(row=8, column=0, sticky=W)

        

        # id number
        post_code = Label(label_frame_left, text = "Id Number", font=("arial", 12, "bold"), padx=2, pady=6)
        post_code.grid(row=9, column=0, sticky=W)

        entry_post_code = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_post_code.grid(row=9, column=1)

        # address
        post_code = Label(label_frame_left, text = "Address", font=("arial", 12, "bold"), padx=2, pady=6)
        post_code.grid(row=10, column=0, sticky=W)

        entry_post_code = ttk.Entry( label_frame_left, width=29, font=("arial", 12, "bold"))
        entry_post_code.grid(row=10, column=1)


if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()