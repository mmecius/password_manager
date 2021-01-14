from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=224, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(column=1, row=1)

window.mainloop()