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
def toggle_bold():
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
top_frame.pack(side=TOP, fill=X)

# Save Button
save_btn = Button(top_frame, text="Save", command=save_doc)
save_btn.pack(side=LEFT, padx=5, pady=5)

# Font dropdown menu
font_var = StringVar(value="Arial")  # Default font
font_menu = OptionMenu(top_frame, font_var, "Arial", "Algerian", "Cambria", "Courier", command=change_font)
font_menu.pack(side=LEFT, padx=5, pady=5)

# Bold button
bold_btn = Button(top_frame, text="Bold", command=toggle_bold)
bold_btn.pack(side=LEFT, padx=5, pady=5)

# Text area
textarea = Text(root, wrap=WORD, undo=True, font=("Arial", 12))
textarea.pack(expand=True, fill=BOTH, padx=5, pady=5)

# Set the initial font configuration
textarea.config(font=font.Font(family="Arial", size=12))

# Run the application
root.mainloop()