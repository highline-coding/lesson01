import random

secret_number = random.choice(range(101))

guess_counter = 0

while True:
    guess = input("Enter a number or 'q' to quit\t")
    if guess == 'q':
        break
    else:
        try:
            my_guess = int(guess)
            guess_counter += 1
        except:
            print("That's not an Integer! (Whole Number)")
    
    if my_guess == secret_number:
        print("You Win!")
        print("It took {0} guesses".format(guess_counter))
        break
    elif my_guess < secret_number:
        print("Too low... Try a larger number")
    elif my_guess > secret_number:
        print("Too high... Try a smaller number")
