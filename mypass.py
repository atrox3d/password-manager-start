import random
import pyperclip
import json

PASSWORD_TXTFILE = "mypass.txt"
PASSWORD_JSONFILE = "mypass.json"

APPEND = 'a'
WRITE = 'w'
READ = 'r'

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def save_text(website, account, password):
    with open(PASSWORD_TXTFILE, APPEND) as file:
        print(f"saving: {website} | {account} | {password} on {PASSWORD_TXTFILE}")
        file.write(f"{website} | {account} | {password}\n")
    return True


def save_json(website, account, password):
    # format the new data
    new_data = {
        website: {
            "account":  account,
            "password": password,
        }
    }

    try:
        with open(PASSWORD_JSONFILE, READ) as file:     # try to open file for reading
            data = json.load(file)                      # if succesful, load data from json file
    except FileNotFoundError:
        with open(PASSWORD_JSONFILE, WRITE):            # create file if it doesnt exist
            data = {}                                   # create empty dictionary
    finally:
        data.update(new_data)                           # update the dictionary with the new data
        with open(PASSWORD_JSONFILE, WRITE) as file:    # open file to write json dictionary
            json.dump(data, file, indent=4)             # save all of the data
        return True


#
# function pointer to current save method
#
save = save_json


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_numbers = [random.choice(NUMBERS) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    return password


def clipboard_copy(password):
    pyperclip.copy(password)
