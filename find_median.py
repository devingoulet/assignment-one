# Devin Goulet, 29 April 2026, Github:Devin Goulet Project 5a

def find_median(numbers):
    """
    Returns the median value of a list of numbers.
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2


# --- TESTS ---
#print(find_median([13, 7, -3, 82, 4]))   # expected: 7
#print(find_median([1, 2, 3, 4]))         # expected: 2.5
#print(find_median([5]))                  # expected: 5