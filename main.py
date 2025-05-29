import tkinter as tk
from tkinter import ttk, messagebox

def go_back():
    root.destroy()
    import main  # Go back to the main menu

# Create the main control panel window
root = tk.Tk()
root.title("Student Management - Control Panel")
root.geometry("600x500")
root.configure(bg="#2c3e50")

# Title Label
label = tk.Label(root, text="Control Panel", font=("Comic Sans MS", 16, "bold"), fg="#f1c40f", bg="#2c3e50")
label.pack(pady=10)

# Promotion Selection
tk.Label(root, text="Select Promotion:", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#2c3e50").pack(pady=5)
promotions = ["Promotion 1", "Promotion 2", "Promotion 3"]
promo_var = tk.StringVar(value=promotions[0])
promo_dropdown = ttk.Combobox(root, textvariable=promo_var, values=promotions, state="readonly")
promo_dropdown.pack(pady=5)

# Add Student Button
add_student_btn = tk.Button(root, text="Add Student", font=("Comic Sans MS", 12, "bold"), bg="#27ae60", fg="white", padx=10, pady=5, relief="raised", bd=5)
add_student_btn.pack(pady=5)

# Remove Student Button
remove_student_btn = tk.Button(root, text="Remove Student", font=("Comic Sans MS", 12, "bold"), bg="#e74c3c", fg="white", padx=10, pady=5, relief="raised", bd=5)
remove_student_btn.pack(pady=5)

# Go Back Button
go_back_btn = tk.Button(root, text="Back to Main Menu", command=go_back, font=("Comic Sans MS", 12, "bold"), bg="#3498db", fg="white", padx=10, pady=5, relief="raised", bd=5)
go_back_btn.pack(pady=20)

# Run the control panel
root.mainloop()

