import random

inputStr = input("Enter the minimum and maximum number separated by a space: \n").split()

if len(inputStr) != 2:
        print("Please enter the minimum and maximum number separated by a space.")
        exit()
else:
    try:
        min = int(inputStr[0])
        max = int(inputStr[1])

        if max <= min:
            print("The maximum number must be greater than the minimum number.")
            exit()

    except:
        print("Please enter a valid number.")
        exit()

guess_number = random.randint(min, max)


while True:
    user_answer = input(f"Guess a number between {min} and {max}:\n")
    try:
        user_answer = int(user_answer)
    except:
        print("Please enter a valid number.")
        continue

    if user_answer == guess_number:
        print("Congratulations! You guessed the number!!!")
        break
    elif user_answer < guess_number:
        print("The number is higher.")
    else:
        print("The number is lower.")