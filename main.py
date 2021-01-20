from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


def save():

    website = website_entry_field.get()
    username = username_password_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": username,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry_field.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry_field.get()
    try:
        with open("data.json") as data:
            data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for website exists!!")



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)
# Labels
website_label = Label(text="Website:")
username_email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entries
website_entry_field = Entry(width=21)
username_password_entry = Entry(width=21)
password_entry = Entry(width=35)

# Buttons
search_button = Button(text="Seach", width=14, command=find_password)
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=35, command=save)

website_label.grid(column=0, row=3)
username_email_label.grid(column=0, row=4)
password_label.grid(column=0, row=5)

website_entry_field.grid(column=1, row=3)
website_entry_field.focus()
username_password_entry.grid(column=1, row=4)
username_password_entry.insert(0,"tmecius@gmail.com")
password_entry.grid(column=1, row=5, columnspan=2)

search_button.grid(column=2, row=3)
generate_button.grid(column=2, row=4)
add_button.grid(column=1, row=6, columnspan=2)

window.mainloop()