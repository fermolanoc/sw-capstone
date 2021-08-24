"""
Author: Fernando Molano

Program to ask user to enter first and last name and create a personalized welcome message
Count how many characters compose the full name and show the info to the user

If user were born in January, show a congrats message as well
"""


def sayHi(first_name, last_name):
    # concatenate first and last name and create a personalized welcome message
    full_name = first_name.title() + ' ' + last_name.title()
    message = f'{full_name}, Welcome to Software Development Capstone Course'

    # show user how many letters compose their full name
    letters_counter = f'Wow, I just realized your whole name contains {len(first_name) + len(last_name)} letters'

    print(message)
    print(letters_counter)


def birthdayMessage(name):
    print(f'{name.title()} your birthday is this month! Congrats! Hope you are having a happy month!')


def main():
    # Get data from user
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    birthday_month = input('What month were you born in: ')


    sayHi(first_name, last_name)

    # if user was born in January, show a congratulations message
    if birthday_month.lower() == 'january':
        birthdayMessage(first_name)


main()