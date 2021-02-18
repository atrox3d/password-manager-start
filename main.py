import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(
    row=1,
    column=1,
    columnspan=2
)

# account
account_label = tkinter.Label(text="Email/username:")
account_label.grid(row=2, column=0)
account_entry = tkinter.Entry(width=35)
account_entry.grid(
    row=2,
    column=1,
    columnspan=2
)


# account
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)
password_button = tkinter.Button(text="Generate Password")
password_button.grid(row=3, column=2)

# add
add_button = tkinter.Button(text="add", width=30)
add_button.grid(row=4, column=1, columnspan=2)


########################################################################
#
#   MAINLOOP
#
########################################################################
window.mainloop()
