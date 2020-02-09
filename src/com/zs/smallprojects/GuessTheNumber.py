import random;

# Enter a username
print("Enter a username: ")
name = input()

# Selection prompt
print(name + ", pick a number between 1 and 10")
generatedNumber = random.randint(1, 10)

# User selection
guessesTaken = 1;

while True:
    # ensures user enters a number
    try:
        guess = int(input())
    except ValueError:
        print('That was not a number. Try again: ')
        continue;

    # checks number against generated number
    if guess < generatedNumber:
        print('That guess is too low.  Try again: ')
        guessesTaken += 1
    elif guess > generatedNumber:
        print('That guess is too high. Try again: ')
        guessesTaken += 1
    else:
        print("That is correct.  It took you " + str(guessesTaken) + " guesses.")
        break;