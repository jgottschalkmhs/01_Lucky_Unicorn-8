 # function goes here
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} and {}".format(low, high)

        try:
            response = int(input("How much money would you like to spend? Please enter a number between {} and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

num_1 = intcheck("Enter a number between 1 and 10", 1, 10)