import customtkinter as ctk
import random
import string

# Initialize window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Random Password Generator")
app.geometry("400x350")

# Function to generate password
def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            result_label.configure(text="Enter a valid length!")
            return
    except ValueError:
        result_label.configure(text="Enter a number!")
        return

    chars = ""
    if letters_var.get():
        chars += string.ascii_letters
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        result_label.configure(text="Select at least one option!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_label.configure(text=password)

# Title
title_label = ctk.CTkLabel(app, text="🔐 Random Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

# Length input
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

length_label = ctk.CTkLabel(frame, text="Password Length:")
length_label.pack(side="left", padx=5)

length_entry = ctk.CTkEntry(frame, width=80)
length_entry.pack(side="left", padx=5)

# Checkboxes
letters_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

letters_check = ctk.CTkCheckBox(app, text="Include Letters (A-Z)", variable=letters_var)
letters_check.pack(pady=3)
numbers_check = ctk.CTkCheckBox(app, text="Include Numbers (0-9)", variable=numbers_var)
numbers_check.pack(pady=3)
symbols_check = ctk.CTkCheckBox(app, text="Include Symbols (!@#)", variable=symbols_var)
symbols_check.pack(pady=3)

# Button
generate_btn = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_btn.pack(pady=15)

# Result Label
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14, "bold"), wraplength=350)
result_label.pack(pady=10)

# Run App
app.mainloop()