import tkinter as tk
root = tk.Tk()
root.title("Multiply Two Numbers")
root.geometry("300x200")
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()