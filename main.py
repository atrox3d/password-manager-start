import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
account_label = tkinter.Label(text="Email/username:")
account_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = tkinter.Entry(
    # width=35
)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry = tkinter.Entry(
    # width=35
)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = tkinter.Entry(
    # width=21
)
password_entry.grid(row=3, column=1, sticky="EW")

# buttons
generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = tkinter.Button(text="add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


########################################################################
#
#   MAINLOOP
#
########################################################################
window.mainloop()
