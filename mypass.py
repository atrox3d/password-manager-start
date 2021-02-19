PASSWORD_FILE = "mypass.txt"
APPEND = 'a'


def save(website, email, password):
    with open(PASSWORD_FILE, APPEND) as file:
        print(f"saving: {website} | {email} | {password} on {PASSWORD_FILE}")
        file.write(f"{website} | {email} | {password}\n")


