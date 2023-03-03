MAX_WORD_LENGTH = 10
MAX_GUESSES = len(set(input(f"Enter a word for someone to guess (Max {MAX_WORD_LENGTH}): ").lower()))

# Get the word to guess
while True:
    word = input(f"Enter a word for someone to guess (Max {MAX_WORD_LENGTH}): ").lower()
    if len(word) > MAX_WORD_LENGTH:
        print(f"The word should not be longer than {MAX_WORD_LENGTH} characters.")
    else:
        break

guessed_letters = []
incorrect_guesses = 0

hangman_correct = "😄"
hangman_incorrect = "😔"

while incorrect_guesses < MAX_GUESSES:
    # Print out the partially guessed word
    word_display = ""
    for letter in word:
        if letter in guessed_letters:
            word_display += letter
        else:
            word_display += "_"
    print(word_display)

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter or a space
    if len(guess) != 1 and guess != " ":
        print("Please enter a single letter or a space.")
        continue

    # Check if the guess has already been made
    if guess in guessed_letters:
        print(f"You have already guessed {guess} {guessed_letters.count(guess)} times.")
        continue

    # Check if the guess is correct
    if guess in word:
        guessed_letters.append(guess)
        print(f"Correct!\n\n{hangman_correct}\n")
    else:
        incorrect_guesses += 1
        print(f"Incorrect!\n\n{hangman_incorrect}\n")

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations, you have won!")
        break

# Check if the player has lost
if incorrect_guesses == MAX_GUESSES:
    print(f"Sorry, you have lost. The word was {word}")
