from tkinter import *
import crypting

root = Tk()
root.title("Encrypt & Decrypt")
root.resizable(False,False)

filename_entry = Entry(width=50)
filename_label = Label(text="File or Directory name", padx=50)
password_label = Label(text="Password", padx=50)
password_entry = Entry(width=50)
decrypt_button = Button(text="Decrypt", pady=10, padx=50, command=lambda:crypting.decrypt_auto(filename_entry.get(), password_entry.get(), 'saltysalt', __file__))
encrypt_button = Button(text="encrypt", pady=10, padx=52, command=lambda:crypting.encrypt_auto(filename_entry.get(), password_entry.get(), 'saltysalt', __file__))
decrypt_button.grid(row=2, column=1)
encrypt_button.grid(row=2, column=0)
filename_label.grid(row=0, column=0, columnspan=2)
filename_entry.grid(row=1, column=0, columnspan=2)
password_entry.grid(row=4, column=0, columnspan=2)
password_label.grid(row=5, column=0, columnspan=2)



root.mainloop()
