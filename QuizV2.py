import tkinter as tk
from tkinter import ttk


class QuizAppV2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz App - Version 2")
        self.geometry("600x400")

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (StartPageV2, QuestionPageV2, ResultPageV2):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPageV2)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class StartPageV2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.image = tk.PhotoImage(file="start_image.png")
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.pack(pady=10)

        self.start_button = ttk.Button(
            self, text="Start Quiz", command=lambda: controller.show_frame(QuestionPageV2))
        self.start_button.pack(pady=10)

        self.difficulty_label = ttk.Label(
            self, text="Select difficulty level:")
        self.difficulty_label.pack(pady=5)

        self.slider = ttk.Scale(self, from_=1, to=3, orient="vertical")
        self.slider.set(1)
        self.slider.pack(pady=10)


class QuestionPageV2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.image = tk.PhotoImage(file="question_image.png")
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.pack(pady=10)

        self.question_label = ttk.Label(
            self, text="Which color matches the RGB values (255, 0, 0)?")
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio1 = ttk.Radiobutton(
            self, text="Red", value="red", variable=self.radio_var)
        self.radio1.pack(pady=5)
        self.radio2 = ttk.Radiobutton(
            self, text="Green", value="green", variable=self.radio_var)
        self.radio2.pack(pady=5)
        self.radio3 = ttk.Radiobutton(
            self, text="Blue", value="blue", variable=self.radio_var)
        self.radio3.pack(pady=5)

        self.submit_button = ttk.Button(
            self, text="Submit", command=lambda: self.check_answer(controller))
        self.submit_button.pack(pady=10)

    def check_answer(self, controller):
        if self.radio_var.get() == "red":
            controller.frames[ResultPageV2].result_label[
                "text"] = "Correct! The RGB values (255, 0, 0) represent Red."
        else:
            controller.frames[ResultPageV2].result_label[
                "text"] = "Incorrect! The RGB values (255, 0, 0) represent Red."
        controller.show_frame(ResultPageV2)


class ResultPageV2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.image = tk.PhotoImage(file="results_image.png")
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.restart_button = ttk.Button(
            self, text="Restart Quiz", command=lambda: controller.show_frame(StartPageV2))
        self.restart_button.pack(pady=10)

        self.text_box = tk.Text(self, wrap="word", height=6)
        self.text_box.pack(fill="both", expand=True)
        self.text_box.insert(
            "end", "Thank you for participating in the quiz.\n\nYour score will be displayed here.")
        self.text_box.config(state="disabled")

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")
        self.text_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_box.yview)


if __name__ == "__main__":
    app_v2 = QuizAppV2()
    app_v2.mainloop()
