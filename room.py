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




if __name__ == "__main__":
    root = Tk()
    obj = Room_window(root)
    root.mainloop()