import json
import random

def load_word_list(filename):
    
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def choose_word(word_list):
    
    return random.choice(word_list)

def display_word(word, guessed_letters):
    
    displayed_word = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def guess_letter(guessed_letters):
    
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess not in guessed_letters:
                return guess
            else:
                print("You already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a single letter.")

def play_round(word, category, player_name):

    max_attempts = len(word) + 3
    guessed_letters = set()

    for attempt in range(1, max_attempts + 1):
        print(f"\n\nPlayer: {player_name}")
        print(f"Category: {category}")
        hidden_word = ""
        for letter in word:
            if letter.lower() in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"
        print(hidden_word)
        guess = input("Guess a letter: ").lower()
        while len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
            guess = input("Invalid guess. Please enter a single letter you haven't guessed yet: ").lower()
        guessed_letters.add(guess)

        if guess in word.lower():
            print("Correct!")
        else:
            print("Incorrect.")

        if hidden_word == word:
            print(f"\nCongratulations, {player_name}, you guessed the word!")
            break

    if attempt == max_attempts:
        print(f"\nSorry, {player_name}. You ran out of attempts. The word was: {word}")


def main():
    filename = "/Users/memmiofen/Desktop/mego /michael project/words_list.json"
    word_list = load_word_list(filename)
    word_data = choose_word(word_list)
    word, category = word_data["word"], word_data["category"]
    player_name = input("Enter your name: ")
    play_round(word, category, player_name)

if __name__ == "__main__":
    main()

