# Devin Goulet, 13 May 2026, Github:Devin Goulet Project 7a

def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

#---TEST---
#def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

#print(multiply(7, 4))   # should print 28
#print(multiply(5, 3))   # should print 15
#print(multiply(9, 2))   # should print 18
#print(multiply(1, 6))   # should print 6