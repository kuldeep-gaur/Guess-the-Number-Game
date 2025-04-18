import random
n = random.randint(1, 100)
a =-1
print("Welcome to the number guessing game!")
guess = 0

while a != n:
    guess += 1
    a = int(input("Guess a number between 1 and 100: "))
    if a < n:
        print("Enter Higher Number please!")  
        print("Enter Lower Number please!")

print(f"Congratulations! You guessed the number {n} in {guess} attempts.")
print("Thank you for playing!")
