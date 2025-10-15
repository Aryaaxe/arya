import random
print("welcome to the guessing game!")
count=0
count2=1
while True:
    print("I have selected a number between 1 and 25. Can you guess it?")
    n = random.randint(1, 25)
    while True:
        m = int(input("Enter your guess: "))
        if m < n:
            print("Your guess is too low. Try again.")
            count+=1
        elif m > n:
            print("Your guess is too high. Try again.")
            count+=1
        else:
            print("Congratulations! You've guessed the number correctly.")
            count+=1
            print("you took ",count,"chances to guess the number.")
            a = input("Do you want to play again? (yes/no): ")
            if a.lower() == 'yes':
                count2+=1
                break
            else:
                print("Thank you for playing! Goodbye!")
                print("You played", count2, "games in total.")