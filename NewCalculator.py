import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan, log, log10, radians, pi, e
from PIL import ImageTk, Image


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.basic_calc_frame = BasicCalculatorFrame(self)
        self.scientific_calc_frame = ScientificCalculatorFrame(self)
        self.currency_converter_frame = CurrencyConverterFrame(self)

        self.notebook.add(self.basic_calc_frame, text='Basic Calculator')
        self.notebook.add(self.scientific_calc_frame,
                          text='Scientific Calculator')
        self.notebook.add(self.currency_converter_frame,
                          text='Currency Converter')


class BasicCalculatorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_label = tk.Label(
            self, textvariable=self.display_var, width=20, height=2, anchor='e')
        self.display_label.grid(row=0, column=0, columnspan=5)

        self.entry = tk.Entry(self, width=20)
        self.entry.grid(row=1, column=0, columnspan=5)

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2),
            ('-', 5, 3), ('*', 5, 4), ('/', 5, 5),
            ('C', 4, 4), ('=', 4, 5)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(
                self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

        # Checkbox for toggling between decimal and binary mode
        self.binary_mode_var = tk.BooleanVar()
        self.binary_mode_checkbox = tk.Checkbutton(
            self, text="Binary Mode", variable=self.binary_mode_var)
        self.binary_mode_checkbox.grid(row=6, column=0, columnspan=3)

        # Slider for font size adjustment
        self.font_size_var = tk.IntVar()
        self.font_size_var.set(10)
        self.font_size_slider = tk.Scale(
            self, from_=8, to=20, orient=tk.HORIZONTAL, variable=self.font_size_var, command=self.update_font_size)
        self.font_size_slider.grid(row=6, column=3, columnspan=2)

        # Listbox for calculation history
        self.calculation_history_listbox = tk.Listbox(self)
        self.calculation_history_listbox.grid(row=7, column=0, columnspan=3)

        # Drawing canvas
        # self.drawing_canvas = tk.Canvas(self, width=150, height=100, bg='white
        # self.drawing_canvas.grid(row=7, column=3, columnspan=2)

    def on_button_click(self, text):
        if text == 'C':
            self.entry.delete(0, 'end')
            self.display_var.set("0")
        elif text == '=':
            try:
                result = eval(self.entry.get())
                self.display_var.set(str(result))
                if self.binary_mode_var.get():
                    self.display_var.set(bin(int(result))[2:])
                self.calculation_history_listbox.insert(
                    tk.END, self.entry.get() + ' = ' + str(result))
            except Exception as e:
                self.display_var.set("Error")
        else:
            self.entry.insert('end', text)

    def update_font_size(self, value):
        font_size = self.font_size_var.get()
        self.display_label.config(font=("Arial", font_size))
        self.entry.config(font=("Arial", font_size))
        for child in self.winfo_children():
            if isinstance(child, tk.Button):
                child.config(font=("Arial", font_size))


class ScientificCalculatorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_text = tk.Text(self, wrap=tk.NONE, width=20, height=2)
        self.display_text.grid(row=0, column=0, columnspan=4)

        self.display_scrollbar = tk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.display_text.xview)
        self.display_scrollbar.grid(row=1, column=0, columnspan=4, sticky='ew')
        self.display_text.configure(xscrollcommand=self.display_scrollbar.set)

        # Replace the Entry widget with a Text widget
        self.entry = tk.Text(self, width=20, height=1, wrap=tk.NONE)
        self.entry.grid(row=2, column=0, columnspan=4)

        # Add a horizontal scrollbar to the entry Text widget
        self.entry_scrollbar = tk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.entry.xview)
        self.entry_scrollbar.grid(row=3, column=0, columnspan=4, sticky='ew')
        self.entry.configure(xscrollcommand=self.entry_scrollbar.set)

        buttons = [
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2),
            ('log', 3, 0), ('ln', 3, 1), ('^', 3, 2),
            ('C', 4, 0), ('=', 4, 1)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(
                self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

        self.angle_mode = tk.StringVar()
        self.angle_mode.set("DEG")

        self.angle_mode_radio_deg = tk.Radiobutton(
            self, text="Degrees", variable=self.angle_mode, value="DEG")
        self.angle_mode_radio_deg.grid(row=4, column=2)

        self.angle_mode_radio_rad = tk.Radiobutton(
            self, text="Radians", variable=self.angle_mode, value="RAD")
        self.angle_mode_radio_rad.grid(row=4, column=3)

        # Drop-down menu for mathematical constants
        self.math_constants_var = tk.StringVar()
        self.math_constants_var.set("Select constant")
        self.math_constants_options = {'pi': pi, 'e': e}
        self.math_constants_menu = ttk.OptionMenu(
            self, self.math_constants_var, *self.math_constants_options.keys(), command=self.insert_constant)
        self.math_constants_menu.grid(row=5, column=0, columnspan=2)

        # Scrollbar for display and entry widgets
        self.entry_scrollbar = tk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.entry.xview)
        self.entry_scrollbar.grid(row=2, column=0, columnspan=4, sticky='ew')
        self.entry.configure(xscrollcommand=self.entry_scrollbar.set)

        self.display_scrollbar = tk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.display_text.xview)
        self.display_scrollbar.grid(row=6, column=0, columnspan=4, sticky='ew')
        self.display_text.configure(xscrollcommand=self.display_scrollbar.set)

    def on_button_click(self, text):
        if text == 'C':
            self.entry.delete('1.0', tk.END)
            self.display_var.set("0")
        elif text == '=':
            try:
                result = self.eval_expr(self.entry.get('1.0', tk.END).strip())
                self.display_text.delete('1.0', tk.END)
                self.display_text.insert(tk.END, str(result))
            except Exception as e:
                self.display_text.delete('1.0', tk.END)
                self.display_text.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

    def eval_expr(self, expr):
        def trig_func(func, angle):
            if self.angle_mode.get() == "DEG":
                return func(radians(angle))
            else:
                return func(angle)

        expr = expr.replace('sin', 'trig_func(sin,')
        expr = expr.replace('cos', 'trig_func(cos,')
        expr = expr.replace('tan', 'trig_func(tan,')
        expr = expr.replace('log', 'log10(')
        expr = expr.replace('ln', 'log(')
        expr = expr.replace('^', '**')
        return eval(expr)

    def insert_constant(self, *args):
        self.entry.insert(
            tk.END, self.math_constants_options[self.math_constants_var.get()])


class CurrencyConverterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        # Currency selection
        self.currency_var_from = tk.StringVar()
        self.currency_var_to = tk.StringVar()

        self.currency_options = ['USD', 'EUR', 'JPY', 'GBP', 'CHF']

        self.currency_var_from.set(self.currency_options[0])
        self.currency_var_to.set(self.currency_options[1])

        self.currency_menu_from = ttk.OptionMenu(
            self, self.currency_var_from, *self.currency_options)
        self.currency_menu_from.grid(row=0, column=0)

        self.currency_menu_to = ttk.OptionMenu(
            self, self.currency_var_to, *self.currency_options)
        self.currency_menu_to.grid(row=0, column=2)

        # Entry and display widgets
        self.entry = tk.Entry(self, width=10)
        self.entry.grid(row=0, column=1)

        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_label = tk.Label(
            self, textvariable=self.display_var, width=10, height=2, anchor='w')
        self.display_label.grid(row=1, column=2)

        # Convert button
        self.convert_button = tk.Button(
            self, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=1, column=1)

    def convert_currency(self):
        # Dummy conversion rates (replace with real API calls)
        conversion_rates = {
            'USD': {'USD': 1, 'EUR': 0.85, 'JPY': 110.15, 'GBP': 0.72, 'CHF': 0.92},
            'EUR': {'USD': 1.18, 'EUR': 1, 'JPY': 129.86, 'GBP': 0.85, 'CHF': 1.08},
            'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'JPY': 1, 'GBP': 0.0065, 'CHF': 0.0083},
            'GBP': {'USD': 1.39, 'EUR': 1.18, 'JPY': 153.59, 'GBP': 1, 'CHF': 1.28},
            'CHF': {'USD': 1.09, 'EUR': 0.93, 'JPY': 120.24, 'GBP': 0.78, 'CHF': 1}
        }

        try:
            amount = float(self.entry.get())
            from_currency = self.currency_var_from.get()
            to_currency = self.currency_var_to.get()

            result = amount * conversion_rates[from_currency][to_currency]
            self.display_var.set(f'{result:.2f}')
        except ValueError:
            self.display_var.set("Error")


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
