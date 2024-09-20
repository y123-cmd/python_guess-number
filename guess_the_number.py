def guess_the_number():
    secret_number = 7
    guess_count = 0
    guess = 0

    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        guess_count += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    print(f"You guessed it in {guess_count} tries!")

# Call the function to start the game
guess_the_number()
