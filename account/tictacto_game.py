from tkinter import *
import random


class TicTacToe:
    def __init__(self):
        self.access = Tk()
        self.access.title("TIC-TAC-TOE")
        self.access.geometry("400x400")
        self.players = ["#", "0"]
        self.player = random.choice(self.players)
        self.buttons = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        self.label = Label(self.access, text=self.player + " turn", font=("james", 40))
        self.label.pack(side="top")

        self.button_reset = Button(self.access, text="Restart", font=("james", 20), command=self.new_game)
        self.button_reset.pack(side="top")

        self.frame = Frame(self.access)
        self.frame.pack()

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(self.frame, text="", font=("james", 40), width=5, height=2,
                                                   command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]["text"] == "" and not self.check_winner():
            if self.player == self.players[0]:
                self.buttons[row][column]["text"] = self.player
                if not self.check_winner():
                    self.player = self.players[1]
                    self.label.config(text=(self.players[1] + " turn"))
                elif self.check_winner() is True:
                    self.label.config(text=(self.players[0] + " wins"))
                elif self.check_winner() == "Tie":
                    self.label.config(text=("Tie!"))
            else:
                self.buttons[row][column]["text"] = self.player
                if not self.check_winner():
                    self.player = self.players[0]
                    self.label.config(text=(self.players[0] + " turn"))
                elif self.check_winner() is True:
                    self.label.config(text=(self.players[1] + " wins"))
                elif self.check_winner() == "Tie":
                    self.label.config(text=("Tie!"))

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]["text"] == self.buttons[1][column]["text"] == self.buttons[2][column][
                "text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        elif self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        elif not self.empty_spaces():
            return "Tie"
        else:
            return False

    def empty_spaces(self):
        space = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]["text"] != "":
                    space -= 1
        return space > 0

    def new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " turn")
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="")

    def start(self):
        self.access.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
