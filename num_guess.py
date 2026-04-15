target = int(input("Enter the integer for the player to guess.\n"))

print("Enter your guess.")
guess = int(input())

count = 1

while guess != target:
    if guess > target:
        print("Too high - try again:")
    else:
        print("Too low - try again:")

    guess = int(input())
    count = count + 1

if count == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in", count, "tries.")