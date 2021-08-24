"""
Author: Fernando Molano

Program that turns (almost) any sentence into camelCase style
"""


def main():
    # get user sentence
    sentence = input('Write any sentence: ')

    invalid_initial_characters = ['@', '#', '$', '*', '^', '(', ')', '_', '-']

    while sentence[0] in invalid_initial_characters:
        sentence = input('Sentence must start with a letter. Try again: ')
    
    list_of_words = sentence.split()
    words_to_capitalize = list_of_words[1:]
    print(words_to_capitalize)

    first_word = list_of_words[0]

    camelcase_sentence = first_word.lower()

    for word in words_to_capitalize:
        camelcase_sentence += word.title()
    

    print(camelcase_sentence)


main()