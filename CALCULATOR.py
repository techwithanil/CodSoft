import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation.set('+')
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x280")
root.config(bg="#f0f0f0")

# Input fields and labels
tk.Label(root, text="Enter first number:", bg="#f0f0f0").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:", bg="#f0f0f0").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Select operation:", bg="#f0f0f0").pack(pady=5)
operation = tk.StringVar()
operation.set('+')  # default
tk.OptionMenu(root, operation, '+', '-', '*', '/').pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white").pack()

# Result display
result_label = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
