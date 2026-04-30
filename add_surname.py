# Devin Goulet, 29 April 2026, Github:Devin Goulet Project 5a

def add_surname(names):
    return [name + " Kardashian" for name in names if name.startswith("K")]
"""will produce surname Kardashian as long as the first name begins with K"""

# --- TEST ---
#names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]

#result = add_surname(names)
#print(result)