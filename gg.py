from tkinter import*
from tkinter import messagebox
def b_click(b):
    pass
root = Tk()
root.title("game view")


b1 = Button(root, text = " " ,font=("Helvetica",20), height= 3, width=6, bg="Gray", command=lambda:b_click(b1))
b2 = Button(root, text = " " ,font=("Helvetica",20), height= 3, width=6, bg="Gray", command=lambda:b_click(b2))
b3 = Button(root, text = " " ,font=("Helvetica",20), height= 3, width=6, bg="Gray", command=lambda:b_click(b3))

b1.grid(row = 0 , column =0)
b2.grid(row = 0 , column =1)
b3.grid(row = 0 , column =2)
