from tkinter import *
from tkinter import messagebox


def save():

    website = website_entry_field.get()
    username = username_password_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                delete_data()


def delete_data():
    website_entry_field.delete(0, END)
    password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
username_email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_entry_field = Entry(width=35)
username_password_entry = Entry(width=21)
password_entry = Entry(width=35)

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=35, command=save)

website_label.grid(column=0, row=3)
username_email_label.grid(column=0, row=4)
password_label.grid(column=0, row=5)

website_entry_field.grid(column=1, row=3, columnspan=2)
website_entry_field.focus()
username_password_entry.grid(column=1, row=4)
username_password_entry.insert(0,"tmecius@gmail.com")
password_entry.grid(column=1, row=5, columnspan=2)

generate_button.grid(column=2, row=4)
add_button.grid(column=1, row=6, columnspan=2)

window.mainloop()