import tkinter
from tkinter import messagebox
import mypass


def search():
    website = website_entry.get()
    try:
        account, password = mypass.search(website)
        if account is not None:
            # update fields
            account_entry.delete(0, tkinter.END)
            account_entry.insert(0, account)
            password_entry.delete(0, tkinter.END)
            password_entry.insert(0, password)

            tkinter.messagebox.showinfo(title=website, message=f"{account}\n{password}")
        else:
            tkinter.messagebox.showinfo(title=website, message=f"no details for {website}")
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title=website, message=f"no data file found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = mypass.generate_password()

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    mypass.clipboard_copy(password)
    tkinter.messagebox.showinfo(title="clipboard", message="password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate(website, account, password):
    return len(website) != 0 and len(account) != 0 and len(password) != 0


def save():
    website = website_entry.get()
    account = account_entry.get()
    password = password_entry.get()

    if not validate(website, account, password):
        tkinter.messagebox.showerror(title="ERROR", message="Please don't leave any fields empty!")
    else:
        # at the moment mypass.save() returns True
        if mypass.save(website, account, password):
            tkinter.messagebox.showinfo(title=website, message="account saved correctly")
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# logo
canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# website
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# search button
search_button = tkinter.Button(text="Search", width=30, command=search)
search_button.grid(row=1, column=2, sticky="EW")

# account
account_label = tkinter.Label(text="Email/username:")
account_label.grid(row=2, column=0)
account_entry = tkinter.Entry(width=35)
account_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
account_entry.insert(0, "insert@email.here")

# password
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")
password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

# add
add_button = tkinter.Button(text="add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

########################################################################
#
#   MAINLOOP
#
########################################################################
window.mainloop()
