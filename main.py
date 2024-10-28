from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    # To show generated password on Password entry field
    pass_entry.insert(0, password)
    # To automatically copy passwords to the clipboard when generated
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nemail:{username}\npassword:{password}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

    if website_entry == 0:
        messagebox.askretrycancel("Check the value you have entered")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()