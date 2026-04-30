# Devin Goulet, 29 April 2026, Github:Devin Goulet Project 5a

def without_duplicates(input_list):
    new_list = []

    """Create a new list with duplicate values removed."""

    for item in input_list:
        if item not in new_list:
            new_list.append(item)

    return new_list

# --- TEST ---
#my_list = [8, 'hello', 8, True, -1000000.4, 'hello', 8]
#result = without_duplicates(my_list)

#print(result)