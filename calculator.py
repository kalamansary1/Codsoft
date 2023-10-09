import tkinter as tk


def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")

    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", justify="right")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

for (text, row, col) in button_texts:
    button = tk.Button(frame, text=text, padx=20, pady=20,
                       font="lucida 15", relief="ridge")
    button.grid(row=row, column=col)
    button.bind("<Button-1>", click)

root.mainloop()
