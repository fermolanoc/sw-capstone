"""
Author: Fernando Molano

Program that turns (almost) any sentence into camelCase style
"""


def validateSentence(sentence):
    # list of characters not valid to start a sentence
    invalid_initial_characters = ['@', '#', '$', '*', '^', '(', ')', '_', '-', '%']

    # if user's sentence starts with one of the invalid characters, keep asking
    while sentence[0] in invalid_initial_characters:
        sentence = input('Sentence must start with a letter. Try again: ')
    

    return sentence


def convertSentenceToCamelCase(sentence):
    # separate the whole sentence into words by space, this will make a list with each word as an item
    list_of_words = sentence.split()

    words_to_capitalize = list_of_words[1:]  # create a new list with all the words that will be capitalize, except the first one

    first_word = list_of_words[0]  # get first word from original list

    camelcase_sentence = first_word.lower()  # create a new variable to store the camelCase style sentence starting with the first world given by the user in lowercase

    # loop thru the list of words that will be capitalized
    for word in words_to_capitalize:
        # capitalize word and concatenate it with what's already stored into camelCase style new sentence
        camelcase_sentence += word.title()
    
    return camelcase_sentence


def main():
    # get user sentence
    sentence = input('Write any sentence: ')


    valid_sentence = validateSentence(sentence)

    camelcase_sentence = convertSentenceToCamelCase(valid_sentence)
    
    print(camelcase_sentence)  # print new sentence which is in camelCase style


main()