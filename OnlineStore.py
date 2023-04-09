import tkinter as tk
from tkinter import ttk, PhotoImage


class OnlineStoreApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Online Store")
        self.geometry("600x400")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (ProductCatalogPage, CartPage, CheckoutPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ProductCatalogPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ProductCatalogPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Product Catalog")
        label.pack(pady=10, padx=10)

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")

        product_list = tk.Listbox(self, yscrollcommand=scrollbar.set)

        for i in range(10):
            product_list.insert(tk.END, f"Product {i+1}")

        product_list.pack(side="left", fill="both")
        scrollbar.config(command=product_list.yview)

        button = ttk.Button(self, text="Go to Cart",
                            command=lambda: controller.show_frame(CartPage))
        button.pack(pady=10)


class CartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Cart")
        label.pack(pady=10, padx=10)

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")

        cart_list = tk.Listbox(self, yscrollcommand=scrollbar.set)

        for i in range(5):
            cart_list.insert(tk.END, f"Product {i+1}")

        cart_list.pack(side="left", fill="both")
        scrollbar.config(command=cart_list.yview)

        button = ttk.Button(self, text="Go to Checkout",
                            command=lambda: controller.show_frame(CheckoutPage))
        button.pack(pady=10)


class CheckoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Checkout")
        label.grid(row=0, column=0, pady=10, padx=10)

        ttk.Label(self, text="Name:").grid(
            row=1, column=0, padx=(10, 0), sticky="w")
        ttk.Entry(self).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, text="Address:").grid(
            row=2, column=0, padx=(10, 0), sticky="w")
        ttk.Entry(self).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self, text="Phone:").grid(
            row=3, column=0, padx=(10, 0), sticky="w")
        ttk.Entry(self).grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(self, text="Shipping Options:").grid(
            row=4, column=0, padx=(10, 0), sticky="w")

        shipping_var = tk.StringVar()
        shipping_var.set("standard")
        ttk.Radiobutton(self, text="Standard Shipping", variable=shipping_var,
                        value="standard").grid(row=4, column=1, padx=10, pady=10, sticky="w")
        ttk.Radiobutton(self, text="Express Shipping", variable=shipping_var,
                        value="express").grid(row=5, column=1, padx=10, pady=0, sticky="w")

        ttk.Label(self, text="Preferred Delivery Time:").grid(
            row=6, column=0, padx=(10, 0), sticky="w")
        delivery_time_slider = ttk.Scale(
            self, from_=1, to=24, orient="horizontal")
        delivery_time_slider.grid(row=6, column=1, padx=10, pady=10)

        button = ttk.Button(self, text="Place Order",
                            command=controller.quit)
        button.grid(row=7, column=1, pady=10)


if __name__ == "__main__":
    app = OnlineStoreApp()
    app.mainloop()
