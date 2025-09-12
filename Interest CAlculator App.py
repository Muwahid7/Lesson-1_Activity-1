import tkinter as tk
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        si = (principal * time * rate) / 100
        ci = principal * ((1 + rate/100) ** time - 1)
        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
tk.Label(root, text="Enter Principal Amount:").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)
tk.Label(root, text="Enter Time (years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)
tk.Label(root, text="Enter Rate of Interest (%):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)
calc_button = tk.Button(root, text="Calculate", command=calculate_interest)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()
