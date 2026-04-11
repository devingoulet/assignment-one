cents = int(input("Please enter an amount in cents less than a dollar.\n"))

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)