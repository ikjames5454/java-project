import tkinter as tk
from diary import Diary
from diaries import Diaries


class DiaryMain:

    def __init__(self, naming):
        self.naming = naming
        self.naming.geometry("500x500")
        self.naming.title("Diary")
        self.menu()
        self.username = 0
        self.password = 0
        self.diaries = Diaries()
        self.diary = None

    def menu(self):
        self.textFunction(text="Welcome to MyDiaries", font=("James", 20))
        self.buttons()

    def buttons(self):
        self.button(text="Click me!", font=("James", 18), command=self.show_main_menu)

    def mainMenu(self):
        self.textFunction(text="Olofofo people una doo oh", font=("James", 20))
        self.button(text="Register", font=("James", 18), command=self.show_main_menu1)
        self.button(text="Login", font=("James", 18), command=self.show_main_menu)
        self.button(text="Delete", font=("James", 18), command=self.show_main_menu)

    def register(self):
        self.textFunction(text="Enter your name below to create username", font=("James", 16))
        username = self.textSize(height=2, font=("james", 8))
        self.username = username.get("1.0", "end-1c")
        self.textFunction(text="Enter a password below to create", font=("James", 16))
        password = self.textSize(height=2, font=("james", 8))
        self.password = password.get("1.0", "end-1c")
        self.diaries.add_diary(self.username, self.password)
        self.button(text="ok", font=("James", 18), command=self.show_main_menu2)

    def successMessage(self):
        self.textFunction(text=str(self.username), font=("James", 16))
        print(str(self.username))
        self.textFunction(text="name created successfully", font=("James", 16))
        self.button(text="ok", font=("James", 18), command=self.show_main_menu)

    def textFunction(self, text, font):
        label = tk.Label(self.naming, text=text, font=font)
        label.pack(padx=20, pady=20)
        return label

    def button(self, text, font, command=None):
        button = tk.Button(self.naming, text=text, font=font, command=command)
        button.pack()

    def show_main_menu(self):
        for widget in self.naming.winfo_children():
            widget.pack_forget()

        self.mainMenu()

    def show_main_menu1(self):
        for widget in self.naming.winfo_children():
            widget.pack_forget()
        self.register()

    def show_main_menu2(self):
        for widget in self.naming.winfo_children():
            widget.pack_forget()
        self.successMessage()

    def textSize(self, height, font):
        text = tk.Text(self.naming, height=height, font=font)
        text.pack(padx=10, pady=10)
        return text


if __name__ == "__main__":
    naming = tk.Tk()
    name = DiaryMain(naming)
    naming.mainloop()
