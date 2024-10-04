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

def enable_drawing():
    textarea.grid_remove()
    canvas.grid(row=2, columnspan=3)

def disable_drawing():
    canvas.grid_remove()
    textarea.grid(row=2,columnspan=3)

# Drawing functions
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill="black", width=2)
    last_x, last_y = event.x, event.y

root = Tk()
root.title("Zeus.Notepad")

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

# Pencil Button (to switch to drawing mode)
pencil_btn = Button(root, text="Pencil", command=enable_drawing)
pencil_btn.grid(row=1, column=3)

# Exit Drawing Mode Button
exit_drawing_btn = Button(root, text="Exit Drawing", command=disable_drawing)
exit_drawing_btn.grid(row=1, column=4)

# Text Area
textarea = Text(root)
textarea.grid(row=2, columnspan=3)

# Canvas for drawing
canvas = Canvas(root, bg="white", width=400, height=300)
canvas.grid(row=2, columnspan=3)
canvas.grid_remove()  # Hide canvas initially


canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Initial font configuration
default_font = font.Font(family="Arial", size=12)
textarea.config(font=default_font)

root.mainloop()