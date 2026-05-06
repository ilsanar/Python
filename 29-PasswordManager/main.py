import random
import string
import pyperclip
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    length = 12
    password = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    ipt_pwd.delete(0, END)
    ipt_pwd.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = ipt_website.get()
    user = ipt_user.get()
    pwd = ipt_pwd.get()
    new_data = {
        website: {
            "email": user,
            "password": pwd,
        }
    }

    if len(pwd) == 0 or len(user) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Empty field", message="At least one of the fields is empty")
    else:
        is_ok = messagebox.askyesno(title=website,
                                    message=f"Do you want to save this input\n User: {user} Password: {pwd}")
        if is_ok:
            try:
                with open("./data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            ipt_pwd.delete(0, END)
            ipt_website.delete(0, END)


def search_website():
    search = ipt_website.get()
    if len(search) > 0:
        try:
            data_file = open("./data.json", "r")
        except FileNotFoundError:
            messagebox.showinfo(title="No data", message="File not found")
        else:
            data = json.load(data_file)
            if search in data:
                email = data[search]["email"]
                password = data[search]["password"]
                messagebox.showinfo(search, f"Username: {email}\nPassword: {password}")
            else:
                messagebox.showinfo("No Data", f"Entry {search} not found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20, bg="#ffffff")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="#FFFFFF")
padlock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:", bg="#ffffff")
lbl_website.grid(column=0, row=1, pady=2, padx=2, sticky=W)

ipt_website = Entry(width=30, relief="solid")
ipt_website.grid(column=1, columnspan=2, row=1, sticky=W, pady=2, padx=2)
ipt_website.focus()

btn_search = Button(text="Search", width=14, relief="flat", fg="#ffffff", bg="#E2A16F", activebackground="#FFF0DD",
                    command=search_website)
btn_search.grid(row=1, column=2, sticky=W, padx=2)

lbl_user = Label(text="Email/Username:", bg="#ffffff")
lbl_user.grid(row=2, column=0, pady=2, padx=2, sticky=W)

ipt_user = Entry(width=51, relief="solid")
ipt_user.grid(row=2, column=1, columnspan=2, sticky=W, pady=2, padx=2)
ipt_user.insert(END, "janzkijan@grzybowaplaneta.pl")

lbl_pwd = Label(text="Password:", bg="#ffffff")
lbl_pwd.grid(row=3, column=0, pady=2, padx=2, sticky=W)

ipt_pwd = Entry(width=30, relief="solid")
ipt_pwd.grid(row=3, column=1, sticky=W, pady=2, padx=2)

btn_gen_pwd = Button(text="Generate Password", relief="flat", fg="#ffffff", bg="#E2A16F", activebackground="#FFF0DD",
                     command=gen_password)
btn_gen_pwd.grid(row=3, column=2, pady=2, padx=2, sticky=W)

btn_add = Button(text="Add", width=43, relief="flat", fg="#ffffff", bg="#E2A16F", activebackground="#FFF0DD",
                 command=save_to_file)
btn_add.grid(row=4, column=1, columnspan=2, pady=2, padx=2, sticky=W)

window.mainloop()