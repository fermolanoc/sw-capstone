""" A quiz program. """

total_score = 0

topic = input('Would you like art, or space questions? ')

if topic == 'art':

    print('Who painted the Mona Lisa?')
    answer = input('Enter your answer: ')
    if answer == 'Vincent Van Gogh':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the answer is Leonardo Da Vinci.')

    print('What precious stone is used to make the artist\'s pigment ultramarine?')
    answer = input('Enter your answer: ')
    if answer == 'Lapiz lazuli':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Lapiz lazuli.')

    print('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
    answer = input('Enter your answer: ')
    if answer == 'Chicago':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Chicago.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!')


elif topic == 'space':

    print('Which planet is closest to the sun?')
    answer = input('Enter your answer: ')
    if answer == 'Mercury':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Mercury.')

    print('Which planet spins in the opposite direction to all the others in the solar system?')
    answer = input('Enter your answer: ')
    if answer == 'Venus':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Venus.')

    print('How many moons does Mars have?')
    answer = input('Enter your answer: ')
    if answer == '2':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is 2.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!')

else:
    print('That is not a valid topic. Restart the program to try again.')
