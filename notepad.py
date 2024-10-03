from tkinter import *
from tkinter import font, filedialog

# Function to save the document
def save_doc():
    text = textarea.get("1.0","end-1c")
    location = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if location:
        with open(location, "w") as file:
            file.write(text)

# Function to change the font of the text area
def change_font(new_font_family):
    current_font = font.Font(font=textarea.cget("font"))
    current_font.config(family=new_font_family)
    textarea.config(font=current_font)

# Function to toggle bold text    
def toggle_doc():
    current_font = font.Font(font=textarea.cget("font"))
    current_weight = current_font.actual("weight")
    new_weight = "bold" if current_weight == "normal" else "normal"
    current_font.config(weight=new_weight)
    textarea.config(font=current_font)

# Initialize the root window
root = Tk()
root.title("Notepad")
root.geometry("600x400")

# Top frame for buttons
top_frame = Frame(root)
top_frame.pack(side=TOP, fill=x)

# Save Button
save_btn = Button(top_frame, text="Save", command=save_doc)
save_btn.pack(side=LEFT, padx=5, pady=5)

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
