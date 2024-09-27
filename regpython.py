import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if name and email and password:
        # Here you can add code to save the data, e.g., to a database or file
        messagebox.showinfo("Registration", "Registration Successful!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entries for the form
label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show='*')
entry_password.pack()

# Create a Register button
button_register = tk.Button(root, text="Register", command=register)
button_register.pack()

# Run the application
root.mainloop()
