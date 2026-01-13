# Number Guessing game 

import random


def main():
    
    print("---Number Guessing Game---")

    number =random.randint(1,100)
    attempt = 0

    while True :
        try:

            guess = int(input("Guess the Number:"))
            attempt += 1

            if guess < number:

                print("Too low try again") 
            elif guess > number:
                print("Too high try again") 
            else:
                print(f"congratulations your guessed the number correctly in {attempt} attempts")
                break

        except ValueError:
            print("Please enter the numeric value")

if __name__ == "__main__":
    main()           
