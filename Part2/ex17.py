import random

# List of sample codenames
codenames = ["Fearless Dragon","Mystic Phoenix","Invisible Wolf","Mighty Tiger"]

# Ask for the user's name
name = input("What is your name?\n")

# Generate a random codename
codename = random.choice(codenames)

# Generate a random lucky number
lucky_number = random.randint(1, 100)

# Output the results
print(f"{name}, your codename is: {codename}")
print(f"Your lucky number is: {lucky_number}")