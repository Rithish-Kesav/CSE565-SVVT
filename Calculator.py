import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan, log, log10, radians
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


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

    def on_button_click(self, text):
        if text == 'C':
            self.entry.delete(0, 'end')
            self.display_var.set("0")
        elif text == '=':
            try:
                result = eval(self.entry.get())
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set("Error")
        else:
            self.entry.insert('end', text)


class ScientificCalculatorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_label = tk.Label(
            self, textvariable=self.display_var, width=20, height=2, anchor='e')
        self.display_label.grid(row=0, column=0, columnspan=4)

        self.entry = tk.Entry(self, width=20)
        self.entry.grid(row=1, column=0, columnspan=4)

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

    def on_button_click(self, text):
        if text == 'C':
            self.entry.delete(0, 'end')
            self.display_var.set("0")
        elif text == '=':
            try:
                result = self.calculate()
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set("Error")
        else:
            self.entry.insert('end', text)

    def calculate(self):
        expression = self.entry.get()
        if '^' in expression:
            expression = expression.replace('^', '**')
        result = eval(expression)
        return result

    def evaluate_trigonometric(self, func, angle):
        if self.angle_mode.get() == 'DEG':
            angle = radians(angle)
        return func(angle)


class CurrencyConverterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.amount_var = tk.StringVar()
        self.amount_var.set("0")

        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_entry = tk.Entry(
            self, textvariable=self.amount_var, width=10)
        self.amount_entry.grid(row=0, column=1)

        self.from_currency_label = tk.Label(self, text="From:")
        self.from_currency_label.grid(row=1, column=0)

        self.from_currency_var = tk.StringVar()
        self.from_currency_var.set("USD")

        self.from_currency_list = ttk.Combobox(
            self, textvariable=self.from_currency_var, values=["USD", "EUR", "GBP", "JPY", "CAD"])
        self.from_currency_list.grid(row=1, column=1)

        self.to_currency_label = tk.Label(self, text="To:")
        self.to_currency_label.grid(row=2, column=0)

        self.to_currency_var = tk.StringVar()
        self.to_currency_var.set("EUR")

        self.to_currency_list = ttk.Combobox(self, textvariable=self.to_currency_var, values=[
                                             "USD", "EUR", "GBP", "JPY", "CAD"])
        self.to_currency_list.grid(row=2, column=1)

        self.convert_button = tk.Button(
            self, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2)

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(
            self, textvariable=self.result_var, width=20, height=2, anchor='e')
        self.result_label.grid(row=4, column=0, columnspan=2)

    def convert(self):
        amount = float(self.amount_var.get())
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        conversion_rate = self.get_conversion_rate(from_currency, to_currency)

        result = amount * conversion_rate
        self.result_var.set(str(round(result, 2)))

    def get_conversion_rate(self, from_currency, to_currency):
        # In a real-world application, you would use an API or an updated data source
        # to get accurate and up-to-date conversion rates.
        # Here, we are using a simple hard-coded conversion rate for demonstration purposes.

        rates = {
            "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.42, "CAD": 1.25},
            "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 130.02, "CAD": 1.47},
            "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 147.20, "CAD": 1.67},
            "JPY": {"USD": 0.0091, "EUR": 0.0077, "GBP": 0.0068, "CAD": 0.0113},
            "CAD": {"USD": 0.80, "EUR": 0.68, "GBP": 0.60, "JPY": 88.32}
        }

        if from_currency == to_currency:
            return 1
        else:
            return rates[from_currency][to_currency]


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
