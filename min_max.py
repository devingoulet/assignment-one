count = int(input("How many integers would you like to enter?\n"))
print("Please enter", count, "integers.")

i = 0

num = int(input())
min_num = num
max_num = num
i = i + 1

while i < count:
    num = int(input())

    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num

    i = i + 1

print("min:", min_num)
print("max:", max_num)