"""
Interactive Scientific Calculator (GUI Version)
Author: Anees Shaikh
Description: Sleek Dark-Mode Desktop Calculator UI built with Tkinter in Python 3.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

class ScientificCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator — Python 3")
        self.root.geometry("420x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#181825")

        self.expression = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Display Header
        header = tk.Label(self.root, text="SCIENTIFIC CALCULATOR", font=("Segoe UI", 10, "bold"), bg="#181825", fg="#89b4fa", pady=6)
        header.pack()

        # Calculation Display Screen
        self.display_var = tk.StringVar(value="0")
        display_frame = tk.Frame(self.root, bg="#11111b", padx=10, pady=10)
        display_frame.pack(fill="x", padx=15, pady=5)

        self.display = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            font=("Segoe UI", 24, "bold"), 
            bg="#11111b", 
            fg="#cdd6f4", 
            anchor="e",
            padx=10,
            pady=15
        )
        self.display.pack(fill="x")

        # Buttons Grid Frame
        btn_frame = tk.Frame(self.root, bg="#181825")
        btn_frame.pack(fill="both", expand=True, padx=15, pady=10)

        buttons = [
            ('Sin', '#313244', '#cdd6f4'), ('Cos', '#313244', '#cdd6f4'), ('Log', '#313244', '#cdd6f4'), ('√', '#313244', '#cdd6f4'), ('C', '#f38ba8', '#11111b'),
            ('^', '#313244', '#cdd6f4'), ('(', '#313244', '#cdd6f4'), (')', '#313244', '#cdd6f4'), ('%', '#313244', '#cdd6f4'), ('÷', '#fab387', '#11111b'),
            ('7', '#45475a', '#cdd6f4'), ('8', '#45475a', '#cdd6f4'), ('9', '#45475a', '#cdd6f4'), ('×', '#fab387', '#11111b'), ('⌫', '#f38ba8', '#11111b'),
            ('4', '#45475a', '#cdd6f4'), ('5', '#45475a', '#cdd6f4'), ('6', '#45475a', '#cdd6f4'), ('-', '#fab387', '#11111b'), ('', '#181825', '#181825'),
            ('1', '#45475a', '#cdd6f4'), ('2', '#45475a', '#cdd6f4'), ('3', '#45475a', '#cdd6f4'), ('+', '#fab387', '#11111b'), ('', '#181825', '#181825'),
            ('0', '#45475a', '#cdd6f4'), ('.', '#45475a', '#cdd6f4'), ('π', '#313244', '#cdd6f4'), ('=', '#a6e3a1', '#11111b'), ('', '#181825', '#181825')
        ]

        row = 0
        col = 0
        for text, bg_color, fg_color in buttons:
            if text == '':
                col += 1
                if col > 4:
                    col = 0
                    row += 1
                continue

            btn = tk.Button(
                btn_frame, 
                text=text, 
                font=("Segoe UI", 11, "bold"),
                bg=bg_color, 
                fg=fg_color,
                activebackground="#585b70",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == '=':
            self.calculate()
        elif char == 'Sin':
            self.eval_func(math.sin, "sin")
        elif char == 'Cos':
            self.eval_func(math.cos, "cos")
        elif char == 'Log':
            self.eval_func(math.log10, "log")
        elif char == '√':
            self.eval_func(math.sqrt, "√")
        elif char == 'π':
            self.expression += str(math.pi)
            self.display_var.set(self.expression)
        elif char == '^':
            self.expression += "**"
            self.display_var.set(self.expression)
        elif char == '×':
            self.expression += "*"
            self.display_var.set(self.expression)
        elif char == '÷':
            self.expression += "/"
            self.display_var.set(self.expression)
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def eval_func(self, func, name):
        try:
            val = float(self.expression) if self.expression else 0
            if name in ["sin", "cos"]:
                res = func(math.radians(val))
            else:
                res = func(val)
            self.display_var.set(f"{res:.6g}")
            self.expression = str(res)
        except Exception as e:
            messagebox.showerror("Math Error", f"Invalid operation for {name}: {e}")
            self.expression = ""
            self.display_var.set("Error")

    def calculate(self):
        try:
            res = eval(self.expression)
            formatted_res = f"{res:.8g}" if isinstance(res, float) else str(res)
            self.display_var.set(formatted_res)
            self.expression = formatted_res
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
            self.display_var.set("Error")
            self.expression = ""
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculatorGUI(root)
    root.mainloop()
