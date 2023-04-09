import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class SurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Survey Application")
        self.geometry("400x400")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (WelcomePage, QuestionPage, ThankYouPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the Survey!")
        label.pack(pady=10, padx=10)

        img = ImageTk.PhotoImage(Image.open(
            "welcome_image.jpg").resize((200, 200), Image.ANTIALIAS))
        image_label = tk.Label(self, image=img)
        image_label.image = img
        image_label.pack()

        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.show_frame(QuestionPage))
        button1.pack()


class QuestionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="What is your favorite programming language?")
        label.pack(pady=10, padx=10)

        entry = tk.Entry(self)
        entry.pack()

        radio_var = tk.StringVar()
        radio_button1 = ttk.Radiobutton(
            self, text="Python", variable=radio_var, value="Python")
        radio_button1.pack()
        radio_button2 = ttk.Radiobutton(
            self, text="JavaScript", variable=radio_var, value="JavaScript")
        radio_button2.pack()

        check_var = tk.BooleanVar()
        check_button = ttk.Checkbutton(
            self, text="I agree to share my opinion", variable=check_var)
        check_button.pack()

        button1 = ttk.Button(self, text="Submit",
                             command=lambda: controller.show_frame(ThankYouPage))
        button1.pack()


class ThankYouPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Thank you for participating!")
        label.pack(pady=10, padx=10)

        img = ImageTk.PhotoImage(Image.open(
            "thanks_image.jpg").resize((200, 200), Image.ANTIALIAS))
        image_label = tk.Label(self, image=img)
        image_label.image = img
        image_label.pack()

        button1 = ttk.Button(self, text="Close",
                             command=controller.quit)
        button1.pack()


if __name__ == "__main__":
    app = SurveyApp()
    app.mainloop()
