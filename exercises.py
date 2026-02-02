# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter(letter):
    letter_lower = letter.lower()
    # checks if letter is not a single letter OR if it isn't in the alphabet
    if len(letter) != 1 or not letter_lower.isalpha():
        return f"'{letter}' is an invalid input."
    
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter_lower in vowels:
        return f"'{letter}' is a vowel."
    else: 
        return f"'{letter}' is a consonant."
    
# Call the function
# print(check_letter('E'))
# print(check_letter('b'))
# print(check_letter('7'))
# print(check_letter('apple'))

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # user input prompt for age
    user_age = input('Please enter your age: ')
    # convert age string to integer
    age = int(user_age)
    # check value
    if age < 0 or age > 120:
        print('That does not appear to be a valid age.')
        return
    
    VOTING_AGE = 18

    if age >= 18:
        print(f"You are {age} years old and eligible to vote!")
    else:
        print(f"You are {age} years old, not quite old enough to vote yet.")

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    age_input = input("Enter a dog's age: ")
    human_years = int(age_input)

    if human_years < 0:
        return 'Age cannot be a negative number.'
    elif human_years <= 2:
        dog_years = human_years * 10
    else:
        dog_years = 20 + (human_years - 2) * 7
    
    return f"The dog's age in dog years is {dog_years}"

# Call the function
# print(calculate_dog_years())

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    is_cold_input = input('Is it cold? Answer yes or no: ').strip().lower()
    is_raining_input = input('Is it raining? Answer yes or no: ').strip().lower()

    is_cold = is_cold_input == 'yes'
    is_raining = is_raining_input == 'yes'

    if (is_cold and is_raining):
        print('Wear a waterproof coat.')
    elif (is_cold and not is_raining):
        print('Wear a warm coat.')
    elif (not is_cold and is_raining):
        print('Carry an umbrella.')
    else:
        print('Wear light clothing.') 

# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month_input = input('Enter the month of the year (Jan-Dec): ').capitalize().strip()
    date_input = int(input('Enter the date (numerical): '))

    season = None

    if (month_input == 'Dec' and date_input >= 21) or (month_input in('Jan', 'Feb')) or (month_input == 'Mar' and date_input <= 19):
        season = 'Winter'
    elif (month_input == 'Mar' and date_input >= 20) or (month_input in('Apr', 'May')) or (month_input == 'Jun' and date_input <= 20):
        season = 'Spring'
    elif (month_input == 'Jun' and date_input >= 21) or (month_input in('Jul', 'Aug')) or (month_input == 'Sep' and date_input <= 21):
        season = 'Summer'
    elif (month_input == 'Sep' and date_input >= 22) or (month_input in ('Oct', 'Nov')) or (month_input == 'Dec' and date_input <= 20):
        season = 'Fall'       
    
    if season:
        print(f"{month_input} {date_input} is in {season}.")
    else: 
        print('Invalid date or month format')
        return     
# Call the function
determine_season()

