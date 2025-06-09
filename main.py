import tkinter as tk
from tkinter import messagebox

# Hàm xử lý tính toán
def calculate():
    try:
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
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Chọn phép toán"

        result_label.config(text="Kết quả: " + str(result))

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")

# Hàm reset
def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_var.set(None)
    result_label.config(text="Kết quả: ")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy tính đơn giản")
root.geometry("300x300")
root.resizable(False, False)

# Nhãn và ô nhập số thứ nhất
tk.Label(root, text="Nhập số thứ nhất:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Nhãn và ô nhập số thứ hai
tk.Label(root, text="Nhập số thứ hai:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Chọn phép toán
operation_var = tk.StringVar()
operation_var.set(None)

tk.Label(root, text="Chọn phép toán:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

tk.Radiobutton(root, text="+", variable=operation_var, value="+").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="-", variable=operation_var, value="-").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="×", variable=operation_var, value="*").grid(row=4, column=1, sticky="w")
tk.Radiobutton(root, text="÷", variable=operation_var, value="/").grid(row=5, column=1, sticky="w")

# Nút Tính
tk.Button(root, text="Tính", command=calculate, width=10).grid(row=6, column=0, pady=15)

# Nút Reset
tk.Button(root, text="Reset", command=reset, width=10).grid(row=6, column=1, pady=15)

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="Kết quả: ", font=("Arial", 12))
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Chạy vòng lặp giao diện
root.mainloop()
