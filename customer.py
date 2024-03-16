from tkinter import *



class Customer_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Customer Window")
        self.root.geometry("1310x555+235+225")




if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()