import tkinter as tk


def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Implement your registration logic here
    if password == confirm_password:
        # Registration successful
        message_label.config(text="Registration Successful")
    else:
        # Passwords do not match
        message_label.config(text="Password and Confirm Password do not match")


# Create a GUI window
root = tk.Tk()
root.title("Registration Page")

# Username Entry Widget
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password Entry Widget
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Passwords are hidden
password_entry.pack()

# Confirm Password Entry Widget
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")  # Passwords are hidden
confirm_password_entry.pack()

# Register Button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

# Message Label
message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
