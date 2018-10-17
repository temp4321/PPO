from tkinter import*
from view import view
from model import model

root = Tk()

viewer = view(root)

root.configure(background="white")
root.geometry('800x800')
root.mainloop()