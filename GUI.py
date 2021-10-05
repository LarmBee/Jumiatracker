import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile

import main

root = tk.Tk()
root.resizable(False, False)
canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3, rowspan=7)

# logo
logo = Image.open("Logo2.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# label
instructions = tk.Label(root, text="Welcome to JUMIASTACK .Input your product :", font="Raleway")
instructions.place(x=120, y=150)


# labels
def show_entry_fields():
    search_term = e1.get()



Search_Term = Label(text="SEARCH_TERM :", )
Search_Term.place(x=15, y=190)
# Search_Term_Entry = Entry(root,textvariable = "Search",width = "50")
e1 = tk.Entry(root, width="50")
e1.place(x=115, y=190)
search_term = e1.get()
# Search_Term_Entry.place (x = 115 , y = 190)


Price_Range = Label(text="PRICE_RANGE :", )
Price_Range.place(x=15, y=220)
Price_Range_Entry = Entry(textvariable="price", width="50")
Price_Range_Entry.place(x=115, y=220)

Email = Label(text="EMAIL :", )
Email.place(x=15, y=250)
Email_Entry = Entry(textvariable="email", width="50")
Email_Entry.place(x=115, y=250)


# create function to save file as
def save_file():
    browse_text.set("Saving...")
    file = asksaveasfile(initialfile="Products.xlsx", defaultextension=".xlsx",
                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    browse_text.set("Browse")


# shows in text box .Should be script instructions
page_content = "Hello world"

# text box
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.insert(1.0, page_content)
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
text_box.grid(column=1, row=4)

# save button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command =main.run, font ="Raleway", bg ="#20bebe", fg ="white", height = 2, width =15)
browse_text.set("SUBMIT")
browse_btn.place(x=150, y=550)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3, rowspan=3)

root.mainloop()
