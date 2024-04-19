from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Signup_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Colightech\Desktop\hotel_management_system\images\pool.jpg")
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)


        img1 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\image2.jpg")
        img1=img1.resize((411,400), Image.Resampling.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        label_img1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        label_img1.place(x=205, y=200, width=411, height=400)

        # Registration Frame
        signup_frame = Frame(self.root, bg="black")
        signup_frame.place(x=615, y=200, width=750, height=400)

        get_str = Label(signup_frame, text = "Registration", font=("times new roman", 18, "bold"), fg="gold", bg="black")
        get_str.place(x=170, y=10)

        # ==== REGISTRATION ENTRY & LABEL ====== The Label and input field to receive input from users
        # =================USERNAME & EMAIL ROW========================
        # User Name Entry
        username = Label(signup_frame, text="Username:", font=("times new roman", 15), fg="gold", bg="black")
        username.place(x=20, y=60)
        self.username_entry = Entry(signup_frame, font=("times new roman", 18))
        self.username_entry.place(x=120, y=60, width=250)

        # Email Address
        email = Label(signup_frame, text="Email Add:", font=("times new roman", 15), fg="gold", bg="black")
        email.place(x=380, y=60)
        self.email_entry = Entry(signup_frame, font=("times new roman", 18))
        self.email_entry.place(x=482, y=60, width=250)
        #===================================================


        # =================FIRST_NAME & LAST_NAME ROW========================
        # First Name Entry
        first_name = Label(signup_frame, text="First Name:", font=("times new roman", 15), fg="gold", bg="black")
        first_name.place(x=20, y=120)
        self.first_name_entry = Entry(signup_frame, font=("times new roman", 18))
        self.first_name_entry.place(x=120, y=120, width=250)

        # Last Name
        last_name = Label(signup_frame, text="Last Name:", font=("times new roman", 15), fg="gold", bg="black")
        last_name.place(x=380, y=120)
        self.last_name_entry = Entry(signup_frame, font=("times new roman", 18))
        self.last_name_entry.place(x=482, y=120, width=250)
        # =========================================

        # =================GENDER & HOME ADD ROW========================
        # Gender Entry
        gender = Label(signup_frame, text="Gender:", font=("times new roman", 15), fg="gold", bg="black")
        gender.place(x=20, y=180)
        self.gender_entry = Entry(signup_frame, font=("times new roman", 18))
        self.gender_entry.place(x=120, y=180, width=250)

        # Home Address Entry
        home_address = Label(signup_frame, text="Home Add:", font=("times new roman", 15), fg="gold", bg="black")
        home_address.place(x=380, y=180)
        self.home_address_entry = Entry(signup_frame, font=("times new roman", 18))
        self.home_address_entry.place(x=482, y=180, width=250)
        # =========================================

        # =================MOBILE & NATIONALITY ROW========================
        # Mobile Entry
        mobile = Label(signup_frame, text="Mobile:", font=("times new roman", 15), fg="gold", bg="black")
        mobile.place(x=20, y=240)
        self.mobile_entry = Entry(signup_frame, font=("times new roman", 18))
        self.mobile_entry.place(x=120, y=240, width=250)

        # Nationality Entry
        nationality = Label(signup_frame, text="Nationality:", font=("times new roman", 15), fg="gold", bg="black")
        nationality.place(x=380, y=240)
        self.nationality_entry = Entry(signup_frame, font=("times new roman", 18))
        self.nationality_entry.place(x=482, y=240, width=250)
        # =========================================

        # =================Post Code & International Passport ROW========================
        # Post Code Entry
        post_code = Label(signup_frame, text="Post Code:", font=("times new roman", 15), fg="gold", bg="black")
        post_code.place(x=20, y=300)
        self.post_code_entry = Entry(signup_frame, font=("times new roman", 18))
        self.post_code_entry.place(x=120, y=300, width=250)

        # International Passport Entry
        inT_passport = Label(signup_frame, text="Int Passport:", font=("times new roman", 15), fg="gold", bg="black")
        inT_passport.place(x=380, y=300)
        self.inT_passport_entry = Entry(signup_frame, font=("times new roman", 18))
        self.inT_passport_entry.place(x=482, y=300, width=250)
        # =========================================

        # Login Button
        submit_btn = Button(signup_frame, text="Submit", font=("arial", 12, "bold"), bg="black", fg="white", width=10, cursor="hand2")
        submit_btn.place(x=120, y=350, width=100)

        # # Sign Up Button
        # signup_btn = Button(signup_frame, text="Forget Password", font=("arial", 12, "bold"), bg="black", fg="white", width=10, cursor="hand2")
        # signup_btn.place(x=477, y=350, width=150)


        

        



if __name__ == "__main__":
    root = Tk()
    app = Signup_window(root)
    root.mainloop()