""" 
Quiz Program

This program will present user categories to choose. Each category will contain different number of questions.
When user answer each question, program will let user know if answer was right or wrong immediately.

A score will be kept and when all the answers have been answered, total score will be shown.
 """


# Structure with list of topics data. Each list item contain a dictionary with a topic details
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


# function to get the list of categories indexes
def get_categories():
    category_ids = []

    # loop thru the topics list
    for topic in topics:
        print(f"\tPress {topic['id']} for {topic['name']}")
        # add topic id to the array category_ids
        category_ids.append(topic['id'])

    return category_ids


# function to show user questions corresponding to the category chosen. Score will be updated here
def get_questions(category_id, score):
    # get name of category user chose
    category_name = topics[int(category_id) - 1]['name']
    print(f'\nOk, you chose {category_name.upper()}. Here are the questions: ')

    # get the list of questions existing on chosen category
    questions = topics[int(category_id) - 1]['questions']
    for item in questions:
        for question in item.keys():  # get only the key for each question which is the question itself
            user_answer = input(f'{question} ')

            # if user's answer is equal to the value assigned to the question (key), increase score by 1
            if user_answer.lower() == item[question].lower():
                print('Correct\n')
                score += 1
            else:
                print(f'No. Answer is {item[question]}\n')

    return category_name, score


def main():
    total_score = 0

    print('Let\'s play Trivia. Choose one of the following categories:')

    # show category id's and names to user to choose and get list of category ids
    category_ids = get_categories()

    user_choice = input('Selection: ')  # get user selection
    valid_option = False  # flag to validate user selection

    while not valid_option:
        # if user chose a number that exist on the category_ids list, raise flag to stop loop, and read questions for that category
        if user_choice in category_ids:
            valid_option = True
            # get category name and score updated
            category, score = get_questions(user_choice, total_score)
            break
        else:
            print('That is not a valid topic')
            user_choice = input('Select a category number: ')

    # print results
    print(
        f"Your total score on category {category.upper()} is {score} out of {len(topics[int(user_choice) - 1]['questions'])}")


main()
