import math

def main():
    """Inputs the bounds of the range of numbers,
    and lets the user guess the computer's number until
    the guess is correct."""
    low = int(input("Enter the smaller number: "))
    high = int(input("Enter the larger number: "))
    count = 0
    maxGuesses = round(math.log(high - low + 1, 2))
    while True:
        count += 1
        myNumber = (low + high) // 2
        print("Your number is", myNumber)
        answer = input("Enter =, <, or >: ")
        if answer == "=":
            print("Hooray, I've got it in", count, "tries!")
            break
        elif count == maxGuesses:
            print("You're cheating!")
            break
        elif answer == "<":
            high = myNumber - 1
        else:
            low = myNumber + 1

if __name__ == "__main__":
    main()
