import random


class Hangman:
    """
    A simple console-based Hangman game.
    """

    MAX_INCORRECT_GUESSES = 6

    WORDS = [
        "python",
        "developer",
        "computer",
        "keyboard",
        "programming"
    ]

    def __init__(self):
        self.secret_word = random.choice(self.WORDS)
        self.guessed_letters = set()
        self.incorrect_guesses = 0

    def display_word(self):
        """
        Returns the current progress of the word.
        Example: p _ t h o n
        """
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.secret_word
        )

    def display_status(self):
        """
        Shows game status.
        """
        print("\n" + "=" * 50)
        print("WORD:", self.display_word())
        print(
            f"INCORRECT GUESSES: "
            f"{self.incorrect_guesses}/{self.MAX_INCORRECT_GUESSES}"
        )

        if self.guessed_letters:
            print(
                "GUESSED LETTERS:",
                ", ".join(sorted(self.guessed_letters))
            )

        print("=" * 50)

    def get_guess(self):
        """
        Validates user input.
        """
        while True:
            guess = input("Enter a letter: ").strip().lower()

            if len(guess) != 1:
                print("Please enter only ONE letter.")
                continue

            if not guess.isalpha():
                print("Please enter a valid alphabet letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            return guess

    def process_guess(self, guess):
        """
        Process user's guess.
        """
        self.guessed_letters.add(guess)

        if guess in self.secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            self.incorrect_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

    def is_won(self):
        """
        Checks if player guessed all letters.
        """
        return all(
            letter in self.guessed_letters
            for letter in self.secret_word
        )

    def is_lost(self):
        """
        Checks if player exceeded max attempts.
        """
        return (
            self.incorrect_guesses >=
            self.MAX_INCORRECT_GUESSES
        )

    def play(self):
        """
        Main game loop.
        """
        print("\n🎯 Welcome to Hangman!")
        print("Guess the hidden word one letter at a time.\n")

        while not self.is_won() and not self.is_lost():
            self.display_status()

            guess = self.get_guess()
            self.process_guess(guess)

        print("\n" + "=" * 50)

        if self.is_won():
            print("🎉 Congratulations! You won!")
        else:
            print("💀 Game Over!")

        print(f"Secret Word: {self.secret_word}")
        print("=" * 50)


def main():
    game = Hangman()
    game.play()


if __name__ == "__main__":
    main()
