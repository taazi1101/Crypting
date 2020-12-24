# -*- coding: utf-8 -*-
from tkinter import *
import base64

root = Tk()
root.resizable(False, False)
root.title("Decode and Encode")

def encode(message, password):
    print(message + " " + password)
    encoded = []

    for i in range(len(message)):
        key_c = password[i % len(password)]
        encoded.append(chr((ord(message[i]) + ord(key_c)) % 256))
    message_entry.delete(1.0, END)
    message_entry.insert(1.0, base64.urlsafe_b64encode("".join(encoded).encode()).decode())

def decode(message, password):
    decoded=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = password[i % len(password)]
        decoded.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    message_entry.delete(1.0, END)
    message_entry.insert(1.0, "".join(decoded))

def get_filename_import():
    filename_get = Tk()
    filename_get.resizable(False, False)
    filename_get.title("Filename")
    filename_entry = Entry(filename_get, width=50)
    enter_button = Button(filename_get, text="Enter", padx=150, pady=30, command=lambda: import_def(filename_entry.get(), filename_get))
    filename_entry.grid(row=0, column=0)
    enter_button.grid(row=1, column=0)

    filename_get.mainloop()

def get_filename_export():
    filename_get = Tk()
    filename_get.resizable(False, False)
    filename_get.title("Filename")
    filename_entry = Entry(filename_get, width=50)
    enter_button = Button(filename_get, text="Enter", padx=150, pady=30, command=lambda: export_def(filename_entry.get(), filename_get))
    filename_entry.grid(row=0, column=0)
    enter_button.grid(row=1, column=0)

    filename_get.mainloop()

def export_def(filename, win_name):
    win_name.destroy()
    file = open(filename, 'w')
    file.write(str(message_entry.get(1.0, END)))
    file.close()

def import_def(filename, win_name):
    if filename != "":
        message_entry.delete(1.0, END)
        win_name.destroy()
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            message_entry.insert(END, line)
        file.close()
    win_name.destroy()


message_entry = Text(width=200, height=45)
password_entry = Entry(width=200)
password_label = Label(text="Password")
message_entry.grid(row=0, column=0, columnspan=2)
password_label.grid(row=4, column=0, columnspan=2)
password_entry.grid(row=3, column=0, columnspan=2)
import_button = Button(text="Import", padx=380, pady=10, command=get_filename_import)
export_button = Button(text="Export", padx=380, pady=10, command=get_filename_export)
encode_button = Button(text="Encode", pady=10, padx=380, command=lambda: encode(message_entry.get(1.0, END), password_entry.get()))
decode_button = Button(text="Decode", pady=10, padx=380, command=lambda: decode(message_entry.get(1.0, END), password_entry.get()))
import_button.grid(row=2, column=0)
export_button.grid(row=2, column=1)
encode_button.grid(row=1, column=0)
decode_button.grid(row=1, column=1)

root.mainloop()
