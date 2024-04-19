from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Colightech\Desktop\hotel_management_system\images\pool.jpg")
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        login_frame = Frame(self.root, bg="black")
        login_frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\logo4.jpg")
        img1=img1.resize((70,70), Image.Resampling.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        label_img1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        label_img1.place(x=740, y=175, width=70, height=70)

        get_str = Label(login_frame, text = "Get Started", font=("times new roman", 18, "bold"), fg="gold", bg="black")
        get_str.place(x=100, y=80)

        # ==== ENTRY & LABEL ====== The Label and input field to receive input from users
        # User Name Entry
        username = Label(login_frame, text="Username", font=("times new roman", 15), fg="gold", bg="black")
        username.place(x=45, y=136)

        # user icon 
        img2 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\user2.jpg")
        img2=img2.resize((17, 17), Image.Resampling.BILINEAR)
        self.photoimage2=ImageTk.PhotoImage(img2)
        labe2_img2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        labe2_img2.place(x=630, y=310, width=17, height=17)

        self.username_entry = Entry(login_frame, font=("times new roman", 18))
        self.username_entry.place(x=15, y=170, width=280)

        # Password Entry
        password = Label(login_frame, text="Password", font=("times new roman", 15), fg="gold", bg="black")
        password.place(x=45, y=236)

        # user icon 
        img3 = Image.open(r"C:\Users\Colightech\Desktop\hotel_management_system\images\pass.jpg")
        img3=img3.resize((17, 17), Image.Resampling.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)
        labe3_img3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        labe3_img3.place(x=630, y=410, width=17, height=17)

        self.password_entry = Entry(login_frame, font=("times new roman", 18))
        self.password_entry.place(x=15, y=270, width=280)

        # Login Button
        login_btn = Button(login_frame, text="Login", font=("arial", 12, "bold"), bg="black", fg="white", width=10, cursor="hand2")
        login_btn.place(x=33, y=330, width=100)

        # Sign Up Button
        signup_btn = Button(login_frame, text="Sign Up", font=("arial", 12, "bold"), bg="black", fg="white", width=10, cursor="hand2")
        signup_btn.place(x=180, y=330, width=100)

        # Forget Password Button
        signup_btn = Button(login_frame, text="Forget Password", font=("arial", 12, "bold"), bg="black", fg="white", width=10, cursor="hand2")
        signup_btn.place(x=90, y=390, width=150)

        


if __name__ == "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()