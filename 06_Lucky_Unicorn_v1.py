# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} and {}".format(low, high)

        try:
            response = int(input("How much money would you like to spend? Please enter a number between ${} and ${}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main routine

# Explain rules to user
print("-" * 10)
print("Welcome to Lucky Unicorn!")
print("-" * 10)
print("In this game, you pay more to play more, and play more to win!")
print("-" * 10)
print("You will get an animal token each round. Each round costs $1.")
print("Horses and Zebras are worth 50c. Donkeys are worth nothing. However, Unicorns are worth $5!")
print("-" * 10)
print("Try your luck!")
print("-" * 10)

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? ", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

# Randomly choose a token from our list above
    token = random.choice(tokens)
    print()

    # Adjust total correctly for a given token and tell user
    if token == "unicorn":
        balance += 5    # wins $5
        print("***********************************************")
        print("***** Congratulations! You won a {}! *****".format(token))
        print("***********************************************")
        feedback = "You won $5!"
    elif token == "donkey":
        balance -= 1    # does not win anything (ie: loses $1)
        print("---------------------------------")
        print("----- Sorry, it's a {}. -----".format(token))
        print("---------------------------------")
        feedback = "You didn't win anything this round."
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("<<< Good try. You got a {}. >>>".format(token))
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        feedback = "You won back 50c."

    print()

    print(feedback)
    print("You have ${:.2f} to play with".format(balance))
    print("-" * 10)
    print()

    if balance < 1:
        print("Sorry you don't have enough money to continue. Game over.")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit.")
        print("-" * 10)

    # Money Calculations ...

# farewell user at end of game.
print("Thank you for playing.")
