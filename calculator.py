from tkinter import *

# Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
entry = Entry(root, font=("Arial", 20), borderwidth=5, relief=RIDGE, justify="right")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Function to insert values
def click(value):
    entry.insert(END, value)

# Function to clear screen
def clear():
    entry.delete(0, END)

# Function to evaluate expression
def calculate():
    try:
        expression = entry.get()

        # Replace symbols
        expression = expression.replace("^", "**")
        expression = expression.replace("\\", "//")

        result = eval(expression)

        entry.delete(0, END)
        entry.insert(END, str(result))

    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '%', '^', '+'],
    ['\\', 'C', '=', ]
]

# Create buttons
for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "C":
            Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=clear
            ).pack(side="left", expand=True, fill="both")

        elif btn == "=":
            Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=calculate
            ).pack(side="left", expand=True, fill="both")

        else:
            Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=lambda b=btn: click(b)
            ).pack(side="left", expand=True, fill="both")

root.mainloop()