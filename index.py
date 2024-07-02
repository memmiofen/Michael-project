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
    
    guessed_letters = set()
    while True:
        print(f"\nPlayer: {player_name}")
        print(f"Category: {category}")
        print(display_word(word, guessed_letters))
        guess = guess_letter(guessed_letters)
        guessed_letters.add(guess)
        if guess in word.lower():
            print("Correct!")
        else:
            print("Incorrect.")
        if display_word(word, guessed_letters) == word:
            print(f"\nCongratulations, {player_name}, you guessed the word!")
            break

def main():
    filename = "/Users/memmiofen/Desktop/mego /michael project/words_list.json"
    word_list = load_word_list(filename)
    word_data = choose_word(word_list)
    word, category = word_data["word"], word_data["category"]
    player_name = input("Enter your name: ")
    play_round(word, category, player_name)

if __name__ == "__main__":
    main()

