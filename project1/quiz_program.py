""" 
Quiz Program

This program will present user categories to choose. Each category will contain different number of questions.
When user answer each question, program will let user know if answer was right or wrong immediately.

A score will be kept and when all the answers have been answered, total score will be shown.
"""


# Structure with list of topics data. Each list item contain a dictionary with a topic details
# Adding structure, and id values, is a good idea.
topics = [{
    'id': '1',
    'name': 'art',
    'questions': [
        {
            # 'Who painted the Mona Lisa?': 'Leonardo Da Vinci'

            # A question clearly relates to the answer, so question keys and answer values make sense. 
            # But in this dictionary, there will only ever be one key-value pair
            # so, its not using the capabilities of a dictionary, and you have more work in get_questions where you loop over the dictionary keys. 
            # How about the same keys in each dictionary, to label questions and answers?  
            # More descriptive, labels what each string is, and also would allow future expansion to store more data about each question,
            # for example custom points per question, difficulty levels etc. 

            'question': 'Who painted the Mona Lisa?',
            'answer': 'Leonardo Da Vinci',
            # 'difficulty': 'moderate',
            # 'points': 1           
            
        },
        {
            'question': 'What precious stone is used to make the artist\'s pigment ultramarine?',
            'answer': 'Lapiz lazuli'
        },
        # {
        #     'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'
        # }
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
# This function does two things - make a list of IDs and print them to the user. 
# Either make the name more specific, or (better) this function should focus on one task.
def get_category_ids():  # be clear this is returning the IDs, not the names 
    category_ids = []

    # loop thru the topics list
    for topic in topics:
        # printing here makes this function do two things. 
        # print(f"\tPress {topic['id']} for {topic['name'].title()}")
        # add topic id to the array category_ids
        category_ids.append(topic['id'])

    # The list comprehension way - optional alternative to the loop 
    # category_ids = [topic['id'] for topic in topics]
    return category_ids


# function to show user questions corresponding to the category chosen. Score will be updated here
# does this fetch and return questions? It looks like it's asking the questions - would this be a better name?
def ask_questions(questions, category_name):  
    # would it be easier to pass the questions list (list of Q:A dictionaries) here and the category/topic name? Less work for the function and it
    # doesn't need to handle subtracting 1 from the category ID to find the correct questions
    
    # Calculate the score from 0.
    # The function can return the score from the list of questions provided, the caller can deal with adding it onto any existing score. 
    # This function shouldn't make assumptions about how the score is used. What if you want to display score by category? 
    score = 0

    # Pass the name as an argument  
    print(f'\nOk, you chose {category_name.upper()}. Here are the questions: ')

    # get the list of questions existing on chosen category - pass this in as an argument
    # questions = topics[int(category_id) - 1]['questions']   # this seems like extra work for this function
    print(questions)
    for item in questions:  # can you use a more specific name?
        # for question in item.keys():  # get only the key for each question which is the question itself
        question = item['question']
        answer = item['answer']       

        user_answer = input(f'{question} ')

        # if user's answer is equal to the value assigned to the question (key), increase score by 1
        if user_answer.lower() == answer.lower():
            print('Correct\n')
            score += 1
        else:
            print(f'No. Answer is {answer}\n')

    return score


# You don't need this feature. 
# A future version of this program may contact an API for the questions, or read from a database; to set the topics data structure. 
# And of course, the rest of your program would work without modification in that case. 
def add_topics(number_of_topics_to_add):

    for i in range(number_of_topics_to_add):
        # get id of last topic currently existing on topics list
        # the -1 and +1 that you need to do to offset the numbers is putting you at risk of off-by-one errors if you forget, or off-by-two errors if you offset the wrong wat
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
    category_ids = get_category_ids()

    # TODO print the topic choices here or call a method to print the choices  
    # Displaying the choices, getting and validating the user input could be a separate function 

    user_choice = input('Selection: ')  # get user selection
    valid_option = False  # flag to validate user selection

    while not valid_option:

        # if user chose a number that exist on the category_ids list, raise flag to stop loop, and read questions for that category
        if user_choice in category_ids:

            # # Code inside a loop is there because at some point, you may need to repeat it. 
            # # This code executes one time so put it after the loop. 
            # topic_name = '' # TODO figure this out here, look up in data strucure 
            # valid_option = True
            # # call get_questions method passing category user chose and score which initially is 0.
            # # Category questions will be asked and score will be updated and returned as well as the category name
            # score = ask_questions(user_choice, topic_name)

            break
        else:
            print('That is not a valid topic')
            user_choice = input('Select a category number: ')

    # Move to after the loop - clearer that this happens one time. If the loop ends, the user has made valid choice.
    category = '' # TODO figure this out here, look up in data strucure 
    # call get_questions method passing category user chose and score which initially is 0.
    # Category questions will be asked and score will be updated and returned as well as the category name

    # Get the questions from the question bank here. 
    questions = topics[int(user_choice) - 1]['questions']
    score = ask_questions(questions, category)

    # Add score to total 
    total_score = total_score + score 

    # print results
    number_of_questions = len(topics[int(user_choice) - 1]['questions'])  # this is a complex line - is there a simpler way to express this? 
    # converting to int, having to subtract 1 to get the right questions, these are both error-prone.
    # What happens if the question IDs don't start at 1, or are not sequential?
    # Think about modifications to your data structure to make it easier to read the data you need. 

    print(
        f"Your total score on category {category.upper()} is {score} out of {number_of_questions}")

    # message to be shown only if all answers were right
    if score == number_of_questions:
        print("You got all the answers correct")


main()
