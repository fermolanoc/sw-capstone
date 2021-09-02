""" 
Quiz Program

This program will present user categories to choose. Each category will contain different number of questions.
When user answer each question, program will let user know if answer was right or wrong immediately.

A score will be kept and when all the answers have been answered, total score will be shown.
 """


# topic = input('Would you like art, or space questions? ')


topics = [{
    'id': '1',
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
    'id': '2',
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
    category_ids = []

    for topic in topics:
        print(f"\tPress {topic['id']} for {topic['name']}")
        category_ids.append(topic['id'])

    return category_ids


def get_questions(category_id, score):
    category_name = topics[int(category_id) - 1]['name']
    print(f'\nOk, you chose {category_name.title()}. Here are the questions: ')

    questions = topics[int(category_id) - 1]['questions']
    for item in questions:
        for question in item.keys():
            user_answer = input(f'{question} ')
            if user_answer.lower() == item[question].lower():
                print('Correct\n')
                score += 1
            else:
                print(f'No. Answer is {item[question]}\n')


def main():
    total_score = 0

    print('Let\'s play Trivia. Choose one of the following categories:')

    category_ids = get_categories()

    user_choice = input('Selection: ')
    valid_option = False
    while not valid_option:
        if user_choice in category_ids:
            valid_option = True
            score = get_questions(user_choice, total_score)
            break
        else:
            print('That is not a valid topic')
            user_choice = input('Select a category number: ')


main()
