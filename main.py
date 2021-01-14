from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_entry_field = Entry(width=35)

username_email_label = Label(text="Email/Username:")
username_password_entry = Entry(width=21)

password_label = Label(text="Password:")
password_entry = Entry(width=35)

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=35)

website_label.grid(column=0, row=3)
website_entry_field.grid(column=1, row=3, columnspan=2)

username_email_label.grid(column=0, row=4)
username_password_entry.grid(column=1, row=4)

password_label.grid(column=0, row=5)
password_entry.grid(column=1, row=5, columnspan=2)

generate_button.grid(column=2, row=4)
add_button.grid(column=1, row=6, columnspan=2)

window.mainloop()