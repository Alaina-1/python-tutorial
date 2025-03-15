from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):

    def __init__(self):
        super().__init__(title="Number Guessing Game")
        self.setSize(400, 200)
        self.setResizable(False)
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.addLabel("Guess a number between 1 and 100!", row=0, column=0, columnspan=2, sticky="NSEW")
        self.inputField = self.addIntegerField(value=0, row=1, column=0, sticky="EW")
        self.addButton("Check", row=1, column=1, command=self.check_guess)
        self.resultLabel = self.addLabel("", row=2, column=0, columnspan=2, sticky="NSEW")

    def check_guess(self):
        """Handles the user's guess and provides feedback."""
        user_guess = self.inputField.getNumber()
        self.attempts += 1

        if user_guess < self.secret_number:
            self.resultLabel["text"] = "Try a higher number!"
        elif user_guess > self.secret_number:
            self.resultLabel["text"] = "Try a lower number!"
        else:
            self.resultLabel["text"] = f"🎉 Correct! You guessed it in {self.attempts} tries."
            self.inputField["state"] = "disabled"  

if __name__ == "__main__":
    GuessingGame().mainloop()
