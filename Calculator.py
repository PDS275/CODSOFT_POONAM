import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    else:
        result = "Invalid operation"

    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create operation selection
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

# Create Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create label for displaying result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the main loop
root.mainloop()
SS