# Devin Goulet, 13 May 2026, Github:Devin Goulet Project 7a

def list_of_primes_up_to(limit=100):
    primes = [True] * (limit + 1)

    primes[0] = False
    primes[1] = False

    for number in range(4, limit + 1, 2):
        primes[number] = False

    divisor = 3

    while divisor <= limit ** 0.5:
        if primes[divisor]:
            for number in range(divisor * 2, limit + 1, divisor):
                primes[number] = False

        divisor += 1

    return [number for number in range(limit + 1) if primes[number]]

#---TEST---
#result = list_of_primes_up_to(1000)
#print(result)