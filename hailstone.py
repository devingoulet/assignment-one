# Returns the number of steps to reach 1 from n using the hailstone sequence.
def hailstone(n):

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps

# answer = hailstone(3)
# print(answer)