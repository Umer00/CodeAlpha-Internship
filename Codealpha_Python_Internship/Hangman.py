import random

words = ["python", "hangman", "codealpha", "internship", "computer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if len(guess)!= 1 or not guess.isalpha():
        print("Please enter only 1 alphabet")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("\n🎉 You Won! The word was:", word)
else:
    print("\n💀 Game Over! The word was:", word)