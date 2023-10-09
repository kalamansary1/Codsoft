import random
import string
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Task 3 Password Generator")
root.geometry("700x450+400+100")
root.resizable(False, False)
root.configure(bg="#55ddf2")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_button_click():
    try:
        password_length = int(length_entry.get())

        if password_length <= 0:
            messagebox.showerror(
                "Error", "Password length should be a positive integer.")
        else:
            generated_password = generate_password(password_length)
            generated_password_label.config(text=" " + generated_password)
            accept_button.config(state=tk.NORMAL)
            reset_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror(
            "Error", "Invalid input. Please enter a valid integer.")


def accept_button_click():
    accepted_password.set(generated_password_label.cget("text")[1:])
    messagebox.showinfo("Successfull", "Password is Accepted Successfully.")
    accept_button.config(state=tk.DISABLED)


def reset_button_click():
    generated_password_label.config(text=" ")
    accepted_password.set("")
    accept_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.DISABLED)


username_label = tk.Label(root,
                          text="Enter username:",
                          width=13,
                          font=("arial", 23, "bold"),
                          fg="#fff",
                          bg="green")
username_label.place(x=50, y=20)

username_entry = tk.Entry(root,
                          width=15,
                          font=("arial", 23, "bold"))
username_entry.place(x=340, y=20)

length_label = tk.Label(root, text="Enter password length:",
                        width=18,
                        font=("arial", 20, "bold"),
                        fg="#fff",
                        bd=2,
                        bg="green")
length_label.place(x=16, y=90)

length_entry = tk.Entry(root,
                        width=15,
                        bd=2,
                        font=("arial", 23, "bold"))
length_entry.place(x=340, y=90)

password_label = tk.Label(root, text=" Generated Password: ",
                          width=17,
                          height=2,
                          font=("arial", 15, "bold"),
                          fg="#fff",
                          bd=2,
                          bg="green")
password_label.place(x=50, y=160)

generated_password_label = tk.Label(root,
                                    text=" ",
                                    width=30,
                                    height=2,
                                    font=("arial", 15, "bold"),
                                    fg="#fff",
                                    bd=2,
                                    bg="#f59d0f")
generated_password_label.place(x=300, y=160)

generate_button = tk.Button(root,
                            text="Generate Password",
                            width=15,
                            font=("arial", 23, "bold"),
                            bd=3,
                            fg="#fff",
                            bg="#f011e1",
                            command=generate_button_click)
generate_button.place(x=230, y=230)

accept_button = tk.Button(root,
                          text="Accept",
                          width=6,
                          font=("arial", 18, "bold"),
                          bd=3,
                          fg="#fff",
                          command=accept_button_click,
                          state=tk.DISABLED)
accept_button.place(x=260, y=310)

reset_button = tk.Button(root,
                         text="Reset",
                         width=6,
                         font=("arial", 18, "bold"),
                         bd=3,
                         fg="#fff",
                         command=reset_button_click,
                         state=tk.DISABLED)
reset_button.place(x=390, y=310)

accepted_password = tk.StringVar()
accepted_password_label = tk.Label(root,
                                   width=30,
                                   height=2,
                                   font=("arial", 15, "bold"),
                                   fg="#fff",
                                   bd=2,
                                   bg="green",
                                   textvariable=accepted_password)
accepted_password_label.place(x=200, y=380)
# Start the GUI event loop
root.mainloop()
