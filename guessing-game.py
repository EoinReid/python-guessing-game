# Guessing Game

# specify secret word, user has to guess a secret word.
# user can keep guessing until they get it correct

secret_word = "Eoin"
user_guess = ""
guess_count = 0
guess_limit = 3

while user_guess != secret_word and guess_count != guess_limit:
    user_guess = input("Guess the name: ")
    guess_count += 1
    if (user_guess == secret_word):
        print("Congrats, you correctly guessed: " +secret_word + " in "+str(guess_count)+" guesses")
    elif(guess_count == guess_limit):
        print("game over - you are out of guesses!")
    else:
        print("Uh oh, wrong guess, try again!")
