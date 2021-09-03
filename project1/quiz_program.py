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
        print(f"\tPress {topic['id']} for {topic['name'].title()}")
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


def add_topics(number_of_topics_to_add):

    for i in range(number_of_topics_to_add):
        # get id of last topic currently existing on topics list
        last_topic = int(topics[-1]['id'])
        topic_name = input('Enter name of topic/category: ')

        topics.append({
            'id': f'{last_topic + 1}',
            'name': f'{topic_name}',
            'questions': []
        })

        add_questions = input(
            f'Enter Y to add a question to {topic_name} topic now or 0 to skip ')
        while add_questions.upper() == 'Y':
            question = input('Type the question: ')
            answer = input('Now enter the right answer: ')

            # dictionary to be added with the key:value -> question : answer
            question_answer = {question: answer}
            topics[-1]['questions'].append(question_answer)

            add_questions = input(
                f'Enter Y to add another question or 0 to skip ')

        """
        For testing purposes:
        topic name: sports

        Questions with their respective answers to add:
        {
                'What does MLB stand for?': 'Major League Baseball'
        },
        {
                'Which country has won the soccer world cup the most times?': 'Brasil'
        }
        """


def main():
    """ Add another category before user selection """
    # topics_to_add = int(input('How many topics do you want to add? '))
    # add_topics(topics_to_add)

    total_score = 0

    print('Let\'s play Trivia. Choose one of the following categories, answer right as many questions as possible and prove how smart you are:')

    # show category id's and names to user to choose and get list of category ids
    category_ids = get_categories()

    user_choice = input('Selection: ')  # get user selection
    valid_option = False  # flag to validate user selection

    while not valid_option:
        # if user chose a number that exist on the category_ids list, raise flag to stop loop, and read questions for that category
        if user_choice in category_ids:
            valid_option = True
            # call get_questions method passing category user chose and score which initially is 0.
            # Category questions will be asked and score will be updated and returned as well as the category name
            category, score = get_questions(user_choice, total_score)
            break
        else:
            print('That is not a valid topic')
            user_choice = input('Select a category number: ')

    # print results
    number_of_questions = len(topics[int(user_choice) - 1]['questions'])
    print(
        f"Your total score on category {category.upper()} is {score} out of {number_of_questions}")

    # message to be shown only if all answers were right
    if score == number_of_questions:
        print("You got all the answers correct")


main()
