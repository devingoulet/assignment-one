num = int(input("Please enter a positive integer: "))

print("The factors of", num, "are:")

i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i = i + 1