import random
print("Hello, what is your name?")
name = input()
secretNumber = random.randint(1,20)
print("Well, " + name + ", I am think of a number between 1 and 20")

for gueeseTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is to low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("Good job " + name + "! You guessed my number")
else:
    print("Nope, The number I was thinking of was " + str(secretNumber))