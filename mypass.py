import random

PASSWORD_FILE = "mypass.txt"
APPEND = 'a'
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def save(website, email, password):
    with open(PASSWORD_FILE, APPEND) as file:
        print(f"saving: {website} | {email} | {password} on {PASSWORD_FILE}")
        file.write(f"{website} | {email} | {password}\n")
    return True


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(LETTERS) for char in range(nr_letters)]
    password_list.extend(password_letters)

    password_symbols = [random.choice(SYMBOLS) for char in range(nr_symbols)]
    password_list.extend(password_symbols)

    password_numbers = [random.choice(NUMBERS) for char in range(nr_numbers)]
    password_list.extend(password_numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password
