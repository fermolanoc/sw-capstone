""" 
Quiz Program

This program will present user categories to choose. Each category will contain different number of questions.
When user answer each question, program will let user know if answer was right or wrong immediately.

A score will be kept and when all the answers have been answered, total score will be shown.
 """


# topic = input('Would you like art, or space questions? ')


topics = [{
    'id': 1,
    'name': 'art',
    'questions': [
        {
            'Who painted the Mona Lisa?': 'Leonardo Da Vinci'
        },
        {
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli'
        },
        {
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'
        }
    ]
},
    {
    'id': 2,
    'name': 'space',
    'questions': [
        {
            'Which planet is closest to the sun?': 'Mercury'
        },
        {
            'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus'
        },
        {
            'How many moons does Mars have?': '2'
        }
    ]
}]


def get_categories():
    for topic in topics:
        print(f"\tPress {topic['id']} for {topic['name']}")

    user_choice = input('Selection: ')


def main():
    total_score = 0

    print('Let\'s play Trivia. Choose one of the following categories:')

    user_choice = get_categories()


main()
