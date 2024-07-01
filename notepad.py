from tkinter import *
from tkinter import font, filedialog

def save_doc():
    text = textarea.get("1.0","end-1c")
    location = filedialog.asksaveasfilename()
    if location:
        with open(location, "w") as file:
            file.write(text)

def change_font(new_font):
    textarea.config(font=new_font)

def bold_doc():
    current_font = textarea.cget("font")
    bold_font = font.Font(font=current_font)
    bold_font.configure(weight="bold")
    textarea.config(font=bold_font)

root = Tk()
root.title("Notepad")

# Save Button
save_btn = Button(root, text="Save", command=save_doc)
save_btn.grid(row=1, column=0)

# Font Menu
font_btn = Menubutton(root, text="Font")
font_btn.grid(row=1, column=1)

font_menu = Menu(font_btn, tearoff=0)
font_btn["menu"] = font_menu

font_names = ["Arial", "Algerian", "Cambria", "Courier"]
for font_name in font_names:
    font_menu.add_radiobutton(label=font_name, command=lambda f=font_name: change_font(f))

# Bold Button
bold_btn = Button(root, text="Bold", command=bold_doc)
bold_btn.grid(row=1, column=2)

# Text Area
textarea = Text(root)
textarea.grid(row=2, columnspan=3)

# Initial font configuration
default_font = font.Font(family="Arial", size=12)
textarea.config(font=default_font)

root.mainloop()
