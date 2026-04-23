# Returns the number at position n of the Fibonacci sequence.

def fib(n):
    if n == 1 or n == 2:
        return 1

    prev1 = 1
    prev2 = 1

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current

    return prev2

# term = fib(17)
# print(term)