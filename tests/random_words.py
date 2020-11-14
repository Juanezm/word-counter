import json
import random


def generate_random_list_of_words():
    words = ("apple", "apricot", "avocado", "banana",
             "blackberries",  "blueberries", "lemons",
             "mandarin", "nectarines", "oranges", "pears",
             "pineapple", "prunes", "coconut", "grapes")
    word_list = list()
    for i in range(0, random.randint(1, len(words))):
        word_list.append(random.choice(words))
    return word_list


def generate_random_dict_of_words():
    words_list = generate_random_list_of_words()
    words = {}
    for word in words_list:
        words.update({word: random.randint(1, 5)})
    return words


def generate_random_string_of_words():
    words = ("apple", "apricot", "avocado", "banana",
             "blackberries",  "blueberries", "lemons",
             "mandarin", "nectarines", "oranges", "pears",
             "pineapple", "prunes", "coconut", "grapes")
    word_string = ""
    for i in range(0, random.randint(1, len(words))):
        word_string += random.choice(words) + ', '
    return word_string


def initialise_random_words_file(words_file):
    words = generate_random_dict_of_words()

    with open(words_file, "w") as json_file:
        json.dump(words, json_file)

    return words
