import json

from wordcounter.adapters import repository

from tests.random_words import initialise_random_words_file, \
    generate_random_dict_of_words


def test_repository_can_get_words(json_test_file):
    init_words = initialise_random_words_file(json_test_file)

    repo = repository.JsonFileRepository(json_test_file)
    words = repo.get_words()

    assert words == init_words


def test_repository_can_add_words(json_test_file):
    words = generate_random_dict_of_words()

    repo = repository.JsonFileRepository(json_test_file)
    repo.add_words(words)

    with open(json_test_file) as json_file:
        words_in_file = json.load(json_file)

    assert words == words_in_file
